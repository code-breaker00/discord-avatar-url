from flask import Flask, redirect
import requests
import os

app = Flask(__name__)


BOT_TOKEN = os.environ.get("BOT_TOKEN")
print("BOT_TOKEN lu :", BOT_TOKEN[:6] + "..." if BOT_TOKEN else "Non défini")

@app.route("/<discord_id>")
def avatar_redirect(discord_id):
    url = f"https://discord.com/api/users/{discord_id}"
    headers = {"Authorization": f"Bot {BOT_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return redirect("https://cdn.discordapp.com/embed/avatars/0.png", code=302)

    data = response.json()
    avatar = data.get("avatar")

    if avatar:
        avatar_url = f"https://cdn.discordapp.com/avatars/{discord_id}/{avatar}.png?size=1024"
    else:
        avatar_url = "https://cdn.discordapp.com/embed/avatars/0.png"

    return redirect(avatar_url, code=302)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

