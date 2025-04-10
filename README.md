# RT25K StatBot

![Build](https://github.com/wersplat/rt25k-statbot/actions/workflows/test.yml/badge.svg)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/wersplat/rt25k-statbot.git
cd rt25k-statbot
```

### 2. Configure Environment Variables
Copy the example `.env` file and update it with your values:
```bash
cp .env.example .env
```

### 3. Run the Application
Use Docker Compose to build and run the services:
```bash
docker-compose up --build -d
```

Visit the dashboard at [http://localhost:5000](http://localhost:5000).

## Features
- Discord bot for OCR and stat parsing
- Flask dashboard for game management
- Google Sheets integration for leaderboard updates