# GUI-Tweepy
# Sends a Tweet to twitter

from tkinter import *
import tkinter.messagebox
import tweepy

# you have to get the information below by applying for a Twitter Developer Account
# Personal Deets
consumer_key = "***********************"
consumer_secret = "***********************************************"
access_token = "**************************************************"
access_token_secret = "*****************************************"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# All that's left to do now, is update the status

windowT = "Post A Tweet To Twitter"
class twitter_tings:
    def __init__(self):
        # starting window
        window = Tk()
        window.title(windowT)

        # Create Window Frames
        top_frame = Frame(padx= 90, pady=10)
        mid_frame = Frame()
        bottom_frame = Frame()

        #Top Prompt & Packing top frame
        self.prompt = Label(top_frame, text="Yo, peep this. This program will post will tweet to twitter for ya.")
        self.prompt.grid()
        top_frame.grid()

        # Entry part with label (mid_frame)
        self.labelText = Label(mid_frame, text="What do you want to tweet? (Enter here ->)")
        self.labelText.grid(row=0, column=0)

        self.entry1 = Entry(mid_frame, width=50)
        self.entry1.grid(row=0, column=1, ipady=50, padx=20, pady=20)
        mid_frame.grid()

        # Buttons and gridding
        self.confirm = Button(bottom_frame, text='Send Tweet', command=self.makingTweet)
        self.confirm.grid()

        bottom_frame.grid()
        

        window.mainloop()

    def makingTweet(self):
        tweet = self.entry1.get()
        api.update_status(status = tweet)