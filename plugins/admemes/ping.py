"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് Start ചെയ്തു നോക്ക്..🙂" 
HELP = "@Client.on_message(filters.command("help"))
async def help(client, message):
   buttons = [[
            InlineKeyboardButton('Mᴀɴᴜᴇʟ Fɪʟᴛᴇʀ', callback_data='manuelfilter'),
            InlineKeyboardButton('Aᴜᴛᴏ Fɪʟᴛᴇʀ', callback_data='autofilter'),
            InlineKeyboardButton('Cᴏɴɴᴇᴄᴛɪᴏɴs', callback_data='coct')
            ],[
            InlineKeyboardButton('Sᴏɴɢ', callback_data='songs'),
            InlineKeyboardButton('Exᴛʀᴀ', callback_data='extra'),
            InlineKeyboardButton("Vɪᴅᴇᴏ", callback_data='video')
            ],[
            InlineKeyboardButton('Pɪɴ', callback_data='pin'), 
            InlineKeyboardButton('Pᴀsᴛᴇ', callback_data='pastes'),
            InlineKeyboardButton("Iᴍᴀɢᴇ", callback_data='image')
            ],[
            InlineKeyboardButton('Fᴜɴ', callback_data='fun'), 
            InlineKeyboardButton('Jsᴏɴ', callback_data='son'),
            InlineKeyboardButton('TTS', callback_data='ttss')
            ],[
            InlineKeyboardButton('Pᴜʀɢᴇ', callback_data='purges'),
            InlineKeyboardButton('Pɪɴɢ', callback_data='pings'),
            InlineKeyboardButton('Tᴇʟᴇɢʀᴀᴘʜ', callback_data='tele')
            ],[
            InlineKeyboardButton('Wʜᴏɪs', callback_data='whois'),
            InlineKeyboardButton('Mᴜᴛᴇ', callback_data='restric'),
            InlineKeyboardButton('Kɪᴄᴋ', callback_data='zombies')
            ],[
            InlineKeyboardButton('Rᴇᴘᴏʀᴛ', callback_data='report'),
            InlineKeyboardButton('Yᴛ-Tʜᴜᴍʙ', callback_data='ytthumb'),
            InlineKeyboardButton('Sᴛɪᴄᴋᴇʀ-Iᴅ', callback_data='sticker')
            ],[
            InlineKeyboardButton('Cᴏᴠɪᴅ', callback_data='corona'),
            InlineKeyboardButton('Aᴜᴅɪᴏ-Bᴏᴏᴋ', callback_data='abook'),
            InlineKeyboardButton('Uʀʟ-Sʜᴏʀᴛ', callback_data='urlshort')
            ],[
            InlineKeyboardButton('G-Tʀᴀɴs', callback_data='gtrans'),
            InlineKeyboardButton('Fɪʟᴇ-Sᴛᴏʀᴇ', callback_data='newdata'),
            InlineKeyboardButton('Sʜᴀʀᴇ-Tᴇxᴛ', callback_data='sharetext'),
            ],[
            InlineKeyboardButton('Pᴀssᴡᴏʀᴅ-Gᴇɴ', callback_data='genpassword'),
            InlineKeyboardButton('Aᴘᴘʀᴏᴠᴇ', callback_data='approve'),
            InlineKeyboardButton('Gʀᴇᴇᴛɴɢs', callback_data='welcome'),
            ],[
            InlineKeyboardButton('Lᴏᴄᴋs', callback_data='lock'),
            InlineKeyboardButton('Nᴏᴛᴇs', callback_data='note'),
            InlineKeyboardButton('Pᴜʀɢᴇ', callback_data='purge'),
            ],[
            InlineKeyboardButton('Rᴜʟᴇs', callback_data='rule'),
            InlineKeyboardButton('Uʀʟ-Sʜᴏʀᴛɴᴇʀ', callback_data='url'),
            InlineKeyboardButton('Tᴏʀʀᴇɴᴛ', callback_data='torrent'),
            ],[
            InlineKeyboardButton('Bᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('Sᴛᴀᴛᴜs', callback_data='stats'),
            InlineKeyboardButton('Cʟᴏsᴇ ✗', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )"
REPO = "Oops The repo is Vanished Because of CopyCats"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
