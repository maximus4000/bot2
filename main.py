import random
import os

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("я готов")

@bot.command()
async def time_bust(ctx, material):
    """время разложения материалов"""
    if material == "пластик":
        await ctx.send(f"{material} разлогается от 6 месяцев до 700 лет")
    elif material == "стекло":
        await ctx.send(f"{material} разлогается от 1 тыс до 1 млн лет")
    elif material == "металл":
        await ctx.send(f"{material} разлогается от 10 до 100 лет")
    elif material == "батарейка":
        await ctx.send(f"{material} разлогается до 100 лет")
    elif material == "резина":
        await ctx.send(f"{material} разлогается более 100 лет")

@bot.command()
async def foto_trash(ctx):
    """фото случайной свалки"""
    files = os.listdir("images")
    rand_mem = random.choice(files)
    with open(f"images/{rand_mem}", 'rb') as file:
        picture = discord.File(file)
    await ctx.send(file=picture)

@bot.command()
async def sort_trash(ctx):
    """информация о сортировке мусора"""
    await ctx.send("Раздельный сбор мусора позволяет отделить перерабатываемые отходы от неперерабатываемых")
    await ctx.send("а также выделить отдельные типы отходов, пригодные для вторичного использования.")
    await ctx.send("отходы разделяются на:")
    await ctx.send("бумагу")
    await ctx.send("стекла")
    await ctx.send("пластик")
    await ctx.send("и пищевые отходы")

@bot.command()
async def dang_trash(ctx, material):
    """опасность мусора"""
    if material == "градусник":
        await ctx.send(f"{material} чрезвычайно опасен. Он оказывают наибольший вред окружающей среде и здоровью людей")
    elif material == "батарейка":
        await ctx.send(f"{material} отнесена ко 2-му классу опасности, приводит к серьезным нарушениям окружающей среды")
    elif material == "телефон":
        await ctx.send(f"{material} ведет к нарушению экологической системы, но  через 10 лет после изъятия окружающая среда полностью восстанавливается.")
    elif material == "пластмасса":
        await ctx.send(f"{material} приводит к нарушениям экосистемы, однако урон относительно невелик")
    elif material == "кирпич":
        await ctx.send(f"{material} безопасный для экосистемы мусор, который самостоятельно разлагается естественным путем")

bot.run("token")
