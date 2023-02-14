import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5971971751:AAEJYE9EGQw7RvtLE1dluzSifgLEy-HlvL4")

API_ID = int(os.environ.get("API_ID", "21970746"))

API_HASH = os.environ.get("API_HASH", "32deb816dc3874e871b6158673fd3683")

STRING = os.environ.get("STRING", "BQFPPzoAiTY8y1h9CmChiQzFISKdR3WM3wWR61-KHcXjZxfp-p3XUM221t_bFjOJsGIpgSfe9rO7OmEJX9FouAYbl4HDW0JASGHnpDczavTeutb5hVmXy8Lsc7ZV-qBbDWf04AKTF_BnjJHFF-WqFf0OCnt1Khah8S-wUZpAxbOZIPMGNdu1gz3TxRhTuMk0C5u5h4Uv8KjWzDlszr9DfJzfR6gU1CQnhS11xJjY467ZfJoCQnuHGGVJVX4cVkp93ic9OoDUstmL7auIv6HcujtMGNI3uqhQG0eX-QYk5BM_cxrxH1-w_bRSuNlYXrxexk2inMcF7lnAxN7-DGYKMb4PaunvyAAAAAFlXtjmAQ")



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
