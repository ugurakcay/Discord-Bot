import discord
from discord.ext import commands
import random
from owo import text_to_owo

bot = discord.Client()

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
  print("logged in as")
  print(bot.user.name)
  print(bot.user.id)
  print('------')

@bot.command()
async def sa(ctx):
  await ctx.send("as")

@bot.command()
async def soru(ctx, *, question):
  responses=["evet", "hayır", "belki"]
  await ctx.send(f"Soru: {question}\nCevap: {random.choice(responses)}")

@bot.command()
async def owo(ctx):
  await ctx.send(text_to_owo(ctx.message.content))

@bot.command(aliases=["kaçcm"])
async def cm(ctx):
  responses=["15", "16", "17", "18" ,"19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
  await ctx.send(f"{random.choice(responses)}")



bot.run("ODE0NTQyODkxMzIxNTI0MjM1.YDfYLg.mPoivCakz6mIYihtD5L49AqjJIs")
