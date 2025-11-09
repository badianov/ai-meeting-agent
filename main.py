from fastapi import FastAPI, Request
import os
from notion_client import Client
from dotenv import load_dotenv

# Load env variables
load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")

print(f"✅ NOTION_API_KEY loaded: {NOTION_API_KEY[:6]}...{NOTION_API_KEY[-4:]}")
print(f"✅ NOTION_DB_ID: {NOTION_DB_ID}")

notion = Client(auth=NOTION_API_KEY)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Meeting Agent running ✅"}


# ✅ MAIN WEBHOOK ENDPOINT
@app.post("/notion/webhook")
async def notion_webhook(request: Request):
    headers = dict(request.headers)

    try:
        body = await request.json()
    except:
        body = {}

    print("\n🔔 NOTION WEBHOOK RECEIVED")
    print("Headers:", headers)
    print("Payload:", body)

    # ✅ Required by Notion: respond to verification challenge
    if "challenge" in body:
        print(f"🟢 Challenge received from Notion: {body['challenge']}")
        return {"challenge": body["challenge"]}

    # ✅ After verification, real events will arrive here
    print("✅ Webhook handled successfully.")
    return {"ok": True}