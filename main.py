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
    await ctx.send("фото слуцайной свалки")

@bot.command()
async def sort_trash(ctx):
    await ctx.send("Информация о сортировке мусора")

@bot.command()
async def dang_trash(ctx, material):
    await ctx.send(f"опастности от {material}")

bot.run("MTE1NTQ0MzI4ODA5NTA4MDQ3OA.GIaCys.mveuO554YmPx6gVOtOu9JEKmUXW81e9qcdYqTk")
