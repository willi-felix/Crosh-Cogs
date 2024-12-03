import discord
from redbot.core import commands

class Calculator(commands.Cog):
    """A cog to perform basic calculations"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calculate")
    async def calculate(self, ctx, num1: float, operation: str, num2: float):
        """
        Perform basic calculations.
        Usage: [p]calculate [number1] [operation] [number2]
        Supported operations: +, -, x/×/., ÷
        """
        try:
            if operation in ["+", "add"]:
                result = num1 + num2
            elif operation in ["-", "subtract"]:
                result = num1 - num2
            elif operation in ["x", "×", ".", "multiply"]:
                result = num1 * num2
            elif operation in ["÷", "/", "divide"]:
                if num2 == 0:
                    await ctx.send("Error: Division by zero is not allowed.")
                    return
                result = num1 / num2
            else:
                await ctx.send("Invalid operation. Supported operations: +, -, x/×/., ÷")
                return

            await ctx.send(f"The result of {num1} {operation} {num2} is: `{result}`")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
