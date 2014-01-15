#!/usr/bin/python
import numpy as np
from bokeh.plotting import *
import time
import pandas
import sys
import calendar
import numpy as np

trade_x = []
trade_price = []
trade_volume = []
trade_buysell = []
trade_marklim = []
trade_unixtime = []

four_hour_trade_prices = []
two_hour_trade_prices = []
one_hour_trade_prices = []
my_time = calendar.timegm(time.gmtime()) 

infile = open ("trades.csv",'r')
text = infile.read()
lines = text.split('\n')
for l in lines[1:]:
  data = l.split(',')
  if len(data)>1:
    trade_x.append(str(data[2]))
    trade_price.append(float(data[0]))
    trade_volume.append(float(data[1]))
    trade_buysell.append(str(data[3]))
    trade_marklim.append(str(data[4]))
    trade_unixtime.append(float(data[6]) * 1)
    
    trade_time = float(data[6]) * 1
    if(trade_time >= my_time - (60 * 60 * 4)):
      four_hour_trade_prices.append(float(data[0]))
    if(trade_time >= my_time - (60 * 120)):
      two_hour_trade_prices.append(float(data[0]))
    if(trade_time >= my_time - (60 * 60)):
      one_hour_trade_prices.append(float(data[0]))

output_file("trades.html", title="XBTLTC Trades")
hold()
window_size = 30

#line(pandas.to_datetime(trade_x),np.array(trade_price), color="#0000FF", x_axis_type = "datetime", tools="pan,zoom,resize", width=1300,height=600, title = 'Price')
#line(trade_unixtime,trade_price, color="#0000FF", x_axis_type = "datetime", tools="pan,zoom,resize", width=1100,height=600, title = 'Price')
line(trade_unixtime,trade_price, color="#0000FF", tools="pan,zoom,resize", width=1100,height=600, title = 'Price')


thirty_min_ago = my_time - 60 * 30
one_hour_height = np.std(one_hour_trade_prices) * 2
one_hour = 60 * 60
rect([thirty_min_ago],[np.mean(one_hour_trade_prices)], one_hour, one_hour_height,fill_color="#D5E1DD", fill_alpha=0.6, line_color="#000000" )
rect([thirty_min_ago],[np.mean(one_hour_trade_prices)], one_hour, .03 ,fill_color="#FF0000", line_color="#FF0000" )

one_hour_ago = my_time - 60 * 60
two_hour_height = np.std(two_hour_trade_prices) * 2
two_hour = 60 * 60 * 2
rect([one_hour_ago],[np.mean(two_hour_trade_prices)], two_hour, two_hour_height,fill_color="#D5E1DD", fill_alpha=0.01, line_color="#000000" )
rect([one_hour_ago],[np.mean(two_hour_trade_prices)], two_hour, .03 ,fill_color="#FF0000", line_color="#FF0000" )

two_hour_ago = my_time - 60 * 60 * 2
four_hour_height = np.std(four_hour_trade_prices) * 2
four_hour = 60 * 60 * 4
rect([two_hour_ago],[np.mean(four_hour_trade_prices)], four_hour, four_hour_height,fill_color="#D5E1DD", fill_alpha=0.02, line_color="#000000" )
rect([two_hour_ago],[np.mean(four_hour_trade_prices)], four_hour, .03 ,fill_color="#FF0000", line_color="#FF0000" )

xaxis()[0].axis_label = "Time"
yaxis()[0].axis_label = "Price"

curplot().title = "Trades"
grid().grid_line_alpha=0.3
figure()

show()
