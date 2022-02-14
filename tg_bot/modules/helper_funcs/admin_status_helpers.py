# admin status module by Luke (@itsLuuke - t.me/itsLuuke)
# written for OdinRobot
# copyright 2022
# this module contains various helper functions/classes to help with the admin status module

from enum import Enum
from cachetools import TTLCache

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, Message

from tg_bot import OWNER_ID, SYS_ADMIN, DEV_USERS, MOD_USERS, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS

# stores admin in memory for 10 min.
ADMINS_CACHE = TTLCache(maxsize = 512, ttl = 60 * 10)

# stores bot admin status in memory for 10 min.
BOT_ADMIN_CACHE = TTLCache(maxsize = 512, ttl = 60 * 10)

DEV_USERS = DEV_USERS

SUDO_USERS = SUDO_USERS + DEV_USERS

WHITELIST_USERS = WHITELIST_USERS + SUDO_USERS

SUPPORT_USERS = SUPPORT_USERS + SUDO_USERS

MOD_USERS = MOD_USERS + SUDO_USERS


class AdminPerms(Enum):
	CAN_RESTRICT_MEMBERS = 'can_restrict_members'
	CAN_PROMOTE_MEMBERS = 'can_promote_members'
	CAN_INVITE_USERS = 'can_invite_users'
	CAN_DELETE_MESSAGES = 'can_delete_messages'
	CAN_CHANGE_INFO = 'can_change_info'
	CAN_PIN_MESSAGES = 'can_pin_messages'
	IS_ANONYMOUS = 'is_anonymous'


class UserClass(Enum):
	ADMIN = SUDO_USERS
	MOD = MOD_USERS


class ChatStatus(Enum):
	CREATOR = "creator"
	ADMIN = "administrator"


class SuperUsers(Enum):
	Owner = [OWNER_ID]
	SysAdmin = [OWNER_ID, SYS_ADMIN]
	Devs = DEV_USERS
	Sudos = SUDO_USERS
	Supports = SUPPORT_USERS
	Whitelist = WHITELIST_USERS
	Mods = MOD_USERS


def anon_reply_markup(cb_id: str) -> InlineKeyboardMarkup:
	return InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
							text = 'Prove identity',
							callback_data = cb_id
					)
				]
			]
	)


anon_reply_text = "Seems like you're anonymous, click the button below to prove your identity"


def edit_anon_msg(msg: Message, text: str):
	"""
	edit anon check message and remove the button
	"""
	msg.edit_text(text, parse_mode = ParseMode.MARKDOWN, reply_markup = None)


anon_callbacks = {}
