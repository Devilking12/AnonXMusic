from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.6791925138),
            InlineKeyboardButton(text=_["S_B_2"], url=config.https://t.me/Devil_support_network),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.https://t.me/feelings_for_you_baby),
            InlineKeyboardButton(text=_["S_B_7"], url=config.https://graph.org/file/029bf1df4f93265764cf2.mp4),
        ],
    ]
    return buttons
