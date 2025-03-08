import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "24817837")
    API_HASH  = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7963364338:AAHF93s-DU2ELTYtfduusIyFZMm7K9gGGfM") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","BotZFlix")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://tgbot:4KzEdxEl4YldwwFR@tg.vr8ef.mongodb.net/?retryWrites=true&w=majority&appName=Tg")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/0lA.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7428552084').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'BotZFlix,Aniflix_official').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002376378205"))
    PORT = int(os.environ.get("PORT", "8080"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Salut {} 
    
Je suis SUKUNA maître des fléaux et ||Elèves Du grand maître KINGCEY.|| Je suis un bot de renommage de fichiers qui fait partie des plus puissant

Envoyer moi votre Fichier et j'utiliserai l'extension du territoire ||Temple des fichiers|| pour la renommer à la perfection.
    
    FILE_NAME_TXT = """<b><u>VOICI LE MENU AUTO-RENOMAGE</u></b>

Utilisez ces mots-clés pour configurer un nom de fichier personnalisé

 `[episode]` :- Pour remplacer le numéro épisode.
 `[quality]` :- Pour remplacé la résolution de la qualité

<b> Exemple :</b> <code> /sukuna Naruto Shippuden S01[episode] [quality][Dual Audio] @BotZFlix</code>

<b> Votre format autorename actuel :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 Mon Nom :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Librarie :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Serveur :</b> <a href='https://heroku.com'>Heroku</a>
<b>🧑‍💻 Developeur :</b> <a href='https://t.me/Kingcey'>ZFlixTeam</a>
    
<b>♻️ Ryōiki Tenkai: Akuryō no Shinden :</b>"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  COMMENT AJOUTER UNE VIGNETTE</u></b>
    
⦿Vous pouvez ajouter une miniature personnalisée simplement en envoyant une photo.....
    
⦿ /viewthumb - Utilise cette commande pour voir ta vignette
⦿ /delthumb - Utilise cette commande pour supprimé ta vignette"""

    CAPTION_TXT = """<b><u>📝  COMMENT DEFINIR UNE LEGENDE ?</u></b>
    
⦿ /set_caption - Utilise cette commande pour définir une légende
⦿ /see_caption - Utilise cette commande pour voir ta légende
⦿ /del_caption - Utilise cette commande pour supprimé ta légende"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰SUKUNA BOT❱━➣
┣⪼ 🗃️ Poids: {1} | {2}
┣⪼ ⏳️ FAIT : {0}%
┣⪼ 🚀 VITESSE: {3}/s
┣⪼ ⏰️ ETA: {4}
┣⪼ 🥺 Rejoins ici : @ZFlixTeam
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>❤️‍🩹 Dσɳɑtiσɳ 💝

🎗Nous ɑvons besoin de votre ɑide ɑujourd’hui pour continuer ɑ̀ vous fournir des contenus de quɑlités ɑ̀ trɑvers nos plɑteformes et bots.🎗

« Seriez-vous prêt ɑ̀ ɑider en fɑisɑnt un don 💝 ? Chɑque centime ɑiderɑ. »

« Fɑire un don ❤️‍🩹 est une fɑçon de tendre une mɑin secourɑble. 

En fɑisɑnt même un petit don💞, vous pouvez pɑrticiper ɑ̀ un effort visɑnt ɑ̀  mɑintenir les bots ZFlix et ce bot en vie.

🤲 Merci de Contribuer ɑ̀ l'hébergement et ɑux frɑis d'ɑbonnement indispensɑbles pour lɑ survie de notre communɑuté🥹. » """
    
    HELP_TXT = """<b>Hey</b> {}
    
écrit nous sur @BotZFlixSupport pour tout aide 24/24 """





