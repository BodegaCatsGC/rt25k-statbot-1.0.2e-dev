import sys

try:
    import discord
    import pytesseract
    print("✅ All dependencies are installed.")
    sys.exit(0)
except Exception as e:
    print(f"❌ Health check failed: {e}")
    sys.exit(1)
