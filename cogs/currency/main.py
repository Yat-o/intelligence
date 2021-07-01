import discord
from discord import colour
from discord import user
from discord import raw_models
from discord import embeds
from discord import member
from discord import client
from discord.ext import commands
import json
import random

from discord.ext.commands.core import command
from cogs.currency._shop import mainshop
import cogs._json

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['bal'])
    async def balance(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()

        user = ctx.author

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        embed = discord.Embed(title = f"{ctx.author.name}'s Balance")
        embed.add_field(name = "Wallet Balance", value= wallet_amt)
        embed.add_field(name = "Bank Balance", value= bank_amt)
        embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @commands.command()
    async def beg(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()

        earnings = random.randrange(101)

        user = ctx.author

        await ctx.send(f"Someone gave you {earnings} coins!")

        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump(users,f)

    @commands.command(aliases = ['wd'])
    async def withdraw(self, ctx, amount = None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("Please enter an amount")
            return
        
        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("You don't have that amount of money in your bank")
            return
        if amount<0:
            await ctx.send("You cant send *negetive* money xD")
            return

        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1*amount, "bank")

        await ctx.send(f"You withdrew {amount} coins!")

    @commands.command(aliases = ['dep'])
    async def deposit(self, ctx, amount = None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("Please enter an amount")
            return
        
        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("You don't have that amount of money in your bank")
            return
        if amount<0:
            await ctx.send("You cant send *negetive* money xD")
            return

        await update_bank(ctx.author, -1*amount)
        await update_bank(ctx.author, amount, "bank")

        await ctx.send(f"You deposited {amount} coins!")

    @commands.command(aliases = ['give'])
    async def send(self, ctx, member: discord.Member,amount = None):
        await open_account(ctx.author)
        await open_account(member)

        if amount == None:
            await ctx.send("Please enter an amount")
            return
        
        bal = await update_bank(ctx.author)

        if amount == "all":
            amount = bal[0]

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("You don't have that amount of money in your bank")
            return
        if amount<0:
            await ctx.send("You cant send *negetive* money xD")
            return

        await update_bank(ctx.author, -1*amount, "bank")
        await update_bank(member, amount, "bank")

        await ctx.send(f"You gave {amount} coins to **{member}**")

    @commands.command()
    async def slots(self, ctx, amount = None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("Please enter a amount")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("You dont have that much money")
            return
        if amount<0:
            await ctx.send("Amount cant be *negetive* xD")
            return

        final = []
        for i in range(3):
            a = random.choice(["X","O","Q"])

            final.append(a)

        await ctx.send(str(final))

        if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await update_bank(ctx.author, 2*amount)
            await ctx.send("You won!")
        else:
            await update_bank(ctx.author, -1*amount)
            await ctx.send("You lost!")

    @commands.command()
    async def rob(self, ctx, member: discord.Member):
        await open_account(ctx.author)
        await open_account(member)

        
        bal = await update_bank(member)

        if bal[1]<100:
            await ctx.send("The user must have at least a 100 coins")
            return

        earnings = random.randrange(0, bal[0])

        await update_bank(ctx.author, earnings)
        await update_bank(member, -1*earnings)

        await ctx.send(f"You robbed **{member}** and got {earnings} coins!")

    @commands.command()
    async def shop(self, ctx):
        embed = discord.Embed(title = "Shop", colour = ctx.author.colour)

        for item in mainshop:
            name = item["name"]
            price = item["price"]
            desc = item["description"]
            embed.add_field(name = name, value=f"${price} | {desc}")

        await ctx.send(embed = embed)

    @commands.command()
    async def buy(self, ctx, item, amount = 1):
        await open_account(ctx.author)

        res = await buy_this(ctx.author, item, amount)

        if not res[0]:
            if res[1] == 1:
                await ctx.send("That object isnt there")
                return
            if res[1] == 2:
                await ctx.send(f"You dont have enough money in your wallet to buy {amount} {item}")
                return
        
        await ctx.send(f"You just bought {amount} {item}")

    @commands.command(aliases = ["inv", "inventory"])
    async def bag(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []

        embed = discord.Embed(title = "Bag", colour = ctx.author.colour)
        for item in bag:
            name = item["item"]
            amount = item["amount"]

            embed.add_field(name = name, value= amount)

        await ctx.send(embed = embed)

    @commands.command()
    async def sell(self, ctx, item, amount = 1):
        await open_account(ctx.author)

        res = await sell_this(ctx.author, item, amount)

        if not res[0]:
            if res[1] == 1:
                await ctx.send("That object isnt there")
                return
            if res[1] == 2:
                await ctx.send(f"You dont have {amount} {item} in your bag.")
                return

        await ctx.send(f"You just sold {amount} {item}")

    @commands.command(aliases = ["lb", "rich"])
    async def leaderboard(self, ctx, x = 3):
        users = await get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total, reverse=True)

        embed = discord.Embed(title = f"Top Richest People", colour = ctx.author.colour)
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = client.get_user(id_)
            name = member.name
            embed.add_field(name = f"{index}. {name}", value= f"{amt}", inline=False)
            if index == x:
                break
            else:
                index += 1

        await ctx.send(embed = embed)

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    
    with open("mainbank.json","w") as f:
        json.dump(users, f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users  = json.load(f)

    return users

async def update_bank(user, change = 0, mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

async def buy_this(user,item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break
    
    if name_ == None:
        return[False, 1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return[False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing[item]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json","w") as f:
        json.dump(users, f)

    await update_bank(user, cost*-1, "wallet")

    return[True, "Worked"]


async def sell_this(user, item_name, amount, price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = item["price"]
            break
    if name_ == None:
        return[False, 1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return[False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return[False, 3]
    except:
        return[False, 3]

    with open("mainbank.json","w") as f:
        json.dump(users, f)

    await update_bank(user, cost,"wallet")

    return[True, "Worked"]

def setup(bot):
    bot.add_cog(Mod(bot))