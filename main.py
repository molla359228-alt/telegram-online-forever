import asyncio
import os
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.sessions import StringSession

# Railway-র Environment Variables থেকে তথ্য নেবে (যদি না থাকে তবে ডিফল্ট ব্যবহার করবে)
api_id = int(os.environ.get("TELEGRAM_API_ID", 30291759))
api_hash = os.environ.get("TELEGRAM_API_HASH", '07069b307a8e6726b2a1dbf8f0682d46')

# আপনার নতুন তৈরি করা সেশন স্ট্রিং সরাসরি এখানে বসানো হলো
session_str = "1BVtsOKlTRUuNTeIjxTjh0qxHSsh_nFe8VLnUB_uhdRsJBKlWa9acAbX0gYvb2cQhQMbs6HDEfMngX0rEpp2O0bd1UMtFDk1fx1dCTvO2k74T06A5K499QYWDxhQd4t28yYE-wwjFTfUUGPBRj8ABGR-0zKaCPKpJqfdJnlQHEU7zz59Frmwlgc7-AuH88FtN2kng0r_03vilFvjumc8I1Ynxxb_6yNoeMCQ784QLwtcpFv8Z0Q0CMR2-x8BQ8V1EdYmS2ZVnxGz_5u9o-ujIw0byLqyW-gQNL1jqQzQEDNrj0U-qYywcIEUG4ZmpOnRRswtUlMJ5rk06JAv9PjXkuN2E="

async def main():
    try:
        # Session String দিয়ে কানেক্ট করা
        client = TelegramClient(StringSession(session_str), api_id, api_hash)
        await client.start()
        print("লগইন সফল! অনলাইন স্ট্যাটাস বজায় রাখা শুরু হচ্ছে...")

        while True:
            try:
                # Telegram সার্ভারকে জানান যে আপনি অনলাইন (offline=False)
                await client(UpdateStatusRequest(offline=False))
                print("অনলাইন স্ট্যাটাস পাঠানো হয়েছে")
            except Exception as e:
                print(f"অনলাইন স্ট্যাটাস পাঠাতে সমস্যা: {e}")
            
            # প্রতি ৪৫ সেকেন্ড পর পর অনলাইন সিগন্যাল পাঠাবে
            await asyncio.sleep(45)
            
    except Exception as e:
        print(f"লগইনে সমস্যা হয়েছে: {e}")

if __name__ == '__main__':
    asyncio.run(main())
