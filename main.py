from pyrogram import Client, filters
from pyrogram.types import Message

# --- بيانات الاتصال الرسمية الخاصة بك ---
API_ID = 8521546538
API_HASH = "1a56f40cb94b019f6f0318add045f1f3"
BOT_TOKEN = "8420084014:AAGeSCEMJFEAKs9gtG5fRROp4-t7HqJcsFs"

app = Client("my_security_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- قائمة الأوامر ---
@app.on_message(filters.command("الاوامر"))
async def commands_list(client: Client, message: Message):
    text = """
🤖 **بوت الحماية الخاص بك جاهز ومستقر!**

إليك الأوامر المتاحة:
• `ايدي` - لعرض الايدي الخاص بك.
• `معلوماتي` - لعرض تفاصيل حسابك.
• `الاوامر` - لعرض هذه القائمة.

✅ البوت يعمل الآن بنجاح على سيرفر Koyeb بنظام الـ Worker.
    """
    await message.reply(text)

# --- أمر الايدي ---
@app.on_message(filters.command("ايدي"))
async def get_id(client: Client, message: Message):
    await message.reply(f"🆔 الايدي الخاص بك هو: `{message.from_user.id}`")

# --- أمر معلوماتي ---
@app.on_message(filters.command("معلوماتي"))
async def my_info(client: Client, message: Message):
    user = message.from_user
    info = f"""
👤 **معلوماتك الشخصية:**
• الاسم: {user.first_name}
• المعرف: @{user.username if user.username else 'لا يوجد'}
• الايدي: `{user.id}`
    """
    await message.reply(info)

# تشغيل البوت
print("--- البوت بدأ العمل الآن بنجاح! ---")
app.run()
