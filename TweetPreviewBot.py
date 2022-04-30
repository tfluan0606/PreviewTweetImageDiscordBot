# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 12:56:34 2022

@author: tfluan0606
"""


import discord
import tweepy

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#twitter API token
consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret'
access_token= 'access_token'
access_token_secret= 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


@client.event
async def on_ready():
    #log information
    #if it boot successfullym,it will send message to specific channel
    log = client.get_channel('channel id(type int)')
    await log.send('成功啟動')


@client.event
async def on_message(message):
    
    #just for handling where the bot should work on,you can set to what you want
    if message.channel.id == 'channel id(type int)':
        channel = message.channel
        url = message.content.split('/')
        if 'twitter.com' in url or 'mobile.twitter.com' in url:
            #process the tweet url to get the tweet id
            statusIndex = url.index('status')
            status = api.get_status(int(url[statusIndex+1].split('?')[0]))
            
            try:
                if 'media' in status.extended_entities:
                    if 'video_info' in status.extended_entities['media'][0]:
                        vodList = list(filter(lambda x:'bitrate' in x,status.extended_entities['media'][0]['video_info']['variants']))           
                        vodHighest = max(vodList,key = lambda x : x['bitrate'])
                        await channel.send(vodHighest['url'])
                        
                    else:
                        for image in status.extended_entities['media']:
                            if image['type'] == 'photo':
                                await channel.send(image['media_url_https'])
                                
            except Exception as e:
                
                pass
                #logging section
                #if error occurs,it will send the error message to specific channel
                #紀錄錯誤的部分，如果有出錯會把錯誤訊息送到特定的頻道去
                """
                await channel.send('推文內容不支援或是出錯。/Error or tweet type not supports')
                log = client.get_channel(channel id(type int))
                await log.send(e)
                """



client.run('discord token')



