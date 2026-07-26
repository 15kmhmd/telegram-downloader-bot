from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import BOT_NAME, DEVELOPER_URL, CHANNEL_URL

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📥 تحميل فيديو",
                    callback_data="download"
                ),
                InlineKeyboardButton(
                    text="🎵 استخراج MP3",
                    callback_data="mp3"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="👨‍💻 المطور",
                    url=DEVELOPER_URL
                ),
                InlineKeyboardButton(
                    text="📢 القناة",
                    url=CHANNEL_URL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ℹ️ المساعدة",
                    callback_data="help"
                )
            ]
        ]
    )

    await message.answer(
        f"""
<b>👋 أهلاً بك في {BOT_NAME}</b>

📥 أرسل رابط فيديو من:

• TikTok
• Instagram
• Facebook
• YouTube
• X (Twitter)

⚡ وسأقوم بتحميله وإرساله لك بأفضل جودة ممكنة.

━━━━━━━━━━━━━━━
👨‍💻 <b>Developed by Abu Janat</b>
""",
        reply_markup=keyboard,
    )
