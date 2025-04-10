# 📘 RT25K StatBot Manual

This manual covers how to use the RT25K StatBot system — including the bot, dashboard, exports, and developer tools.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/wersplat/rt25k-statbot.git
cd rt25k-statbot
```

### 2. Add Environment Variables
Copy the example file and update:
```bash
cp .env.example .env
```

Set values:
- `DISCORD_TOKEN`
- `SPREADSHEET_ID`
- `GOOGLE_APPLICATION_CREDENTIALS`
- `API_TOKEN`
- `WEBHOOK_URL`

---

## 🐳 Run with Docker

Start the full system:
```bash
docker-compose up --build -d
```

This starts:
- Discord bot (image OCR + stat embed)
- Flask dashboard (http://localhost:5000)

---

## 💬 Discord Commands

| Command        | Description                                   |
|----------------|-----------------------------------------------|
| `!mvp`         | Recalculates MVP from last game               |
| `!winner`      | Announces the winning team                    |
| `!refresh`     | Reruns OCR on the last uploaded image         |
| `!export`      | Pushes game data to Google Sheets             |
| `!leaderboard` | Posts top stats (PTS, MVPs, Wins, Losses)     |

---

## 📊 Dashboard Routes

- `/` → Dashboard Home
- `/games` → List of all uploaded games
- `/leaderboard` → Live leaderboard from SQLite

---

## 🧾 Output Logs

All processed games are saved to:
```
/output/YYYY-MM-DD_game.json
/output/YYYY-MM-DD_game.csv
```

Also synced to:
- Google Sheets (new tab per game)
- SQLite for leaderboard
- JSON/CSV archive folder

---

## 🧠 Developer Tips

### Run tests
```bash
pytest
```

### Health check
```bash
docker exec rt25k-discord-bot python healthcheck.py
```

### GitHub Tag + Release
```bash
./tag_and_release.sh
```

---

## 🧼 Common Fixes

| Problem                        | Fix                                             |
|-------------------------------|--------------------------------------------------|
| Docker build fails on COPY    | Make sure required files exist in build context |
| Blank dashboard               | Upload game screenshots to Discord              |
| Discord commands don't work   | Check your `.env` and role permissions          |

---

Built for Bodega Cats GC and the Road to $25K Series 🏀
