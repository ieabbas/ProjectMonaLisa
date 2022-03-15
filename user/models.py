from flask import Flask, jsonify, request, session, redirect
from TikTokApi import TikTokApi

api = TikTokApi()

class User:

    def __init__(self, username):
        self.username = username
        self.user = api.user(username=self.username)

    def getVideoCount(self):
        count = 0
        for video in self.user.videos(count=500):
            count += 1
        return jsonify({"count": count}), 200