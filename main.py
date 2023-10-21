import discord
from discord.ext import commands
from model import get_class
from bot_logic import bot_l
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def q(ctx):
    attachments = ctx.message.attachments
    if ctx.message.attachments:
        for attachment in attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'img/{file_name}')
            await ctx.send("картинка сохранена")
            a = get_class(f'img/{file_name}')
            await ctx.send(bot_l(a))
    else:
        await ctx.send('Картинка не была найдена')
bot.run("TOKEN")