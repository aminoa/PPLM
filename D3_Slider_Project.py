from IPython.display import display
import ipywidgets as widgets
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np
from d3graph import d3graph
from twitter_responses import *

#This is where we get the original tweet that will start off the entire conversation
original_tweet = input("Hello and welcome to Tweets R' Us, Where we help you craft your perfect responses on Twitter. To start, can you please enter in the Tweet that you want to repond to?\n")

#These are the matricies that will hold all of the data
adj_matrix = pd.DataFrame({
    '0': [0],
}, index=['0'])

tweet = [
    {'tweet': original_tweet, 'connection': 0, 'sentiment': 0, 'og': 'Starting Tweet'},
]

df_tweet = pd.DataFrame(tweet)
print("Here is the slider that you can use to choose the sentiment score that you want to include for the response:\n -1 means very negative\n 0 means neutral \n 1 means very positive \n")

def update_graph(val):
    # Retrieve the current value of the slider
    slider_value = slider.val
    
    global graph_value
    graph_value = slider_value
    
    # Display a confirmation button
    confirm_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
    confirm_button = Button(confirm_ax, 'Confirm', color='green', hovercolor='lightgreen')
    
    def confirm_clicked(event):
        global confirmed
        confirmed = True
    
    confirm_button.on_clicked(confirm_clicked)
    
    global confirmed
    confirmed = False
    while not confirmed:
        plt.pause(0.05)

past_connection = 0

while True:
    slider_ax = plt.axes([0.1, 0.1, 0.8, 0.03])
    slider = Slider(slider_ax, label="Mood:", valmin=-1, valmax=1, valinit=0, valstep=0.1)
    slider.on_changed(update_graph)
    plt.show()

    sentiment_score = graph_value
    print("Generating tweet...")
    new_tweet = generate_tweet(True, original_tweet, 30, sentiment_score * 0.03)

    print(new_tweet)
    check = input("Would you like to cleanup the tweet? Reply Yes or No: ")
    if check == "Yes":
        new_tweet = input("Please enter the new tweet: ")

    new_tweet_data =  [
        {'tweet': new_tweet, 'connection': past_connection, 'sentiment': sentiment_score, 'og': 'Response'}
    ]

    df_tweet = df_tweet.append(new_tweet_data)
    print(df_tweet)
    row = df_tweet.iloc[-1]
    papa_node = row.connection

    adj_matrix.loc[str(len(df_tweet) - 1)] = 0
    adj_matrix[str(len(df_tweet) - 1)] = 0
    adj_matrix.loc[str(past_connection), str(len(df_tweet) - 1)] = 1

    d3 = d3graph()
    label = df_tweet['og'].values
    tweets = df_tweet['tweet'].values
    sent_scores = df_tweet['sentiment'].values

    d3.graph(adj_matrix)
    d3.set_edge_properties(edge_distance=1000)
    d3.set_edge_properties(directed=True)
    d3.set_node_properties(color=sent_scores)
    d3.set_node_properties(label=label, color=sent_scores, cmap='coolwarm', tooltip=tweets)
    d3.show()

    stop_the_tweets = input("Are you happy with your Responses?\n Reply Yes if you are done or No if you want to continue creating responses: ")
    if stop_the_tweets == 'Yes':
        exit()
    else:
        reply = input("Do you want to create a potential reply to this tweet, or try a different reply to the original tweet? \n Type Original if you want to find a reply to the original tweet \n Type New if you want to respond to the tweet that has been generated \n Type Again if you want to generate a response with a different sentiment of the last tweet: ")
        if reply == 'Original':
            find_tweet = df_tweet.iloc[0]
            original_tweet = find_tweet.tweet
            past_connection = 0
        elif reply == 'Again':
            find_tweet = df_tweet.iloc[-1]
            last_connection = find_tweet.connection
            last_tweet = df_tweet.iloc[last_connection]
            original_tweet = last_tweet.tweet
            past_connection = last_connection
        else:
            find_tweet = df_tweet.iloc[-1]
            original_tweet = find_tweet.tweet
            past_connection = len(df_tweet) - 1