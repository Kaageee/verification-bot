import discord
from discord.ext import commands
import settings
import dontedit

#####################################################################################   
##      $$\   $$\                                                                  ##
##      $$ | $$  |                                                                 ##
##      $$ |$$  / $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\        ##
##      $$$$$  /  \____$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       ##
##      $$  $$<   $$$$$$$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$$$$$$$ |$$$$$$$$ |      ##
##      $$ |\$$\ $$  __$$ |$$  __$$ |$$ |  $$ |$$   ____|$$   ____|$$   ____|      ##
##      $$ | \$$\\$$$$$$$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ \$$$$$$$\ \$$$$$$$\       ##
##      \__|  \__|\_______| \_______| \____$$ | \_______| \_______| \_______|      ##
##                                   $$\   $$ |                                    ##
##                                   \$$$$$$  |                                    ##
##                                    \______/                                     ##
#####################################################################################

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(dontedit.sn)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))

@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == int(settings.MessageId):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if payload.emoji.name == settings.Reaction:
            user = payload.member
            role = discord.utils.get(user.guild.roles, name=settings.rolename)
            await user.add_roles(role)


bot.run(settings.TOKEN)
