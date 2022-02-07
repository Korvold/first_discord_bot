from discord.ext import commands
import discord


class Talks(commands.Cog):
    """ Talk with user """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi", help="Envia um Oi (Não requer argumento)")
    async def send_hello(self, ctx):
        name = ctx.author.name

        response = "Fala tu, " + name

        await ctx.send(response)

    @commands.command(name="segredo", help="Envia um segredo no privado. Não requer argumento")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Se tiver qualquer crítica ou sugestão Amanda aê")
            await ctx.author.send("Podemos crescer juntos!")
            await ctx.author.send("Ambos podemos nos aproveitar desse aprendizado!")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor(Opções > Privacidade)")


def setup(bot):
    bot.add_cog(Talks(bot))
