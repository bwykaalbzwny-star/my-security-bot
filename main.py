
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
import asyncio

# --- ضع بياناتك هنا ---
API_ID = 35155369
API_HASH = "1a56f40cb94b019f6f0318add045f1f3"
BOT_TOKEN = "8420084014:AAGeSCEMJFEAKs9gtG5fRROp4-t7HqJcsFs"
# --------------------

app = Client("guard_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 1. رسالة ترحيب عند دخول عضو جديد
@app.on_chat_member_updated()
async def welcome(client, update):
    if update.new_chat_member:
        user = update.new_chat_member.user
        await client.send_message(update.chat.id, f"أهلاً بك يا {user.mention} في المجموعة! يرجى الالتزام بالقوانين.")

# 2. حذف الروابط تلقائياً لغير المشرفين
@app.on_message(filters.group & filters.regex(r"(https?://\S+|t\.me/\S+)"))
async def delete_links(client, message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status not in ["administrator", "creator"]:
        await message.delete()

# 3. أمر الطرد (بالرد على الشخص بكلمة طرد)
@app.on_message(filters.command("طرد") & filters.group)
async def ban_user(client, message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status in ["administrator", "creator"]:
        if message.reply_to_message:
            await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.reply(f"✅ تم طرد {message.reply_to_message.from_user.first_name}")

# 4. أمر الكتم (بالرد على الشخص بكلمة كتم)
@app.on_message(filters.command("كتم") & filters.group)
async def mute_user(client, message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status in ["administrator", "creator"]:
        if message.reply_to_message:
            await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
            await message.reply(f"🔇 تم كتم {message.reply_to_message.from_user.first_name}")

print("البوت يعمل الآن بنجاح...")
app.run()
