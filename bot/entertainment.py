# Copyright (C) 2021 By VeezMusicProject
# module by @tofikdn

import requests
from pyrogram import Client

from config import Veez
from helpers.filters import command


@Client.on_message(command(["asupan", f"asupan@{Veez.BOT_USERNAME}"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        await message.reply_text("failed to get asupan from server...")
        print(ex)


@Client.on_message(command(["wibu", f"wibu@{Veez.BOT_USERNAME}"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        print(ex)
        await message.reply_text("failed to get wibu from server...")


@Client.on_message(command(["chika", f"chika@{Veez.BOT_USERNAME}"]))
async def chika(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        print(ex)
        await message.reply_text("failed to get chika from server...")


@Client.on_message(command(["truth", f"truth@{Veez.BOT_USERNAME}"]))
async def truth(_, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception as ex:
        print(ex)
        await message.reply_text("something went wrong...")


@Client.on_message(command(["dare", f"dare@{Veez.BOT_USERNAME}"]))
async def dare(_, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception as ex:
        print(ex)
        await message.reply_text("something went wrong...")
