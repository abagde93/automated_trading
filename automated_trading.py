from Robinhood import Robinhood

import re
#from datetime import datetime
import datetime
import time

from ISStreamer.Streamer import Streamer

import threading


class automate():

  can_buy = False
  price_window_thread = True
  
  def get_time(self):

    #Get current 24HR timestamp
    ts = time.time()
    
    current_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    timestring_split = map(int, re.split(r"[:,]", current_time))
    current_time = timestring_split[0]*3600+timestring_split[1]*60+timestring_split[2]
    
    #Check if we are within trading hours(6:30:00 --> 23400 & 13:00:00 --> 46800). Times range between 0 - 86399
    if(0 < current_time < '86399'):
        self.can_buy = True
        
  def price_window(self, stock_list, time_interval):
    
    #In this function, calculate the average price of a stock over a certain amount of time
    quote = my_trader.last_trade_price("AMD")
    print quote
    threading.Timer(time_interval, auto.price_window, [stock_list, time_interval]).start()
    
    
        
    


#Import class Robinhood from Robinhood.py file
my_trader = Robinhood()

#Make instance of class automate
auto = automate()

#login
username = raw_input("Username: ")
password = raw_input("Password: ")
my_trader.login(username, password)


#Monitor price of stock(s) for a certain time period
stocks_to_monitor = ["AMD","JNUG"]
time_window = 5.0 #Time window in seconds
auto.price_window(stocks_to_monitor, time_window)

    

while True:
    #Get current time and allow purchases if within trading hours
    auto.get_time()
    
    
   
    
  
    
  


    
    



