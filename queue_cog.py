import discord
import os
import random
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
load_dotenv()

class MainQ(commands.Cog, name="Queue Commands"):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        print(len(self.queue))

    @commands.command(name="queue", aliases=['Q', 'q', 'Queue'])
    async def joinQ(self, ctx):

        gamer = ctx.author

        if gamer in self.queue:
            await ctx.send('You have already queued')
            return

        self.queue.append(gamer)
        print(len(self.queue))

        if len(self.queue) < 10:
            if len(self.queue) == 1:
                embed = discord.Embed(title=f'{len(self.queue)} player has joined the queue!')
            else:
                embed = discord.Embed(title=f'{len(self.queue)} players are in the queue!')
            embed.color = 0x00e1ff
            embed.description = f'{gamer.mention} has joined.'
            embed.set_footer(text=f'{str(10-len(self.queue))} more spaces left.', icon_url=f'https://cdn.discordapp.com/attachments/202119075739074560/801989478930841600/cs10.png')
            await ctx.send(embed=embed)

        elif len(self.queue) == 10:


            embed = discord.Embed(title=f'{len(self.queue)} players are now in the queue!!!')
            embed.color = 0x00e1ff
            embed.description = f'{gamer.mention} has joined.'
            embed.set_footer(text=f'{str(10-len(self.queue))} spaces left.', icon_url=f'https://cdn.discordapp.com/attachments/202119075739074560/801989478930841600/cs10.png')
            await ctx.send(embed=embed)

            embed = discord.Embed(title=f'There is now 10 people ready to play!')
            embed.set_footer(text=f'Get ready to tilt :)', icon_url=f'https://cdn.discordapp.com/attachments/202119075739074560/801989478930841600/cs10.png')
            embed.color = 0x00e1ff
            await ctx.send(embed=embed)

            lobby = discord.Embed(title="Click here to join your match room.", url="https://popflash.site/scrim/"+str(random.randint(1000, 1000000)), color=0x00e1ff)
            lobby.set_author(name="RLI 10 mans.")
            lobby.set_thumbnail(url="https://cdn.discordapp.com/attachments/202119075739074560/801989478930841600/cs10.png")
            lobby.add_field(name="Info", value="Your queue has popped!", inline=False)
            for gamer in self.queue:
                await gamer.send(embed=lobby)
            self.queue.clear()
            return

    @commands.command(name="leave", aliases=['L', 'l', 'Leave'])
    async def leave(self, ctx):

        gamer = ctx.author
        
        if gamer not in self.queue:
            await ctx.send('You are not in the queue to leave it :/')
            return

        self.queue.remove(gamer)
        print(len(self.queue))

        leave = discord.Embed(title=f'{len(self.queue)} players are in the the queue.')
        leave.description = f'{gamer.mention} has left the queue.'
        leave.color = 0x00e1ff
        leave.set_footer(text=f'{str(10-len(self.queue))} are needed.', icon_url=f'https://cdn.discordapp.com/attachments/202119075739074560/801989478930841600/cs10.png')
        await ctx.send(embed=leave)

        if len(self.queue) == 0:
            Qempty = discord.Embed(title=f'The queue is now empty.')
            Qempty.description = f':('
            Qempty.color = 0x00e1ff
            Qempty.set_footer(text=f'No craic..', icon_url=f'https://cdn.discordapp.com/attachments/202119075739074560/801989478930841600/cs10.png')
            await ctx.send(embed=Qempty)


    @commands.command(name='players', aliases=['lp'])
    async def players(self, ctx):

        if len(self.queue) == 1:
            playersls1 = discord.Embed(title=f'{len(self.queue)} player is in the queue.')
            playersls1.description = (" ".join(gamer.mention for gamer in self.queue))
            playersls1.color = 0x00e1ff
            playersls1.set_footer(text=f'{str(10-len(self.queue))} players are needed!', icon_url=f'https://cdn.discordapp.com/attachments/202119075739074560/801989478930841600/cs10.png')
            await ctx.send(embed=playersls1)

        else:
            playersls = discord.Embed(title=f'{len(self.queue)} players are in the queue.')
            playersls.description = (" ".join(gamer.mention for gamer in self.queue))
            playersls.color = 0x00e1ff
            playersls.set_footer(text=f'{str(10-len(self.queue))} more needed!', icon_url=f'https://cdn.discordapp.com/attachments/202119075739074560/801989478930841600/cs10.png')
            await ctx.send(embed=playersls)

    @commands.command(name='clear_q', description='Forcefully emptys the queue')
    async def clear_queue(self, ctx):
        self.queue.clear()
        await ctx.send('The queue has been cleared.')
        

def setup(bot):
    bot.add_cog(MainQ(bot))
    bot.remove_command("help")
