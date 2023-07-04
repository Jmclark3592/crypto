# API allows 5 calls per second
# whale address to track: 0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe
# my address: 0x15378FA7495bac16040877F7E17c6547481687F6

import requests
import json
import smtplib
import time
import os

# connect to API
url = "https://api.etherscan.io/api"
address = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"
API_KEY = os.getenv("API_KEY")

params = {
    "module": "account",
    "action": "balance",
    "address": address,
    "tag": "latest",
    "apikey": API_KEY,
}

prev_bal = None

while True:
    response = requests.get(url, params=params)
    data = response.json()
    current_bal = float(data["result"]) / 10**18
    print(f"Current Balance: {current_bal} ETH")

    if prev_bal is not None and prev_bal - current_bal >= 10000:
        print("Sending alert - will replace with actual alert")
        # configure to send to my email or SMS text
        # maybe use smtplib for email

    prev_bal = current_bal

    time.sleep(60)
