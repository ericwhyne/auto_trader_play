#!/usr/bin/python
import numpy as np
from bokeh.plotting import *
import time
import pandas
import sys

spread_x = []
spread_ask = []
spread_bid = []
infile = open ("spread.csv",'r')
text = infile.read()
lines = text.split('\n')
for l in lines[1:]:
  data = l.split(',')
  if len(data)>1:
    print str(data[0])
    spread_x.append(str(data[0]))
    spread_ask.append(float(data[1]))
    spread_bid.append(float(data[2]))

output_file("line.html", title="XBTLTC Spread")
hold()
window_size = 30
#line(np.array(spread_x),np.array(spread_bid), color="#00FF00", tools="pan,zoom,resize, preview, save", name="yb")
#line(np.array(spread_x),np.array(spread_ask), color="#0000FF", tools="pan,zoom,resize, preview, save", name="ya")

line(pandas.to_datetime(spread_x),np.array(spread_bid), color="#0000FF", x_axis_type = "datetime", \
    tools="pan,zoom,resize", width=1900,height=900, title = 'bid')
line(pandas.to_datetime(spread_x),np.array(spread_ask), color="#00FF00", x_axis_type = "datetime", \
    tools="pan,zoom,resize", width=1900,height=900, title = 'ask')

xaxis()[0].axis_label = "Time"
yaxis()[0].axis_label = "bid"

curplot().title = "Spread"
grid().grid_line_alpha=0.3
figure()

show()
