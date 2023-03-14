import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5971971751:AAEJYE9EGQw7RvtLE1dluzSifgLEy-HlvL4")

API_ID = int(os.environ.get("API_ID", "21970746"))

API_HASH = os.environ.get("API_HASH", "32deb816dc3874e871b6158673fd3683")

STRING = os.environ.get("STRING", "BQFPPzoAjmRiU_7vE2yAKnizU4-JIzZ8IgsddWK2rTyu_zhd81XL0qCLR6w9L1nnhYb_YqUAV1S2DScVhyxdjC4N0ncIYFWSNki7j9v2YjgJPX7D0Z7l2rJ8AuqWAgzU8ELKekjJejyYU5cq_dVi6l0PaoZZv6MVNVYKjD4D-qaxklYkre03pAN9Z5NDWPiisN6fHF7O3emiivEh8t4dGOWBcIQtTlBFQRXldYj5AOx4yPC8voGes4hkUGXlYakr39ji9VKWkrxmu-rxi85in0Vt4MK_TEFbSgq2_fE_73b0M3BaDvPtL6X9nA5kx1d6V8ziTXXFKCi6KT3OFbzBGe7iqhXXawAAAAFj9Q6nAQ")



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
