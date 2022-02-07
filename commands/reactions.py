from discord.ext import commands


class Reactions(commands.Cog):
    """ Work with Reactions """

    def __init__(self, bot):
        self.bot = bot

    # events ==>commands.Cog.listener
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "🚀":
            role = user.guild.get_role(939576379039711303)
            await user.add_roles(role)
        elif reaction.emoji == "💩":
            role = user.guild.get_role(939576489798684712)
            await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
