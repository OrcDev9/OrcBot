from keep_alive import keep_alive
import os
import discord
from cairosvg import svg2png
import matplotlib.image as img
import numpy as npy
import asyncio
# import requests
# import json
# import random
# from time import gmtime, strftime
# from replit import db
from discord.ext import tasks

from web3 import Web3

channel_id = 771164031405785129

#w3 = Web3(Web3.IPCProvider('./path/to/geth.ipc'))
w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/14c9a01125e248b486af50a96d153c94'))

orcsABI = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"activities","outputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint88","name":"timestamp","type":"uint88"},{"internalType":"enum EtherOrcs.Actions","name":"action","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"claimable","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cooldown","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"enum EtherOrcs.Actions","name":"action_","type":"uint8"}],"name":"doAction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"enum EtherOrcs.Actions","name":"action_","type":"uint8"}],"name":"doActionWithManyOrcs","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"doSumthin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getHundredZug","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"enum EtherOrcs.Places","name":"","type":"uint8"}],"name":"lootPools","outputs":[{"internalType":"uint8","name":"minLevel","type":"uint8"},{"internalType":"uint8","name":"minLootTier","type":"uint8"},{"internalType":"uint16","name":"cost","type":"uint16"},{"internalType":"uint16","name":"total","type":"uint16"},{"internalType":"uint16","name":"tier_1","type":"uint16"},{"internalType":"uint16","name":"tier_2","type":"uint16"},{"internalType":"uint16","name":"tier_3","type":"uint16"},{"internalType":"uint16","name":"tier_4","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mint","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintBatch","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"orcs","outputs":[{"internalType":"uint8","name":"body","type":"uint8"},{"internalType":"uint8","name":"helm","type":"uint8"},{"internalType":"uint8","name":"mainhand","type":"uint8"},{"internalType":"uint8","name":"offhand","type":"uint8"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint16","name":"zugModifier","type":"uint16"},{"internalType":"uint32","name":"lvlProgress","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"enum EtherOrcs.Places","name":"place","type":"uint8"},{"internalType":"bool","name":"tryHelm","type":"bool"},{"internalType":"bool","name":"tryMainhand","type":"bool"},{"internalType":"bool","name":"tryOffhand","type":"bool"}],"name":"pillage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"enum EtherOrcs.Places","name":"place","type":"uint8"},{"internalType":"bool","name":"tryHelm","type":"bool"},{"internalType":"bool","name":"tryMainhand","type":"bool"},{"internalType":"bool","name":"tryOffhand","type":"bool"}],"name":"pillageBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"meta","type":"address"}],"name":"setMetadataHandler","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startingTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"supported","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"upLevel","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"zug","outputs":[{"internalType":"contract ERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'

inventoryABI = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint8","name":"","type":"uint8"}],"name":"bodies","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"footer","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"id","type":"uint8"}],"name":"getBodyName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint8","name":"id","type":"uint8"}],"name":"getHelmName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint8","name":"id","type":"uint8"}],"name":"getMainhandName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint8","name":"id","type":"uint8"}],"name":"getOffhandName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint8","name":"body_","type":"uint8"},{"internalType":"uint8","name":"helm_","type":"uint8"},{"internalType":"uint8","name":"mainhand_","type":"uint8"},{"internalType":"uint8","name":"offhand_","type":"uint8"}],"name":"getSVG","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"id_","type":"uint16"},{"internalType":"uint8","name":"body_","type":"uint8"},{"internalType":"uint8","name":"helm_","type":"uint8"},{"internalType":"uint8","name":"mainhand_","type":"uint8"},{"internalType":"uint8","name":"offhand_","type":"uint8"},{"internalType":"uint16","name":"level_","type":"uint16"},{"internalType":"uint16","name":"zugModifier_","type":"uint16"}],"name":"getTokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"header","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"","type":"uint8"}],"name":"helms","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"","type":"uint8"}],"name":"mainhands","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"","type":"uint8"}],"name":"offhands","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8[]","name":"ids","type":"uint8[]"},{"internalType":"address","name":"source","type":"address"}],"name":"setBodies","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8[]","name":"ids","type":"uint8[]"},{"internalType":"address","name":"source","type":"address"}],"name":"setHelms","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8[]","name":"ids","type":"uint8[]"},{"internalType":"address","name":"source","type":"address"}],"name":"setMainhands","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8[]","name":"ids","type":"uint8[]"},{"internalType":"address","name":"source","type":"address"}],"name":"setOffhands","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8[]","name":"ids","type":"uint8[]"},{"internalType":"address","name":"source","type":"address"}],"name":"setUniques","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"","type":"uint8"}],"name":"uniques","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'

orcsAddress = "0xf40E6e68c13e7D445638928e74715bed30FdfE1A"

inventoryAddress = '0x6b36fCC8D847B321174a878072249e35f8DcF7F2'

EtherOrcsContract = w3.eth.contract(abi=orcsABI, address=orcsAddress)

InventoryContract = w3.eth.contract(abi=inventoryABI, address=inventoryAddress)

@tasks.loop(minutes=10)
async def send():
  await send_embed_zug()
  
@send.before_loop
async def before():
  await client.wait_until_ready()


client = discord.Client()



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content.lower()
  
  print(msg)

  if msg.startswith('!zug'):
      print('zug')
      await send_embed_zug()

  # ORC INFO
      
  if msg.startswith('!data'):
    orc_id = msg.split()[1]
    print(orc_data(orc_id))
    await send_embed_orc_data(orc_id)

  if msg.startswith('!img'):
    orc_id = msg.split()[1]
    print(orc_data(orc_id))
    await send_orc_img(orc_id)

  if msg.startswith('!orc'):
    orc_id = msg.split()[1]
    await send_image_and_data(orc_id)

  # LOOT POOLS
  
  if msg.startswith('!lootpool'):
    pool_id = int(msg.split()[1])-1
    if pool_id <= 5:
      await lootPool(pool_id)

  if msg.startswith('!loot town'):
    await lootPool(0)

  if msg.startswith('!loot dungeon'):
      await lootPool(1)

  if msg.startswith('!loot thecrypt'):
    await lootPool(2)

  if msg.startswith('!loot the crypt'):
      await lootPool(2)

  if msg.startswith('!loot castle'):
    await lootPool(3)

  if msg.startswith('!loot dragons lair'):
      await lootPool(4)
  if msg.startswith('!loot the dragons lair'):
    await lootPool(4)

  if msg.startswith('!loot dragonslair'):
    await lootPool(4)

  if msg.startswith('!loot thedragonslair'):
    await lootPool(4)

  if msg.startswith('!loot the ether'):
    await lootPool(5)

  if msg.startswith('!loot theether'):
    await lootPool(5)

def start():
  keep_alive()
  client.run(os.getenv('TOKEN'))


# Send To Discord - Bot Methods
async def send_embed_zug():
  embed = discord.Embed(
    colour = discord.Colour.blue()
  )
  embed.set_image(url="https://i.ibb.co/NFJyMpt/Screen-Shot-2021-10-01-at-5-06-19-PM.png")
  channel = client.get_channel(channel_id)
  await channel.send(embed=embed)


async def send_embed_orc_data(orc_id):
  embed = discord.Embed(
    colour = discord.Colour.blue()
  )
  
  data = orc_data(orc_id)

  helm = getHelmName(data[1])
  mainhand = getMainhandName(data[2])
  offhand = getOffhandName(data[3])
  level = data[4]
  zugModifier = data[5]

  embed.add_field(name="Id", value="{}".format(orc_id), inline=True)
  embed.add_field(name="Level", value="{}".format(level), inline=True)
  embed.add_field(name="Zug Modifier", value="{}".format(zugModifier), inline=True)
  embed.add_field(name="Helm", value="{}".format(helm), inline=True)
  embed.add_field(name="Mainhand", value="{}".format(mainhand), inline=True)
  embed.add_field(name="Offhand", value="{}".format(offhand), inline=True)

  
  channel = client.get_channel(channel_id)
  await channel.send(embed=embed)

async def send_orc_img(orc_id):
  # body, helm, mainhand, offhand - SVG arg order
  orc = orc_data(orc_id)
  body = orc[0]
  helm = orc[1]
  mainhand = orc[2]
  offhand = orc[3]

  svg = InventoryContract.functions.getSVG(body, helm, mainhand, offhand).call()

  svg2png(bytestring=svg, write_to='orc.png')
  
  m = img.imread("orc.png")
  w, h = m.shape[:2]
  xNew = int(w * 4)
  yNew = int(h * 4)
  xScale = xNew/(w-1)
  yScale = yNew/(h-1)
  newImage = npy.zeros([xNew, yNew, 4]);
  
  for i in range(xNew-1):
    for j in range(yNew-1):
        newImage[i + 1, j + 1]= m[1 + int(i / xScale),
                                  1 + int(j / yScale)]
  
  img.imsave('scaled.png', newImage);

  channel = client.get_channel(channel_id)

  await channel.send(file=discord.File( "scaled.png"))

## Using asyncio due to orc images not being stored server-side
async def send_image_and_data(orc_id):
  await asyncio.gather(send_orc_img(orc_id), send_embed_orc_data(orc_id))

defaultImageURL = "https://art.pixilart.com/b1d2bc6cd17acba.png"

async def lootPool(poolNum):

  poolInfo = EtherOrcsContract.functions.lootPools(poolNum).call()
  enteredNum = poolNum + 1

  poolNames = {
    1: "Town",
    2: "Dungeon",
    3: "The Crypt",
    4: "Castle",
    5: "Dragons Lair",
    6: "The Ether"
  } 
  minLVL = int(poolInfo[0])
  totalItems = int(poolInfo[3])
  tier1 = int(poolInfo[4])
  tier2 = int(poolInfo[5])
  tier3 = int(poolInfo[6])

  pool_name = poolNames[enteredNum]
  tier1_name = "Tier %s Items"%(enteredNum)
  tier2_name = "Tier %s Items"%(enteredNum)
  tier3_name = "Tier %s Items"%(enteredNum)

  embed = discord.Embed(
    colour = discord.Colour.blue()
  )

  embed.add_field(name="Area", value=pool_name, inline=True)
  embed.add_field(name="Minimum Level", value=minLVL, inline=True)
  embed.add_field(name="Items Remaining", value=totalItems, inline=True)
  embed.add_field(name=tier1_name, value=tier1, inline=True)
  embed.add_field(name=tier2_name, value=tier2, inline=True)
  embed.add_field(name=tier3_name, value=tier3, inline=True)
  embed.set_image(url=defaultImageURL)

  channel = client.get_channel(channel_id)
  await channel.send(embed=embed)

## Data fetch 

def orc_data(id):
  int_id = Web3.toInt(text=id)
  return EtherOrcsContract.functions.orcs(int_id).call()

# Helper functions
def getHelmName(id):
  int_id = Web3.toInt(text=id)
  return InventoryContract.functions.getHelmName(int_id).call()

def getMainhandName(id):
  int_id = Web3.toInt(text=id)
  return InventoryContract.functions.getMainhandName(int_id).call()

def getOffhandName(id):
  int_id = Web3.toInt(text=id)
  return InventoryContract.functions.getOffhandName(int_id).call()

