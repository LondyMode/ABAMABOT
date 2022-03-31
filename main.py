import discord
from discord.ext import commands
from config import settings
bot = commands.Bot(command_prefix = settings['prefix']) 
@bot.command() 
async def помощь(ctx): 
    author = ctx.message.author 
    await ctx.send(f'{author.mention}\n $привет - кто я?\n $еда - я голоден!')
@bot.command() 
async def привет(ctx): 
    author = ctx.message.author 
    await ctx.send(f'Привет {author.mention}! Меня зовут ОБАМА, я чёрный!')
@bot.command() 
async def еда(ctx): 
    author = ctx.message.author 
    await ctx.send(f'{author.mention}, снюс есть?!') 
@bot.event    
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("ЧЁРНАЯ ИГРА $помощь"))
bot.run(settings['token'])    