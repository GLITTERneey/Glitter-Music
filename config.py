import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Rio Music")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/7da420adf9bc7ef02f71a.jpg")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/18d25616d9883400af112.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/47ba4feefcaeb718b7ca6.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/3ba727ff3ba2542022dbf.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/3ba727ff3ba2542022dbf.jpg")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/e954fc1ac5f7aa16d4f91.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "rio2robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "rioasistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "riogroupsupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "riobotsupport")
OWNER_NAME = getenv("OWNER_NAME", "fckualot") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "fckualot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
