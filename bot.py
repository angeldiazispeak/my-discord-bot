import os
from dotenv import load_dotenv

load_dotenv()
# ... your existing bot code ...

bot.run(os.getenv('DISCORD_TOKEN'))

import discord
from discord.ext import commands
import random
import asyncio

# Setup bot intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read channel messages

bot = commands.Bot(command_prefix="!", intents=intents)

# --- Databases ---
DAD_JOKES = [
    "Why did the old Macromedia Flash animation go to therapy? It had too many frames of mind.",
    "What is an astronaut's favorite keyboard shortcut? The Space bar.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "What did Freddie Mercury say when he bought a broken guitar? I want to break free! [Insert awkward wheezing laugh]",
    "Why can't you trust an atom? Because they make up everything. No, seriously, they do. Mr. Fox said it!!"
]

NERD_OUT_TOPICS = {
    "queen": [
        "Did you know Brian May built his guitar, the 'Red Special', out of an old fireplace mantel from the 18th century? No? Well, I didn't..",
        "The isolated vocal stems of 'Bohemian Rhapsody' are absolute art. Roy Thomas Baker bounced those tapes so many times the tape became transparent!",
        "Freddie's vocal range technically spanned almost four full octaves, and his fast vocal fold vibrato was unmatched. Though, he did get nodules later in his life."
    ],
    "flash": [
        "Macromedia Flash 8 is a PEAK animation software! The ActionScript 2.0 system might be old, but onion skinning, shape tweens, and drawing on twos at 24.0 fps just feels right to me.",
        "Nothing beats importing vector elements from Inkscape right onto a classic 4:3 canvas in Flash 8. Though Inkscape is a pain in the ass sometimes.",
        "The blend modes and filter options introduced in Flash 8 completely changed the game for web animation compared to Flash MX. Wait, who even uses Flash MX?"
    ],
    "htf": [
        "Did you know Warren Graff broke the sound equipment when recording Handy's choking sounds in the classic season 2 episode, 'Shard at Work'?",
        "Cuddles has over 55+ deaths!",
        "It's wild that the TV series reached its 20th anniversary, and we're still getting real internet episodes like 'Swole Mates'!"
    ]
}

QUEEN_QUIZ = [
    {"q": "When was Queen's iconic Live Aid performance?", "a": "OOH!! I KNOW!! JULY 13, 1985!! AND YET AUBREY CALLS ME A NERD FOR IT!"},
    {"q": "Which Queen member wrote the song 'Another One Bites the Dust'?", "a": "John Deacon!!<3"},
    {"q": "What album features 'Good Old-Fashioned Lover Boy'?", "a": "A Day at the Races...Yummy..."},
    {"q": "What was Freddie Mercury's birth name?", "a": "Farrokh Bulsara!"}
]

CHAT_PROMPTS = [
    "Hey! What project are you guys working on right now? Animating anything cool?",
    "Hey darling, what song are you listening to today?",
    "I'm so sleepy"
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("------")

# --- Command: Dad Jokes ---
@bot.command(name="joke")
async def dad_joke(ctx):
    """Tells a terribly unfunny dad joke."""
    await ctx.send(random.choice(DAD_JOKES))

# --- Command: Nerd Out ---
@bot.command(name="nerdout")
async def nerd_out(ctx, topic: str = ""):
    """Nerds out about Queen, Flash, or HTF. Usage: !nerdout flash"""
    topic = topic.lower()
    if topic in NERD_OUT_TOPICS:
        await ctx.send(random.choice(NERD_OUT_TOPICS[topic]))
    else:
        await ctx.send("Pick a valid topic! Try `!nerdout queen`, `!nerdout flash`, or `!nerdout htf`.")

# --- Command: Queen Quiz ---
@bot.command(name="quiz")
async def queen_quiz(ctx):
    """Starts a quick, interactive Queen trivia question."""
    item = random.choice(QUEEN_QUIZ)
    await ctx.send(f"**Queen Trivia Time!** 👑\n{item['q']}\n*(You have 30 seconds to type your answer!)*")

    def check(m):
        return m.channel == ctx.channel and not m.author.bot

    try:
        # Wait for user input
        guess = await bot.wait_for('message', check=check, timeout=30.0)
        
        if guess.content.strip().lower() == item['a'].lower():
            await ctx.send(f"🎉 Correct, {guess.author.mention}! You know your stuff!")
        else:
            await ctx.send(f"❌ Close, but not quite! The correct answer was **{item['a']}**.")
            
    except asyncio.TimeoutError:
        await ctx.send(f"⏱️ Time's up! The answer was **{item['a']}**.")

# --- Command: Chat Initiator ---
@bot.command(name="chat")
async def start_chat(ctx):
    """Starts a friendly, real-person-style conversation starter."""
    await ctx.send(f"{random.choice(CHAT_PROMPTS)}")

# Run the bot
bot.run('MTU2MDUxMDk1NjMxNTA4MjgwMg.GhrGjV.SHoHaM3hpoCB20zcpENq9b8S--AXDsFVHQT8Mo')

import os
from dotenv import load_dotenv

load_dotenv()
# ... your existing bot code ...

bot.run(os.getenv('DISCORD_TOKEN'))

