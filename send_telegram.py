import json, urllib.request, urllib.error, os

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

with open("news.md", "r") as f:
    message = f.read()

chunks = [message[i:i+4000] for i in range(0, len(message), 4000)]
for i, chunk in enumerate(chunks):
    data = json.dumps({"chat_id": CHAT_ID, "text": chunk, "disable_web_page_preview": True}).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as r:
        result = json.loads(r.read().decode())
        print(f"ok={result.get('ok')}, msg_id={result.get('result', {}).get('message_id')}")
