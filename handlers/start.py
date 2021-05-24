from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAx0CS3uSDgACCXFgq2Z06ZZ64aOjyc0xt3l4vFM3HAACzQsAAnNKWEkyBTLDU--O7R8E")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI am  𝐋𝐔𝐂𝐈𝐅𝐄𝐑 𝐌𝐔𝐒𝐈𝐂, an efficient and a perfect bot that lets you play music in your Telegram groups voice chat
Maintained by @D3VIL_LUCIFER ❤
\nTo add in your group contact @D3VIL_LUCIFER.
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑 Owner", url="https://t.me/D3VIL_LUCIFER",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/LUCIFER_OP_MUSIC_BOT?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑 Owner", url="https://t.me/D3VIL_LUCIFER"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑 Owner", url="https://t.me/D3VIL_LUCIFER"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/AwesomeSupport"
                    )
                ]
            ]
        )
    )    
