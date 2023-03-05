from discord.ext import commands
import discord, os, json, hashlib, platform
config = json.load(open("config.json", encoding="utf-8"))


def clear(): #clears the terminal
    os.system('cls' if os.name =='nt' else 'clear')
    

if platform.system() == 'Windows':
    os.system('cls & title .gg/boostd here')  
elif platform.system() == 'Linux':
    os.system('clear') 
    sys.stdout.write("\x1b]0;.gg/boostd'\x07")  
elif platform.system() == 'boostd':
    os.system("clear && printf '\e[3J'")  
    os.system('''echo "\033]0;.gg/boostd here\007"''')  

    
activity = discord.Activity(type=discord.ActivityType.watching, name=config["bot_status"])
bot = commands.Bot(command_prefix = "$", intents = discord.Intents.all(), activity = activity)
    
@bot.event
async def on_ready():
    sprint(f"{bot.user} is online!", True)

@bot.slash_command(guild_ids=[config["guildID"]], name="create", description="Creating Image Logger to log some skids.")
async def ping(ctx):
    await ctx.respond(embed = discord.Embed(title = "boostdBuilder | Finished Compiling",description = "```https://uploads.getpop.org/wp-content/uploads/2016/12/click.png```", color = 0x212121,)),


    
clear()

bot.run(config['bot_token'])


#ALL MADE BY BOOSTD#0001
# DONT USE THAT FOR SCAM KIDS BITCHES