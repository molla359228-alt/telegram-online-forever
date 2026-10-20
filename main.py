import asyncio
import base64
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.sessions import StringSession

# সরাসরি কোডের ভেতরে তথ্য স্থাপন করা হয়েছে
api_id = 30291759
api_hash = '07069b307a8e6726b2a1dbf8f0682d46'

# আপনার সেশন স্ট্রিং
session_str = "1BQANOTEuMTA4LjU2LjEzMAG7sdnNuYWoLnP1HO7o/XBFEbH3N4G2aY8+XC0oXzHTb5K/0zGr5ZNZTwphCbMigp0N5npNkyZ0Qc6xSyXaRd7t871ZDd2Ox4qX+G+PrMD1C+Fu0QxHoDCe1WA2R5X1XNSArxSNnITGhJAh5jZtppTgoHwIo5G60t/EG8EcAI/BdngqJEHPG9KhA0t9e6fN2wjX0YvWkFRzaF6yH9g2vm5UtQ4np758s5YgZ0u+0jOJYESSxGqyoorxTGwox8zeBSws6ptrp8ICsfs5oiOuVobU+M9mml7xON/wBOJzdZ3msIA8ejkJe4hHkL4T4o3r9XdA780G1tq25pINScN0/aHCEw"

def fix_base64_padding(s):
    """বেস64 স্ট্রিংয়ের প্যাডিং ঠিক করুন, যাতে এর দৈর্ঘ্য 4 এর গুণিতক হয়"""
    # সমস্ত ফাঁকা অক্ষর (স্পেস, লাইন ব্রেক ইত্যাদি) মুছে ফেলুন
    s = ''.join(s.split())
    # যদি দৈর্ঘ্য 4 এর গুণিতক না হয়, তাহলে '=' দিয়ে পূরণ করুন
    padding = len(s) % 4
    if padding:
        s += '=' * (4 - padding)
    return s

async def main():
    try:
        # ডিকোড করার আগে প্যাডিং ঠিক করুন
        fixed_session = fix_base64_padding(session_str)
        
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
