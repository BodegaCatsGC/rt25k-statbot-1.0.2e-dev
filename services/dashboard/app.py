from flask import Flask, request, render_template, session, redirect, url_for
import os  # Added missing import

app = Flask(__name__)

@app.route("/")
def index():
    return "Dashboard is live!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

app.secret_key = os.getenv('FLASK_SECRET_KEY', 'supersecret')

import requests

DISCORD_CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
DISCORD_CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")
DISCORD_REDIRECT_URI = os.getenv("DISCORD_REDIRECT_URI", "http://localhost:5000/callback")

@app.route("/login")
def login():
    return redirect(
        f"https://discord.com/api/oauth2/authorize?client_id={DISCORD_CLIENT_ID}&redirect_uri={DISCORD_REDIRECT_URI}&response_type=code&scope=identify"
    )

@app.route("/callback")
def callback():
    code = request.args.get("code")
    data = {
        "client_id": DISCORD_CLIENT_ID,
        "client_secret": DISCORD_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": DISCORD_REDIRECT_URI,
        "scope": "identify"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    access_token = response.json().get("access_token")

    if not access_token:
        return "⛔ Login failed.", 403

    user_response = requests.get(
        "https://discord.com/api/users/@me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user = user_response.json()
    session["discord_user"] = user
    return redirect(url_for("dashboard_home"))

@app.route("/logout")
def logout():
    session.pop("discord_user", None)
    return redirect("/")
