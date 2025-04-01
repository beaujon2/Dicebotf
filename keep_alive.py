import requests
import time

URL = "https://dicebotf-oo87.onrender.com"

while True:
    try:
        requests.get(URL)
        print("Ping envoyé")
    except Exception as e:
        print("Erreur :", e)
    time.sleep(300)  # Ping toutes les 5 minutes
