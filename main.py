from telethon import TelegramClient, events
from telethon.tl.functions.channels import GetPendingJoinRequests, ApproveChannelJoinRequest
from telethon.tl.functions.messages import SendMessage
import asyncio

api_id = 29118684
api_hash = 'aebe66b9221b83255fb123c7f9eb7cf4'
client = TelegramClient('auto_accept_session', api_id, api_hash)

WELCOME_MSG = "🎉 स्वागत है Samrat परिवार में!\n🔥 यहाँ हर मैच की पक्की भविष्यवाणी सबसे पहले!"

async def main():
    await client.start()
    print("💥 Bot चालू है — Requests को हर 15 सेकंड में चेक करूंगा…")
    while True:
        try:
            result = await client(GetPendingJoinRequests(channel='me'))
            for user in result.users:
                await client(ApproveChannelJoinRequest(channel='me', user_id=user.id))
                await client(SendMessage(user.id, WELCOME_MSG))
                print(f"✅ Approved and welcomed → @{user.username or user.id}")
        except Exception as e:
            print("Error:", e)
        await asyncio.sleep(15)

if _name_ == "_main_":
    asyncio.run(main())
