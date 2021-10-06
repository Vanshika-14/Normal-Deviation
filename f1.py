import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import statistics

df = pd.read_csv("data.csv")
dataSet = df["writing score"].tolist()

mean = statistics.mean(dataSet)
standard_deviation = statistics.stdev(dataSet)
median = statistics.median(dataSet)
mode = statistics.mode(dataSet)

first_standard_deviation_start, first_standard_deviation_end = mean - standard_deviation, mean + standard_deviation
second_standard_deviation_start, second_standard_deviation_end = mean - (2 * standard_deviation), mean + (2 * standard_deviation)
third_standard_deviation_start, third_standard_deviation_end = mean - (3 * standard_deviation), mean + (3 * standard_deviation)

fig = ff.create_distplot([dataSet], ["writing scores"], show_hist = False)

# fig.show()

list_of_data_within_1_standard_deviation = [result for result in dataSet if result > first_standard_deviation_start and result < first_standard_deviation_end]
list_of_data_within_2_standard_deviation = [result for result in dataSet if result > second_standard_deviation_start and result < second_standard_deviation_end]
list_of_data_within_3_standard_deviation = [result for result in dataSet if result > third_standard_deviation_start and result < third_standard_deviation_end]

print("RESULTS:")
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)

print("STANDARD DEVIATIONS:")
print("{}% of Data lies within 1 Standard Deviation...".format(len(list_of_data_within_1_standard_deviation)*100.0/len(dataSet)))
print("{}% of Data lies within 2 Standard Deviation...".format(len(list_of_data_within_2_standard_deviation)*100.0/len(dataSet)))
print("{}% of Data lies within 3 Standard Deviation...".format(len(list_of_data_within_3_standard_deviation)*100.0/len(dataSet)))