import asyncio
import requests
from flask import Flask,request
import threading
import os
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton,Bot
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters, CallbackContext

TOKEN = "7610262736:AAHYgaBJxJJuoyDcPDzikhSODiPlg0Hs2yI"
WEBHOOK_URL = "https://dicebotf-oo87.onrender.com"

# ID de l'administrateur (ton ID Telegram)
ADMIN_ID = 6111033488 # Ton vrai ID Telegram

# Liste pour stocker les utilisateurs inscrits
users = set()

# Initialisation du bot
app_telegram = Application.builder().token(TOKEN).build()
bot = Bot(token=TOKEN)


# Création du serveur Flask
app = Flask(__name__)

# async def setup_webhook():
#     await bot.delete_webhook()
#     await bot.set_webhook(f"{WEBHOOK_URL}/{TOKEN}")

@app.route("/", methods=["GET"])
def home():
    return "Le bot est en ligne"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    print("Réception d'un message :", update)  # Debug
    return "OK", 200  # Réponse correcte

# Charger les données utilisateurs
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Fonction de démarrage
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    users.add(user_id)  # Ajouter l'utilisateur à la liste des utilisateurs

    keyboard = [
        ["S'INSCRIRE"],
        ["Menu"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    inscription_button = InlineKeyboardMarkup([
        [InlineKeyboardButton("S'INSCRIRE", url="https://1wqvhy.com/?p=zql1")]
    ])

    await update.message.reply_text(
        "𝘽𝙞𝙚𝙣𝙫𝙚𝙣𝙪𝙚 𝙙𝙖𝙣𝙨 𝙡𝙚 𝙗𝙤𝙩 𝙙𝙚 𝙥𝙧𝙚‌𝙙𝙞𝙘𝙩𝙞𝙤𝙣 𝙙𝙪 𝙟𝙚𝙪 𝘿𝙞𝙘𝙚 !\n\n"
        "𝘈𝘷𝘢𝘯𝘵 𝘥𝘦 𝘫𝘰𝘶𝘦𝘳 𝘢𝘷𝘦𝘤 𝘴𝘦𝘴 𝘱𝘳𝘦‌𝘥𝘪𝘤𝘵𝘪𝘰𝘯 𝘢𝘴𝘴𝘶𝘳𝘦‌𝘦 𝘷𝘰𝘶𝘴 𝘥'𝘦‌𝘵𝘳𝘦 𝘪𝘯𝘴𝘤𝘳𝘪𝘳𝘦 𝘴𝘶𝘳 𝟣𝘸𝘪𝘯 𝘢𝘷𝘦𝘤 𝘭𝘦 𝘤𝘰𝘥𝘦 𝘱𝘳𝘰𝘮𝘰 𝘿𝙄𝘾𝙀𝙒 𝘰𝘶‌ 𝘾𝘼𝙎𝙃𝙁 !\n\n"
        "👇 Cliquez sur le bouton ci-dessous pour vous inscrire 👇",
        reply_markup=inscription_button
    )

    await update.message.reply_text("Choisissez une option :", reply_markup=reply_markup)

# Fonction pour afficher le menu principal
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["S'INSCRIRE"],
        ["Menu"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bienvenue dans le menu principal !", reply_markup=reply_markup)

# Fonction pour afficher le sous-menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["𝙁𝘼𝙄𝙍𝙀 𝙐𝙉𝙀 𝙋𝙍𝙀‌𝘿𝙄𝘾𝙏𝙄𝙊𝙉 🎲"],
        ["𝘾𝙊𝙈𝙈𝙀𝙉𝙏 𝘾̧𝘼 𝙈𝘼𝙍𝘾𝙃𝙀 ❗️❓"],
        ["𝙍𝙀𝙏𝙊𝙐𝙍 🔙"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Choisissez une option :", reply_markup=reply_markup)

# Fonction pour retourner au menu principal
async def back_to_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await main_menu(update, context)

# Fonction pour afficher "Comment ça marche"
async def how_it_works(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "𝐂𝐨𝐦𝐦𝐞𝐧𝐭 𝐮𝐭𝐢𝐥𝐢𝐬𝐞𝐫 𝐬𝐞 𝐛𝐨𝐭 👨‍💻:\n\n"
        "- 𝙸𝚗𝚜𝚌𝚛𝚒𝚟𝚎𝚣-𝚟𝚘𝚞𝚜 𝚜𝚞𝚛 𝟷𝚠𝚒𝚗 𝚊𝚟𝚎𝚌 𝚕𝚎 𝚌𝚘𝚍𝚎 𝚙𝚛𝚘𝚖𝚘 𝘿𝙄𝘾𝙀𝙒.\n\n"
        "-𝙵𝚊𝚒𝚛𝚎 𝚞𝚗 𝚍𝚎́𝚙𝚘̂𝚝 𝚖𝚒𝚗𝚒𝚖𝚞𝚖 𝚍𝚎  𝟸𝟶𝟶𝟶 𝙵𝙲𝙵𝙰 𝚙𝚘𝚞𝚛 𝚊𝚌𝚝𝚒𝚟𝚎́  𝚕𝚊 𝚏𝚊𝚒𝚕𝚕𝚎 𝚎𝚝 𝚛𝚎𝚌𝚎𝚟𝚘𝚒𝚛 𝟻𝟶𝟶% 𝚍𝚎 𝚋𝚘𝚗us 𝚜𝚞𝚛 𝚕𝚎𝚜 𝟺 𝚙𝚛𝚎𝚖𝚒𝚎𝚛𝚜 𝚍𝚎́𝚙𝚘̂𝚝\n\n"
        "-𝚁𝚎𝚌𝚑𝚎𝚛𝚌𝚑𝚎𝚛 𝚕𝚎 𝚓𝚎𝚞 𝗗𝗶𝗰𝗲 𝚜𝚞𝚛 𝟷𝚠𝚒𝚗.\n\n"
        "- 𝙲𝚕𝚒𝚚𝚞𝚎𝚣 𝚜𝚞𝚛 𝙁𝘼𝙄𝙍𝙀 𝙐𝙉𝙀 𝙋𝙍𝙀‌𝘿𝙄𝘾𝙏𝙄𝙊𝙉 🎲𝚙𝚘𝚞𝚛 𝚊𝚟𝚘𝚒𝚛 𝚞𝚗 𝚙𝚛𝚎́𝚍𝚒𝚌𝚝𝚒𝚘𝚗 𝚊 𝚓𝚘𝚞𝚎𝚛."
    )
    keyboard = [["𝙍𝙀𝙏𝙊𝙐𝙍 🔙"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(text, reply_markup=reply_markup)

# Fonction pour faire une prédiction avec précision ajustée
import random
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = random.choices(["supérieure à 50", "inférieure à 50"], weights=[52, 48])[0]
    await update.message.reply_text(f"La prédiction est : {choice}")

# Fonction pour envoyer un message à tous les utilisateurs (commande réservée à toi)
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != ADMIN_ID:
        await update.message.reply_text("⛔️ Vous n'avez pas l'autorisation d'utiliser cette commande.")
        return

    if not context.args:
        await update.message.reply_text("Utilisation : /broadcast [message]")
        return

    message = " ".join(context.args)
    
    for user_id in users:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
        except:
            pass  # Ignorer les erreurs si un utilisateur a bloqué le bot

    await update.message.reply_text("✅ Message envoyé à tous les utilisateurs !")

# Fonction pour envoyer les ID de tous les utilisateurs
async def list_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != ADMIN_ID:
        await update.message.reply_text("⛔️ Vous n'avez pas l'autorisation d'utiliser cette commande.")
        return

    user_ids = "\n".join(str(user) for user in users)
    await update.message.reply_text(f"Liste des utilisateurs :\n{user_ids}")

# Commande pour envoyer des annonces multimédias
async def envoyer_annonce(update: Update, context: CallbackContext):
    if update.message.from_user.id != 6111033488:  # Remplacez par votre ID admin
        await update.message.reply_text("❌ Vous n'avez pas la permission d'utiliser cette commande.")
        return

    if update.message.photo:
        media_id = update.message.photo[-1].file_id
        caption = update.message.caption
        for user_id in load_data().keys():
            try:
                await context.bot.send_photo(chat_id=user_id, photo=media_id, caption=caption)
            except Exception as e:
                print(f"Erreur lors de l'envoi à {user_id} : {e}")

    elif update.message.video:
        media_id = update.message.video.file_id
        caption = update.message.caption
        for user_id in load_data().keys():
            try:
                await context.bot.send_video(chat_id=user_id, video=media_id, caption=caption)
            except Exception as e:
                print(f"Erreur lors de l'envoi à {user_id} : {e}")

    await update.message.reply_text("📢 Annonce envoyée à tous les utilisateurs.")


# Initialisation du bot
def main():
    print("Le bot est en cours d'exécution...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))  # Commande réservée à toi
    app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, envoyer_annonce))
    app.add_handler(CommandHandler("list_users", list_users))  # Commande pour lister les IDs des utilisateurs
    app.add_handler(MessageHandler(filters.Text("Menu"), menu))
    app.add_handler(MessageHandler(filters.Text("S'INSCRIRE"), start))
    app.add_handler(MessageHandler(filters.Text("𝙁𝘼𝙄𝙍𝙀 𝙐𝙉𝙀 𝙋𝙍𝙀‌𝘿𝙄𝘾𝙏𝙄𝙊𝙉 🎲"), predict))
    app.add_handler(MessageHandler(filters.Text("𝘾𝙊𝙈𝙈𝙀𝙉𝙏 𝘾̧𝘼 𝙈𝘼𝙍𝘾𝙃𝙀 ❗️❓"), how_it_works))
    app.add_handler(MessageHandler(filters.Text("𝙍𝙀𝙏𝙊𝙐𝙍 🔙"), back_to_main_menu))

# Configuration du webhook au lancement
def set_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}/{TOKEN}"
    response = requests.get(url)
    print(response.json())

if __name__ == "__main__":
    set_webhook()  # Active le webhook
    app.run(host="0.0.0.0", port=8080)
# Exécuter l'initialisation du webhook
asyncio.run(setup_webhook())

# @app.route("/", methods=["GET"])
# def home():
#     return "Bot actif ! 🚀"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)


# if __name__ == "__main__":
#     # Supprimer les anciens Webhooks
#     bot.delete_webhook()
    
#     # Définir un nouveau Webhook
#     bot.set_webhook(f"{WEBHOOK_URL}/{TOKEN}")

#     # Lancer Flask
#     app.run(host='0.0.0.0', port=8080)

#     # app.run_polling()
