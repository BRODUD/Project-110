from random import randint
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import statistics as ss
import random
import plotly.graph_objects as go

df = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 110\medium_data.csv')
# .shape shows the rows and columns (only works in dataframe.)
print(df.shape)
data = df['responses'].tolist()

# code to find mean and std deviation of 100 random data points
#function to get the mean of given data samples

def random_set_of_mean(counter):
    dataset =[]
    for i in range(0,counter):
        random_index= random.randint(0,6508)
        value = data[random_index]
        dataset.append(value)

    mean_sample = ss.mean(dataset)
    return mean_sample
#std_dev_sample = ss.stdev(dataset)


# function to plot the mean list graph
def show_fig(mean_list):
    df= mean_list
    mean = ss.mean(mean_list)
    print("Mean of sampling distribution: ", mean)
    fig = ff.create_distplot([df],["Responses"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()


# function to get mean of 100 (counter) data points 1000 times and plot the graph
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
        
    std_dev = ss.stdev(mean_list)
    print("Standard Deviation of sampling distribution: ", std_dev)
    show_fig(mean_list)


setup()