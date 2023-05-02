import asyncio
from pyrogram import Client, filters
from config import BANNED_USERS
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

AM_COMMAND = get_command("AM_COMMAND")


@app.on_message(
    command(AM_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/94c43633525702295679d.mp4",
        caption=f"""✧ اهلين فيك في اوامر بوت كرستال\n\n -› **جميع اوامر البوت موجودة بالقائمة هذي ، اضغط الازرار الي تحت واستكشف ياوحش**\n\n• Developer -› [كرستال](t.me/SSxHH)\n• Channel -› [𝐒𝐎𝐔𝐑𝐂𝐄  𝐂𝐑𝐘𝐒𝐓𝐀𝐋 (t.me/NO1BROS)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بمنصات الاغاني", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),

                    InlineKeyboardButton(
                        "اوامر خدمية", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        "تحديثات كرستال 🥢", url=f"https://t.me/NO1BROS"),

                ],
            ]
        ),
    )
