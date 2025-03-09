# -*- coding: utf-8 -*-
import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "24777493")
    API_HASH  = os.environ.get("API_HASH", "bf5a6381d07f045af4faeb46d7de36e5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7683456107:AAH3y7X7fe6XtTjfYlv5v27wIGgsgcGHL70") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","altof2")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://altof2:123Bonjoure@cluster0.s1suq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/7c1856ae9ba0a15065ade-abf2c0b5a93356da7b.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5116530698').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'sineur_x_bot,sineur_x_bot').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002203058630"))
    PORT = int(os.environ.get("PORT", "8080"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Salut {} 
    
Je suis BUG maître des fléaux et ||Elèves Du grand maître SINEUR.|| Je suis un bot de renommage de fichiers qui fait partie des plus puissant

Envoyer moi votre Fichier et j'utiliserai l'extension du territoire ||Temple des fichiers|| pour la renommer à la perfection.
    
    FILE_NAME_TXT = """<b><u>VOICI LE MENU AUTO-RENOMAGE</u></b>

Utilisez ces mots-clés pour configurer un nom de fichier personnalisé

 `[episode]` :- Pour remplacer le numéro épisode.
 `[quality]` :- Pour remplacé la résolution de la qualité

<b> Exemple :</b> <code> /sukuna ou /bug Naruto Shippuden S01[episode] [quality][Dual Audio] @BotZFlix</code> 

<b> Votre format autorename actuel :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 Mon Nom :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Librarie :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Serveur :</b> <a href='https://t.me/REQUETE_ANIME_30sbot'>clood</a>
<b>🧑‍💻 Developeur :</b> <a href='https://t.me/altof2'>ZFlixTeam</a>
    
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
╭━━━━❰BUG BOT❱━➣
┣⪼ 🗃️ Poids: {1} | {2}
┣⪼ ⏳️ FAIT : {0}%
┣⪼ 🚀 VITESSE: {3}/s
┣⪼ ⏰️ ETA: {4}
┣⪼ 🥺 Rejoins ici : @sineur_x_bot
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>❤ Dσɳɑtiσɳ 

🎗Nous ɑvons besoin de votre ɑide ɑujourd’hui pour continuer ɑ̀ vous fournir des contenus de quɑlités ɑ̀ trɑvers nos plɑteformes et bots.

« Seriez-vous prêt ɑ̀ ɑider en fɑisɑnt un don  ? Chɑque centime ɑiderɑ. »

« Fɑire un don ❤ est une fɑçon de tendre une mɑin secourɑble. 

En fɑisɑnt même un petit don💞, vous pouvez pɑrticiper ɑ̀ un effort visɑnt ɑ̀  mɑintenir les bots ZFlix et ce bot en vie.

🤲 Merci de Contribuer ɑ̀ l'hébergement et ɑux frɑis d'ɑbonnement indispensɑbles pour lɑ survie de notre communɑuté. » """
    
    HELP_TXT = """<b>Hey</b> {}
    
écrit nous sur @REQUETE_ANIME_30sbot pour tout aide 24/24 """





