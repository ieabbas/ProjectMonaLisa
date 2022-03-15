from TikTokApi import TikTokApi

api = TikTokApi()
user = api.user(username='cherrius_')

count = 0
for video in user.videos(count=1000):
    count += 1
print(count)