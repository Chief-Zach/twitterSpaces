from decouple import config
import interactions
import main

bot = interactions.Client(token=config("DISCORD"))


@bot.command(
    name="tweet",
    description="Get Twitter post from website summary ",
    options=[
        interactions.Option(
            name="website",
            description="What website would you like to scrape",
            type=interactions.OptionType.STRING,
            required=True, )
    ],
)
async def embed(ctx: interactions.CommandContext, website: str):
    await ctx.defer()
    response = main.scrape(website)
    await ctx.send(response)


@bot.command(
    name="summarizer",
    description="Summarize a website!",
    options=[
        interactions.Option(
            name="website",
            description="What website would you like to scrape",
            type=interactions.OptionType.STRING,
            required=True, )
    ],
)
async def embed(ctx: interactions.CommandContext, website: str):
    await ctx.defer()
    response = main.scrapeSum(website)
    await ctx.send(response)


@bot.command(
    name="wiki",
    description="Summarize a Wikipedia page!",
    options=[
        interactions.Option(
            name="wikipedia",
            description="What Wikipedia would you like to scrape?",
            type=interactions.OptionType.STRING,
            required=True, )
    ],
)
async def embed(ctx: interactions.CommandContext, wikipedia: str):
    await ctx.defer()
    response = main.wikipedia(wikipedia)
    await ctx.send(response)


bot.start()
