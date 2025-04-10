# 📦 RT25K StatBot - Changelog

## [1.0.1b] - 2024-04-10
### 🐳 Docker Build Fixes & GitHub Updates
- Fixed all COPY and path issues in `services/dashboard/Dockerfile`
- Added `requirements.txt` directly to dashboard context
- Removed broken `COPY docs` and `COPY services` errors
- Applied `wersplat` as GitHub username in all relevant configs:
  - `README.md`, `push.sh`, `DOCKERHUB.md`, `ghcr.yml`

## [1.0.1c] - 2024-04-10
### 🐛 Critical Docker Fixes
- Fixed bot container failing to find `bot/main.py`
- Updated Dockerfile to copy only the bot folder into `/app/bot/`
- Updated `docker-compose.yml` to use correct Dockerfile path

## [1.0.1d] - 2024-04-10
### 🌐 Dashboard Fix
- Flask server now binds to `0.0.0.0` instead of localhost
- Fixes Docker port forwarding and ERR_CONNECTION_RESET

- Bot now listens to specific channel via `WATCH_CHANNEL_ID` in .env
- Added image attachment handler to trigger OCR placeholder
- Connected real `process_image()` logic from `ocr.py`

## [1.0.2-dev] - 2024-04-10
### 🚧 Development Kickoff
- Initialized development version for next feature cycle
- Inherits all features and fixes from v1.0.1d

## [1.0.2a-dev] - 2024-04-10
### 🆕 Version Increment
- Continued development from `v1.0.2-dev`
- Prepares for additional feature layers (admin-only auth, image metadata, etc.)

## [1.0.2b-dev] - 2024-04-10
### 🐛 Fixes
- Added `python-dotenv` to requirements.txt to resolve missing module error

## [1.0.2c-dev] - 2024-04-10
### 🛠️ Import Fixes
- Added `__init__.py` to make `bot/` a valid Python package
- Updated Dockerfile with `PYTHONPATH` to fix module loading errors

## [1.0.2d-dev] - 2024-04-10
### 🧠 OCR Stub Added
- Added missing `bot/ocr.py` file
- Implemented basic `process_image()` placeholder function
- Integrated full `process_image()` logic with image saving, OCR, stat parsing, and JSON export

## [1.0.2e-dev] - 2024-04-10
### 🔍 OCR Functional Build
- Integrated working `process_image()` with OCR, stat parsing, and image saving
- Added `parser.py` with `normalize_stats()` for structured box score extraction
- Ready for full image-to-leaderboard workflow
- Repackaged with all OCR dependencies installed:
  - ✅ `pytesseract` and `Pillow` in `requirements.txt`
  - ✅ `tesseract-ocr` installed in Dockerfile
