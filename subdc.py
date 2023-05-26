import json #JSON parsing
import time #Timer functionalty
import pytz 
import requests #Getting data from the web
import discord #Discord bot API
import asyncio

#Initialize bot client

client = discord.Client(intents=discord.Intents.all()) 

channel_id = "YOUR_ID_HERE" # Replace channel_id with the actual ID of the channel you want to send messages to

bot_token = "YOUR_TOKEN_HERE"

timeout = 20 #Timeout defines the delay between checks(in minutes)

async def send_message(message):
    channel = client.get_channel(channel_id)  
    await channel.send(message)


async def meme_loop():
    #Last checked url
    last_check = 0
    #Time when the last check was ran
    last_url = None
    #Subreddit to fetch from
    subreddit = "python" 
    
    #Timer loop
    while True:
        print("Check begin!") #check 
        
        url = "https://www.reddit.com/r/"+subreddit+"/new/.json" 
        
        response = requests.get(url, headers = {'User-agent': 'subdc 0.1'}) 
        
        data = json.loads(response.text)
        url = "https://www.reddit.com" + data['data']['children'][0]['data']['permalink']
        
        print("Got URL!")
        
        if url != last_url:
            print('New post detected!')
            
            last_url = url
            
            post_url = url + '.json'
            
            response = requests.get(post_url, headers = {'User-agent': 'okdc 0.1'}) 
            
            #Load the newest post's title
            
            post_data = json.loads(response.text)
            
            post_title = post_data[0]['data']['children'][0]['data']['title']
            
            msg_output = (post_title)
            
            #data = mdata[0]['data']['children'][0]['data']['media']['reddit_video']['fallback_url']
            #data = mdata[0]['data']['children'][0]['data']['url']
            
            post_hint = post_data[0]['data']['children'][0]['data']['post_hint']
            if post_hint == 'image':
                data = post_data[0]['data']['children'][0]['data']['url']
                print('Its an image!')
                print(data)
            elif post_hint == 'hosted:video': 
                data = post_data[0]['data']['children'][0]['data']['media']['reddit_video']['fallback_url']
                print('Its a video!') 
            else: 
                data = f"Unsupported media type/YouTube video"
                print('Something else!')
                #else:
                #data = mdata[0]['data']['children'][0]['data']['url']
            await send_message(msg_output)
            await send_message(data)
            
        else:
            print("Repeat!") #The Url did repeat, no new post
        await asyncio.sleep(timeout*60)
#Change presence
@client.event 
async def on_ready(): 
    await client.change_presence(activity=discord.Activity(name="r/okdraugedebile", type=discord.ActivityType.watching))
    client.loop.create_task(meme_loop())
client.run(bot_token)
