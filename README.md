# PreviewTweetImageDiscordBot
Somehow discord can't show some of preview of tweets(most of them are NSFW).By replace the "twitter" in url with "fxtwitter", it works, but it's annoying.
This Bot written by discord.py can send the image link(and some video/gif link) in tweets to the text channel.
This Bot also use tweepy, so if you want to use it, you need to get twitter api token.

If your discord.py version is not 2.0, it may not work.

# 不用再輸入fx就能直接顯示twitter連結的內容了
因為每次貼連結都要手動輸入fx很白癡，所以就自己寫了一隻機器人。
只要是推文連結他都會幫你把裡面的圖片或影片連結貼到頻道內，如果沒有就不會有任何動作。
同時有一些logging的機制，可以自己決定要不要設定，程式碼內有註解。

需要注意的是記得將discord py的版本手動更新到2.0，除了機器人本身的語法有改成2.0的寫法外，2.0才有支援討論串的功能。
