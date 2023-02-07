import discord
import random
from discord.ext import commands
from music_cog import music_cog
from assist_help import assist_help
from discord.ext import commands
from youtube_dl import YoutubeDL



client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is connected")

client.add_cog(assist_help(client))
client.add_cog(music_cog(client))

class music_cog(commands.Cog):
    def _init_(self,bot):
        self.bot = bot 
        self.is_playing = False #states of music bot whether they are playing  something or not
        self.is_paused = False

        self.music_queue =[]
        self.YDL_OPTIONS = {'format': 'queue'}
        self.FFMPEG_OPTIONS = {'before_options': 'reconnect'}

        self.vc = None

def search_youtube(self, item):
    with YoutubeDL(self.YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % item,  download=False)['tries'][0]
        except Exception:
            return False
        return {'source': info['formats'[0]['url']], 'title': info['title']}
         

 
def play(self): #This part plays the next music that is in the queue
    if len(self.music_queue) > 0:
        self.is_playing = True
        m_url = self.music_queue[0][0]['source']
        self.music.queue.pop(0)
        self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next() )
        
    else:
         self.is_playing = False











        






