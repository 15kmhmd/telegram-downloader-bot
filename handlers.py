from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 أهلاً بك!\n\n"
        "أرسل رابط فيديو من TikTok أو Instagram أو Facebook وسأحاول تحميله لك."
    )
