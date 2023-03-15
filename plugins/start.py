from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os

CHANNEL = os.environ.get('CHANNEL', "-1001856961053")
STRING = os.environ.get("STRING", "BQFPPzoAjmRiU_7vE2yAKnizU4-JIzZ8IgsddWK2rTyu_zhd81XL0qCLR6w9L1nnhYb_YqUAV1S2DScVhyxdjC4N0ncIYFWSNki7j9v2YjgJPX7D0Z7l2rJ8AuqWAgzU8ELKekjJejyYU5cq_dVi6l0PaoZZv6MVNVYKjD4D-qaxklYkre03pAN9Z5NDWPiisN6fHF7O3emiivEh8t4dGOWBcIQtTlBFQRXldYj5AOx4yPC8voGes4hkUGXlYakr39ji9VKWkrxmu-rxi85in0Vt4MK_TEFbSgq2_fE_73b0M3BaDvPtL6X9nA5kx1d6V8ziTXXFKCi6KT3OFbzBGe7iqhXXawAAAAFj9Q6nAQ")
ADMIN = int(os.environ.get("ADMIN", 1987289639))
bot_username = os.environ.get("BOT_USERNAME","bamel_file_renamer_bot")
log_channel = int(os.environ.get("LOG_CHANNEL", "-1001543295404"))
token = os.environ.get('TOKEN', '5971971751:AAEJYE9EGQw7RvtLE1dluzSifgLEy-HlvL4')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "https://te.legra.ph/file/a5f387534683a7f021dc5.jpg")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "❤️ Good morning ❤️"
elif 12 <= currentTime.hour < 12:
    wish = '🤍 Good afternoon 🤍'
else:
    wish = '🦋 Good evening 🦋'

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""Hello {wish} {message.from_user.first_name } \n\n
	I am file renamer bot, Please sent any telegram**Document Or Video** and enter new filename to rename it"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("🎥 Movie Channel 🎥", url="https://t.me/newnetflixmovies_Premium")],
                                      [InlineKeyboardButton("🦋 Subscribe us 🦋", url="https://youtube.com/@BamelMoviesOfficial")],
                                      [InlineKeyboardButton("Support Group", url='https://t.me/Bamel_Backup'),
                                      InlineKeyboardButton("🔺 Update Channel 🔺", url='https://t.me/Bamel_Backup')],
                                      [InlineKeyboardButton("☕ Buy Me A Coffee ☕", url='https://t.me/Bamel_Group/302')]
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "Your Friend is Already Using Our Bot")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("🎥 Movie Channel 🎥", url="https://t.me/newnetflixmovies_Premium")],
                                              [InlineKeyboardButton("🦋 Subscribe us 🦋", url="https://youtube.com/@BamelMoviesOfficial")],
                                              [InlineKeyboardButton("Support Group", url='https://t.me/Bamel_Backup'),
                                             InlineKeyboardButton("🔺 Update Channel 🔺", url='https://t.me/Bamel_Backup')],
                                             [InlineKeyboardButton("☕ Buy Me A Coffee ☕", url='https://t.me/Bamel_Group/302')]
                                          ]))
            except:
                return
        else:
            await client.send_message(id, "Congrats! You Won 100MB Upload limit")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 104857600
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"""
	Hello {wish} {message.from_user.first_name }\n\n
	__I am file renamer bot, Please send any telegram 
	**Document Or Video** and enter new filename to rename it__
	""", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🔺 Update Channel 🔺", url="https://t.me/Bamel_Backup")],
                                          [InlineKeyboardButton("🦋 Subscribe us 🦋", url="https://youtube.com/@BamelMoviesOfficial")],
                                          [InlineKeyboardButton("Support Group", url='https://t.me/Bamel_Backup'),
                                          InlineKeyboardButton("Movie Channel", url='https://t.me/newnetflixmovies_Premium')],
                                          [InlineKeyboardButton("☕ Buy Me A Coffee ☕", url='https://t.me/Bamel_Group/302')]
                                          ]))
    


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("**__You are not subscribed my channel__** ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"🦋 #Bamel Movie Log 🦋,\n\n**ID** : `{user_id}`\n**Name**: {message.from_user.first_name} {message.from_user.last_name}\n**User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 Restrict User ( **pm** ) 🔺", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("Use About cmd first /about")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"",
                                  reply_markup=InlineKeyboardMarkup([
                                                                     [InlineKeyboardButton("🦋 Contact Developer 🦋", url='https://telegram.me/Bamel_Shab')],
                                                                     [InlineKeyboardButton("🔺 Watch Tutorial 🔺", url='https://youtube.com/@BamelMoviesOfficial')],
                                                                     [InlineKeyboardButton("🦋 Visit Channel  ", url='https://t.me/Bamel_Backup'),
                                                                     InlineKeyboardButton("  Support Group 🦋", url='https://t.me/Bamel_Backup')],
                                                                     [InlineKeyboardButton("☕ Buy Me A Coffee ☕", url='https://t.me/Bamel_Group/302')]

        await message.reply_text(text=f"🦋")
        return 

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 60
    else:
        LIMIT = 1
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% of daily {humanbytes(limit)} data quota exhausted.\n\n  File size detected {humanbytes(file.file_size)}\n  Used Daily Limit {humanbytes(used)}\n\nYou have only **{humanbytes(remain)}** left on your Account.\nIf U Want to Rename Large File Upgrade Your Plan ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daily Limit {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rename", callback_data="rename"), InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Your Plan Expired On {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Can't upload files bigger than 2GB ")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 1288490188)
                    usertype(message.from_user.id, "Free")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rename", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
