import asyncio
import os
import base64
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.sessions import StringSession

api_id = int(os.environ.get("TELEGRAM_API_ID", 30291759))
api_hash = os.environ.get("TELEGRAM_API_HASH", '07069b307a8e6726b2a1dbf8f0682d46')

# আপনার নতুন সেশন স্ট্রিং এখানে পেস্ট করুন
session_str = "1BVtsOKlTRUuNTeIjxTjh0qxHSsh_nFe8VLnUB_uhdRsJBKlWa9acAbX0gYvb2cQhQMbs6HDEfMngX0rEpp2O0bd1UMtFDk1fx1dCTvO2k74T06A5K499QYWDxhQd4t28yYE-wwjFTfUUGPBRj8ABGR-0zKaCPKpJqfdJnlQHEU7zz59Frmwlgc7-AuH88FtN2kng0r_03vilFvjumc8I1Ynxxb_6yNoeMCQ784QLwtcpFv8Z0Q0CMR2-x8BQ8V1EdYmS2ZVnxGz_5u9o-ujIw0byLqyW-gQNL1jqQzQEDNrj0U-qYywcIEUG4ZmpOnRRswtUlMJ5rk06JAv9PjXkuN2E="

def clean_session(s):
    """স্ট্রিং থেকে অপ্রয়োজনীয় স্পেস ও লাইন ব্রেক মুছে ফেলে এবং প্যাডিং ঠিক করে"""
    if not s:
        return None
    # সব স্পেস, লাইন ব্রেক, ট্যাব মুছে ফেলুন
    s = ''.join(s.split())
    # যদি প্যাডিং (=) অনুপস্থিত থাকে, স্বয়ংক্রিয়ভাবে যোগ করুন
    s += "=" * (-len(s) % 4)
    return s

async def main():
    fixed_session = clean_session(session_str)
    if not fixed_session:
        print("সেশন স্ট্রিং খালি!")
        return

    try:
        client = TelegramClient(StringSession(fixed_session), api_id, api_hash)
        await client.start()
        print("লগইন সফল! অনলাইন স্ট্যাটাস বজায় রাখা শুরু হচ্ছে...")

        while True:
            try:
                await client(UpdateStatusRequest(offline=False))
                print("অনলাইন স্ট্যাটাস পাঠানো হয়েছে")
            except Exception as e:
                print(f"অনলাইন স্ট্যাটাস পাঠাতে সমস্যা: {e}")
            await asyncio.sleep(45)
    except Exception as e:
        print(f"লগইনে সমস্যা: {e}")

if __name__ == '__main__':
    asyncio.run(main())
