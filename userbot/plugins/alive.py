"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**Team Joker Member**"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("𝗥𝗘𝗔𝗗𝗬 𝗧𝗢 𝗥𝗔𝗜𝗗 🦾")
    await asyncio.sleep(1.5)
    await alive.edit("`Your Userbot is Working Fine!`\n\n"
                     "`Spam Level:` **Elite**\n\n`Go and Raid some Groups!😼`")
