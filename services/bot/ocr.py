import os
import discord
import pytesseract
from PIL import Image
from io import BytesIO
from datetime import datetime
from bot.parser import normalize_stats

async def process_image(bot, message):
    for attachment in message.attachments:
        if not attachment.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            await message.channel.send("⚠️ Please upload a valid image file (.png, .jpg, .jpeg)")
            return

        try:
            # Download image bytes
            image_bytes = await attachment.read()
            image = Image.open(BytesIO(image_bytes))

            # Save original image
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"output/screenshots/{timestamp}_{attachment.filename}"
            os.makedirs("output/screenshots", exist_ok=True)
            image.save(filename)

            # Run OCR
            raw_text = pytesseract.image_to_string(image)
            if not raw_text.strip():
                await message.channel.send("😕 OCR found no text in the image.")
                return

            # Normalize stats
            parsed_players = normalize_stats(raw_text)
            if not parsed_players:
                await message.channel.send("📄 OCR succeeded, but no valid stat lines were detected.")
                return

            # Save result
            game_data = {
                "timestamp": datetime.now().isoformat(),
                "source_image": filename,
                "players": parsed_players
            }

            game_json_path = f"output/{timestamp}_game.json"
            os.makedirs("output", exist_ok=True)
            with open(game_json_path, "w") as f:
                import json
                json.dump(game_data, f, indent=2)

            # Discord response
            top_player = max(parsed_players, key=lambda p: p["PTS"])
            await message.channel.send(f"✅ OCR complete! Top scorer: **{top_player['name']}** with **{top_player['PTS']}** points.")

        except Exception as e:
            await message.channel.send(f"❌ Error during OCR processing: {str(e)}")
