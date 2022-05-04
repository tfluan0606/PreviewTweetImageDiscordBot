# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 11:59:07 2022

@author: tfluan0606
"""


import discord
import tweepy
import os
import re

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#twitter token
consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret'
access_token= 'access_token'
access_token_secret= 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


@client.event
async def on_ready():
    pid = os.getpid()
    log = client.get_channel(channelId)
    await log.send('成功啟動'+'\n'+str(pid))


@client.event
async def on_message(message):
        
    
    if do something:
        channel = message.channel
        #字串的處理
        url = message.content.split('/')
        if 'twitter.com' in url or 'mobile.twitter.com' in url:

            embeds = message.embeds
            checkUrl = len(embeds) #如果會顯示預覽，embed長度會>0
            if not checkUrl:
                #拿到推文的ID
                statusIndex = url.index('status')
                status = api.get_status(int(url[statusIndex+1].split('?')[0]),tweet_mode='extended')
                #拿推文使用者的資料(帳號、頭貼)
                userProfile = status.user
                #去掉推文內容的網址
                tweetContent = re.sub(r' https://t.co/\w{10}', '', status.full_text)
                try:
                    #如果是圖片或影片，且是敏感內容
                    if 'media' in status.extended_entities and status.possibly_sensitive:
                        #要輸出至頻道的鑲嵌內容製作
                        embedToSend = discord.Embed(description=tweetContent,color=0x00acee)
                        embedToSend.set_author(name=userProfile.name+'(@'+userProfile.screen_name+')',
                                        url='https://twitter.com/'+userProfile.screen_name,
                                        icon_url=userProfile.profile_image_url_https)
                        #影片的處理
                        if 'video_info' in status.extended_entities['media'][0]:
                            vodList = list(filter(lambda x:'bitrate' in x,status.extended_entities['media'][0]['video_info']['variants']))           
                            vodHighest = max(vodList,key = lambda x : x['bitrate'])
                            await channel.send(embed=embedToSend)
                            await channel.send(vodHighest['url'])
                            #將原網址的預覽關掉                               
                            await message.edit(suppress=True)    
                        else:
                            image = status.extended_entities['media']
                            if image[0]['type'] == 'photo':
                                embedToSend.set_image(url=image[0]['media_url_https'])
                                await channel.send(embed=embedToSend)
                            
                            #如果有多張圖片
                            if len(image) > 1:
                                for i in range(1,len(image)):
                                    if image[i]['type'] == 'photo':
                                        await channel.send(image[i]['media_url_https'])
                                                                    
                            #將原網址的預覽關掉 
                            await message.edit(suppress=True)   
                except Exception as e:
                    #有錯或不支援
                    await channel.send('推文內容不支援或是出錯。')
                    """
                    log = client.get_channel(channelId)
                    await log.send(e)
                    """



#discord token
client.run('discord token')



