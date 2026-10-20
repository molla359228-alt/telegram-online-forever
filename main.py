import asyncio
import os
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.sessions import StringSession

# Railway-র Environment Variables থেকে তথ্য নেবে (যদি না থাকে তবে ডিফল্ট ব্যবহার করবে)
api_id = int(os.environ.get("TELEGRAM_API_ID", 30291759))
api_hash = os.environ.get("TELEGRAM_API_HASH", '07069b307a8e6726b2a1dbf8f0682d46')

# আপনার নতুন সেশন স্ট্রিং সরাসরি এখানে বসানো হলো
session_str = "1BQANOTEuMTA4LjU2LjEzMAG7mmc1nSTAm5J9oc0w9XVc5lJozgo6hy7/v8AWkK3uP3QuEagx+7Wg9ol9Y9JFdZllHx5wsFaMBThRI/02dkIBRTFVyrraqMrhEBgzwwgeohoCba4ci3pE5JDHdbGIas/gs/rvt0TLydcqQ5QOz4lU+6pQcrWkDnfg3FIWEDNd5fNSMKgOrnwZOrq35WNah1QVQ6+dp6VG4xcxWKBi9HyH/F6fHr+pF+UveUAxEyl8O4Rxqh1m1BjaF3VQjEhgtrRDpY246uwsBIuet97R2Isxbfd2nF3CyZw771R1WtKvQryuEroi3wRDSqttyC6Zt17JsIAQkJpgfr0I+8oFShaTFg=="

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
