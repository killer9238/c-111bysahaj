import csv
import plotly.figure_factory as ff
import statistics
import pandas as pd
import random
import plotly.graph_objects as go

df=pd.read_csv('studentMarks.csv')
data=df["Math_score"].tolist()
fig=ff.create_distplot([data],["Maths Score"],show_hist=False)
fig.show()

mean=statistics.mean(data)
std=statistics.stdev(data)

print("Mean of the data is-> "+str(mean))
print("Standard Deviation of the data is-> "+str(std))

#code to find the mean of 100 data points 1000 times
#function to get the mean of given data points
#pass the number of data points you want as counter
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return(mean)

#pass the number of times you want the mean of the data points as the parameter in the range function in for loop.
mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

mean=statistics.mean(mean_list)
std=statistics.stdev(mean_list)

print("The mean of the gorup of 100 students each is-> "+str(mean))
print("The Standard Deviation of the group of 100 students is-> "+str(std))

fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.show()

#finding the standard deviation starting and ending values
#1,2 and 3 standard deviation for height
first_stdev_start,first_stdev_end=mean-std,mean+std

second_stdev_start,second_stdev_end=mean-(2*std),mean+(2*std)

third_stdev_start,third_stdev_end=mean-(3*std),mean+(3*std)

print("Std1",first_stdev_start,first_stdev_end)
print("Std2",second_stdev_start,second_stdev_end)
print("Std3",third_stdev_start,third_stdev_end)

fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines",name="Std1 satrt"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name="Std1 end"))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines",name="Std2 satrt"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="Std2 end"))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines",name="Std3 start"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name="Std3 end"))
fig.show()