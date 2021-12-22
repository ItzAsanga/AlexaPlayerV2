
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**Hay Homiis This is Super Powerfull Music Player of AleXa OweNs \n You can Play Songs In Voice Chat Smothly And Without Buffering**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰Developer❱", url="https://t.me/Asanga_Udara")
                  ],[ 
                    InlineKeyboardButton(
                        "❰𝗖𝗼𝗺𝗺𝗮𝗱𝘀❱", url="https://api.asangabro.ga"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("ping") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲..😎**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://asangabro.ga#contact")
                ]
            ]
        )
   )
