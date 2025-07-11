import discord
from discord.ext import commands
from main import dato_random
#from main import Localizame
import pyttsx3

engine = pyttsx3.init()

#engine.setProperty("rate", 100)
engine.setProperty("volume", 1)

voices = engine.getProperty("voices")

#for index, voice in enumerate(voices):
#    print(f"Voz {index}: {voice.name}: {voice.languages}")

engine.setProperty("voice", voices[0].id)


def bot():
        from discord.ext import commands

        intents = discord.Intents.default()
        intents.message_content = True

        bot = commands.Bot(command_prefix='$', intents=intents)

        @bot.command('Dato_Random')
        async def DR(ctx):
                DR = dato_random

                await ctx.send(f'El dato random es {DR}')


#    @bot.command('Localizame')
#    async def localizame(ctx, *, IP):
#            ipadress = IP
#            CN = Localizame()

#            await ctx.send(f'tu ip esta localizada en {CN}', 
#                            engine.say(CN),
#                            engine.runAndWait(),
#                            engine.stop(),
#                            )

        bot.run("Enter Your Token")

bot()