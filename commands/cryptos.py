from discord.ext import commands
import requests


class Crypto(commands.Cog):
    """ Work with Cryptocurrency """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Verifica o preço de um par na Binance. Argumentos: moeda,base")
    async def binance(self, ctx, coin, base):
        try:
            response = requests.get(
                f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}"
            )

            data = response.json()
            price = data.get("price")

            if price:
                await ctx.send(f"Valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"O par {coin}/{base} é inválido")
        except Exception as error:
            await ctx.send("Ops..... Deu algum erro!")
            print(error)


def setup(bot):
    bot.add_cog(Crypto(bot))
