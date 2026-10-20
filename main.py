import asyncio
import os
import re
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.sessions import StringSession

# Railway-র Environment Variables থেকে তথ্য নেবে
api_id = int(os.environ.get("TELEGRAM_API_ID", 30291759))
api_hash = os.environ.get("TELEGRAM_API_HASH", '07069b307a8e6726b2a1dbf8f0682d46')
raw_session = os.environ.get("TELEGRAM_SESSION_STRING", "")

# স্ট্রিংয়ের ভেতরের অপ্রয়োজনীয় স্পেস বা নতুন লাইন মুছে ফেলার ফাংশন
def clean_session(session):
    if not session:
        return None
    # BEGIN, END এবং == চিহ্ন বাদ দেওয়া
    session = session.replace("-----BEGIN STRING SESSION-----", "")
    session = session.replace("-----END STRING SESSION-----", "")
    session = session.replace("==", "")
    # সব নতুন লাইন এবং স্পেস মুছে ফেলা
    session = re.sub(r'\s+', '', session)
    return session

session_str = clean_session(raw_session)

async def main():
    if not session_str:
        print("ত্রুটি: Railway-তে TELEGRAM_SESSION_STRING সেট করা নেই!")
        return

    try:
        # Session String দিয়ে কানেক্ট করা
        client = TelegramClient(StringSession(session_str), api_id, api_hash)
        await client.start()
        print("লগইন সফল! অনলাইন স্ট্যাটাস বজায় রাখা শুরু হচ্ছে...")

        while True:
            try:
                await client(UpdateStatusRequest(offline=False))
                print("অনলাইন স্ট্যাটাস পাঠানো হয়েছে")
            except Exception as e:
                print(f"অনলাইন স্ট্যাটাস পাঠাতে সমস্যা: {e}")
            
            # প্রতি ৪৫ সেকেন্ড পর পর অনলাইন সিগন্যাল পাঠাবে
            await asyncio.sleep(45)
            
    except Exception as e:
        print(f"লগইনে সমস্যা হয়েছে, সেশনটি সঠিক নয়: {e}")

if __name__ == '__main__':
    asyncio.run(main())
