import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5971971751:AAEJYE9EGQw7RvtLE1dluzSifgLEy-HlvL4")

API_ID = int(os.environ.get("API_ID", "21970746"))

API_HASH = os.environ.get("API_HASH", "32deb816dc3874e871b6158673fd3683")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
