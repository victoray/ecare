import json
import os

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    raw = os.getenv("FIREBASE_SERVICE_JSON", "{}")
    with open("credentials.json", "w") as f:
        cred = json.loads(raw)
        json.dump(cred, f)
