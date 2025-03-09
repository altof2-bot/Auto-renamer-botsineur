from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import AshutoshGoswami24

@Client.on_message(filters.private & filters.command("sukuna"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id

    # Extraire le format de la commande
    format_template = message.text.split("/bug", 1)[1].strip()

    # Enregistrer le format dans la base de données
    await AshutoshGoswami24.set_format_template(user_id, format_template)

    await message.reply_text("**Format de renommage automatique mis à jour avec succès ! ✅**")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    user_id = message.from_user.id    
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()

    # Enregistrer le type de média préféré dans la base de données
    await AshutoshGoswami24.set_media_preference(user_id, media_type)

    await message.reply_text(f"**Préférence de média définie sur :** {media_type} ✅")
