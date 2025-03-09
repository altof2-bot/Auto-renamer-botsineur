import random
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ForceReply,
    CallbackQuery,
    Message,
    InputMediaPhoto,
)

from helper.database import AshutoshGoswami24
from config import Config, Txt


@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await AshutoshGoswami24.add_user(client, message)
    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📢 Mises à jour", url="https://t.me/sineur_x_bot"),
                InlineKeyboardButton("💬 Support", url="https://t.me/REQUETE_ANIME_30sbot"),
            ],
            [
                InlineKeyboardButton("⚙️ Aide", callback_data="help"),
                InlineKeyboardButton("💙 À propos", callback_data="about"),
            ],
            [
                InlineKeyboardButton(
                    "🧑‍💻 Développeur 🧑‍💻", url="https://t.me/altof2"
                )
            ],
        ]
    )
    if Config.START_PIC:
        await message.reply_photo(
            Config.START_PIC,
            caption=Txt.START_TXT.format(user.mention),
            reply_markup=button,
        )
    else:
        await message.reply_text(
            text=Txt.START_TXT.format(user.mention),
            reply_markup=button,
            disable_web_page_preview=True,
        )


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id

    if data == "home":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📢 Mises à jour", url="https://t.me/sineur_x_bot"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/REQUETE_ANIME_30sbot"),
                    ],
                    [
                        InlineKeyboardButton("⚙️ Aide", callback_data="help"),
                        InlineKeyboardButton("💙 À propos", callback_data="about"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🧑‍💻 Développeur 🧑‍💻", url="https://t.me/altof2"
                        )
                    ],
                ]
            ),
        )
    elif data == "caption":
        await query.message.edit_text(
            text=Txt.CAPTION_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✖️ Fermer", callback_data="close"),
                        InlineKeyboardButton("🔙 Retour", callback_data="help"),
                    ]
                ]
            ),
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "⚙️ Configurer le format AutoRename ⚙️", callback_data="file_names"
                        )
                    ],
                    [
                        InlineKeyboardButton("🖼️ Miniature", callback_data="thumbnail"),
                        InlineKeyboardButton("✏️ Légende", callback_data="caption"),
                    ],
                    [
                        InlineKeyboardButton("🏠 Accueil", callback_data="home"),
                        InlineKeyboardButton("💰 Faire un don", callback_data="donate"),
                    ],
                ]
            ),
        )
    elif data == "donate":
        await query.message.edit_text(
            text=Txt.DONATE_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✖️ Fermer", callback_data="close"),
                        InlineKeyboardButton("🔙 Retour", callback_data="help"),
                    ]
                ]
            ),
        )

    elif data == "file_names":
        format_template = await AshutoshGoswami24.get_format_template(user_id)
        await query.message.edit_text(
            text=Txt.FILE_NAME_TXT.format(format_template=format_template),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✖️ Fermer", callback_data="close"),
                        InlineKeyboardButton("🔙 Retour", callback_data="help"),
                    ]
                ]
            ),
        )

    elif data == "thumbnail":
        await query.message.edit_caption(
            caption=Txt.THUMBNAIL_TXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✖️ Fermer", callback_data="close"),
                        InlineKeyboardButton("🔙 Retour", callback_data="help"),
                    ]
                ]
            ),
        )

    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✖️ Fermer", callback_data="close"),
                        InlineKeyboardButton("🔙 Retour", callback_data="home"),
                    ]
                ]
            ),
        )

    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
