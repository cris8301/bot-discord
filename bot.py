import discord
import random
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def coin_flip(ctx):
    # Lista de la cuenta regresiva
    await ctx.send("Lanzando moneda...")
    
    for i in range(3, 0, -1):
        await ctx.send(str(i))
        await asyncio.sleep(1) # Espera 1 segundo
    
    result = random.choice(['Cara', 'Cruz'])
    await ctx.send(f'¡Salió: **{result}**!')

@bot.command()
async def _help(ctx):
    await ctx.send('Comandos disponibles:\n$_help - Muestra este mensaje\n$hello - Saluda al bot\n$heh [count_heh] - Repite "he" un número de veces (por defecto 5)\n$coin_flip - Lanza una moneda')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


bot.run("tu_token_aqui")