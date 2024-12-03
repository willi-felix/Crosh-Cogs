from .calculate import Calculator

async def setup(bot):
    bot.add_cog(Calculator(bot))
