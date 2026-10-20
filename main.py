import asyncio
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.sessions import StringSession

# সরাসরি কোডের ভেতরে তথ্য বসানো হলো
api_id = 30291759
api_hash = '07069b307a8e6726b2a1dbf8f0682d46'

# আপনার সেশন স্ট্রিং (BEGIN, END এবং == ছাড়া শুধু মাঝের অংশ)
session_str = "1BQANOTEuMTA4LjU2LjEzMAG7sdnNuYWoLnP1HO7o/XBFEbH3N4G2aY8+XC0oXzHTb5K/0zGr5ZNZTwphCbMigp0N5npNkyZ0Qc6xSyXaRd7t871ZDd2Ox4qX+G+PrMD1C+Fu0QxHoDCe1WA2R5X1XNSArxSNnITGhJAh5jZtppTgoHwIo5G60t/EG8EcAI/BdngqJEHPG9KhA0t9e6fN2wjX0YvWkFRzaF6yH9g2vm5UtQ4np758s5YgZ0u+0jOJYESSxGqyoorxTGwox8zeBSws6ptrp8ICsfs5oiOuVobU+M9mml7xON/wBOJzdZ3msIA8ejkJe4hHkL4T4o3r9XdA780G1tq25pINScN0/aHCEw"

async def main():
    try:
        client = TelegramClient(StringSession(session_str), api_id, api_hash)
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
        print(f"লগইনে সমস্যা: {e}")

if __name__ == '__main__':
    asyncio.run(main())
