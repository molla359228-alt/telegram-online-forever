import asyncio
import os
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.sessions import StringSession

# Railway Variable থেকে তথ্য নেবে
api_id = int(os.environ.get("TELEGRAM_API_ID", 30291759))
api_hash = os.environ.get("TELEGRAM_API_HASH", '07069b307a8e6726b2a1dbf8f0682d46')
session_str = os.environ.get("TELEGRAM_SESSION_STRING")

async def main():
    if not session_str:
        print("ত্রুটি: Railway-তে TELEGRAM_SESSION_STRING সেট করা নেই!")
        return

    try:
        # Railway থেকে পাওয়া স্ট্রিংটি ডিকোড করা
        client = TelegramClient(StringSession(session_str.strip()), api_id, api_hash)
        await client.start()
        print("লগইন সফল! অনলাইন স্ট্যাটাস বজায় রাখা শুরু হচ্ছে...")

        while True:
            try:
                await client(UpdateStatusRequest(offline=False))
                print("অনলাইন স্ট্যাটাস পাঠানো হয়েছে")
            except Exception as e:
                print(f"অনলাইন স্ট্যাটাস পাঠাতে সমস্যা: {e}")
            
            await asyncio.sleep(45)
            
    except Exception as e:
        print(f"লগইনে সমস্যা হয়েছে (স্ট্রিংটি সম্ভবত ভুল): {e}")

if __name__ == '__main__':
    asyncio.run(main())
