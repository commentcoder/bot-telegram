import os
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

load_dotenv()

token = os.getenv("TOKEN")

async def start(update, context):
  await update.message.reply_text("""Bienvenue sur le bot de Comment Coder.
Pour avoir les dernières informations, veuillez faire :
- /site pour consulter le site
- /question pour répondre à une question
- /youtube pour voir les dernières vidéos""")


async def site(update, context):
  await update.message.reply_text("Le lien du site Comment Coder est https://www.commentcoder.com")


async def question(update, context):
  keyboard = [
    [KeyboardButton("Python"), KeyboardButton("Java")],
    [KeyboardButton("JavaScript"), KeyboardButton("C et C++")],
  ]

  reply_markup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True,
    one_time_keyboard=True
  )

  await update.message.reply_text("Quel est votre langage préféré ?",
                                  reply_markup=reply_markup)


async def youtube(update, context):
  keyboard = [
    [InlineKeyboardButton('Python', 'https://www.youtube.com/watch?v=5EnpNI2iCZA')],
    [InlineKeyboardButton('Django', 'https://www.youtube.com/watch?v=xJNvJaLl8bU')],
    [InlineKeyboardButton('Bot Discord en Python', 'https://www.youtube.com/watch?v=vDmed9KcGRc')],
  ]

  reply_markup = InlineKeyboardMarkup(keyboard)

  await update.message.reply_text("Que voulez-vous apprendre aujourd'hui ?",
                                  reply_markup=reply_markup)


if __name__ == '__main__':
  app = Application.builder().token(token).build()

  app.add_handler(CommandHandler('start', start))
  app.add_handler(CommandHandler('site', site))
  app.add_handler(CommandHandler('question', question))
  app.add_handler(CommandHandler('youtube', youtube))

  app.run_polling(poll_interval=5)