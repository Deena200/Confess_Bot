
import os
import asyncio
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    print("🤫 Ragasiya Arai Bot Started")
    print(f"Token Loaded: {'Yes' if TOKEN else 'No'}")

    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
