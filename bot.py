import discord
import random
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

BASE = os.path.dirname(os.path.abspath(__file__))

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def coin_flip(ctx):
    await ctx.send("Lanzando moneda...")
    
    for i in range(3, 0, -1):
        await ctx.send(str(i))
        await asyncio.sleep(1)
    
    result = random.choice(["Cara", "Cruz"])
    await ctx.send(f"¡Salió: **{result}**!")

@bot.command()
async def imagen(ctx, nombre: str = None):
    carpeta = os.path.join(BASE, "imagenes")

    if nombre is None:
        archivos = [os.path.splitext(f)[0] for f in os.listdir(carpeta) if f.endswith((".png", ".jpg"))]
        lista = "\n".join(archivos)
        embed = discord.Embed(title="🖼️ Imágenes disponibles", description=lista, color=discord.Color.blue())
        embed.set_footer(text="Uso: $imagen <nombre>")
        await ctx.send(embed=embed)
        return

    ruta = None
    ext_encontrada = None
    for ext in (".jpg", ".png"):
        posible = os.path.join(BASE, "imagenes", f"{nombre}{ext}")
        if os.path.exists(posible):
            ruta = posible
            ext_encontrada = ext
            break

    if ruta is None:
        await ctx.send(f"❌ No encontré **{nombre}**. Usa `$imagen` para ver las disponibles.")
        return

    file = discord.File(ruta, filename=f"{nombre}{ext_encontrada}")
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_image(url=f"attachment://{nombre}{ext_encontrada}")
    await ctx.send(file=file, embed=embed)

@bot.command()
async def _help(ctx):
    await ctx.send('Comandos disponibles:\n$_help - Muestra este mensaje\n$hello - Saluda al bot\n$heh [count_heh] - Repite "he" un número de veces (por defecto 5)\n$coin_flip - Lanza una moneda')


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user}!")

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)


bot.run("tu_token_aqui")