from IPython.display import display
import ipywidgets as widgets
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np
from d3graph import d3graph


original_tweet = input("Hello and welcome to Tweets R' Us, Where we help you craft your perfect responses on Twitter. To start, can you please enter in the Tweet that you want to repond to?\n")

adj_matrix = pd.DataFrame({
    '0': [0],
}, index=['0'])



tweet = [
    {'tweet': original_tweet, 'connection': -1, 'sentiment': 0},
    
]
df_tweet = pd.DataFrame(tweet)




print("Here is the slider that you can use to choose the sentiment score that you want to include for the response:\n -1 means very negative\n 0 means neutral \n 1 means very positive \n")


# Define the function to update the graph based on the slider value
def update_graph(val):
    # Retrieve the current value of the slider
    slider_value = slider.val
    
    # Update the global variable graph_value
    global graph_value
    graph_value = slider_value
    
    # Update the graph based on the slider value
    # For example, you could use d3.select() to select the relevant SVG element in the D3 visualization, and update its attributes based on the slider value
    # This example just prints the slider value
    #print(slider_value)
    
    # Display a confirmation button
    confirm_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
    confirm_button = Button(confirm_ax, 'Confirm', color='green', hovercolor='lightgreen')
    
    # Define the function to handle the confirmation button click
    def confirm_clicked(event):
        global confirmed
        confirmed = True
    
    # Add an event listener to the confirmation button
    confirm_button.on_clicked(confirm_clicked)
    
    # Wait for the user to confirm their selection
    global confirmed
    confirmed = False
    while not confirmed:
        plt.pause(0.05)

# Define the slider widget
slider_ax = plt.axes([0.1, 0.1, 0.8, 0.03])
slider = Slider(slider_ax, label="Mood:", valmin=-1, valmax=1, valinit=0, valstep=0.1)

# Add the event listener to the slider
slider.on_changed(update_graph)

# Display the slider and the graph
plt.show()

#HERE IS WHERE WE WOULD SEND THE TWEET AND THE SENTIMENT SCORE TO ANEESHES FUN FUN FUN TIME
new_tweet = "in in in in in in in in in"
sentiment_score = round(graph_value)
Done = False
past_connection = 0
while Done == False:
    new_tweet_data =  [
    {'tweet': new_tweet, 'connection': past_connection, 'sentiment': sentiment_score}   
]
    df_tweet = df_tweet.append(new_tweet_data)
    row = df_tweet.iloc[-1]
    
    
    papa_node = row.connection


    adj_matrix.loc[str(len(df_tweet))] = 0
    adj_matrix[str(len(df_tweet))] = 0
    adj_matrix.loc[str(len(df_tweet)), str(papa_node)] = 1
    adj_matrix.loc[str(papa_node), str(len(df_tweet))] = 1

    # Initialize
    d3 = d3graph()
    # Load karate example
    

    label = df_tweet['tweet'].values
    

    d3.graph(adj_matrix)
    d3.set_node_properties(color=df_tweet['sentiment'].values)
    '''
    d3.show()
    
    d3.set_node_properties(label=label, color=label, cmap='Set1')
    d3.show()

    d3.set_node_properties(size=node_size)
    d3.show()

    d3.set_node_properties(color=label, size=node_size)
    d3.show()

    d3.set_edge_properties(edge_distance=100)
    d3.set_node_properties(color=node_size, size=node_size)
    d3.show()
    '''
    # d3 = d3graph(charge=1000)
    # d3.graph(adjmat)
    # d3.set_node_properties(color=node_size, size=node_size)
    # d3.show()

    # d3 = d3graph(collision=1, charge=250)
    # d3.graph(adjmat)
    # d3.set_node_properties(color=label, size=node_size, edge_size=node_size, cmap='Set1')
    # d3.show()

    d3.set_edge_properties(directed=True)
    d3.show()

    Done = input("Do you want to add another tweet?")
    
