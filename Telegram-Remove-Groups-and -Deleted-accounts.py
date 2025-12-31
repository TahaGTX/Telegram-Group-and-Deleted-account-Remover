import asyncio
from telethon import TelegramClient
from telethon.tl.types import User

api_id = XXXXXXXX
api_hash = "XXXXXXXXXXXXXXXX"
phone = "+91XXXXXXXXXX"

async def main():
    client = TelegramClient(phone, api_id, api_hash)
    await client.start(phone=phone)

    print("Logged in successfully.\n")

    async for dialog in client.iter_dialogs():  # NO LIMIT
        try:
            entity = dialog.entity

            # -------- KEEP ONLY REAL INDIVIDUAL USERS --------
            if isinstance(entity, User):
                if not entity.bot and not entity.deleted:
                    #  Keep normal private chats
                    continue

            #  Remove everything else
            print(f"Removing: {dialog.name}")
            await client.delete_dialog(entity)

        except Exception as e:
            print(f"Skipped {dialog.name}: {e}")

    await client.disconnect()
    print("\nCleanup completed. Only individual chats remain.")


if __name__ == "__main__":
    asyncio.run(main())
