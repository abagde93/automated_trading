from Robinhood import Robinhood

import re
#from datetime import datetime
import datetime
import time

from ISStreamer.Streamer import Streamer

import threading


class automate():

  can_buy = False
  amd_quote_array = []
  jnug_quote_array = []
  
  
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
    
    #In this function, populate an array of quotes for each stock. The quote will be updated every minute, and added to array
    amd_quote = float(my_trader.last_trade_price("AMD"))
    #self.amd_quote_array.append(amd_quote)
    
    #Figure out way to push values through array - in FILO architecture. If array is full, last value should be deleted/popped off, and new value should be the
    #first item in the array. Try doing this with an array containing 10 quotes
    
    while len(self.amd_quote_array) <= 10:
        self.amd_quote_array.insert(0, amd_quote)
    self.amd_quote_array.pop()
    print(self.amd_quote_array)
    #print(sum(self.amd_quote_array) / float(len(self.amd_quote_array)))
    
    #Call this function every time interval(1 minute or so). Make sure this is the last line in the function
    threading.Timer(time_interval, auto.price_window, [stock_list, time_interval]).start()
    
    
        
    


#Import class Robinhood from Robinhood.py file
my_trader = Robinhood()

#Make instance of class automate
auto = automate()

#login
username = raw_input("Username: ")
password = raw_input("Password: ")
my_trader.login(username, password)


#Get a quote for stocks every 60 seconds - this function has its own thread
stocks_to_monitor = ["AMD","JNUG"]
time_window = 10.0 #Time window in seconds
auto.price_window(stocks_to_monitor, time_window)

#Every 15 minutes take average of ***_quote_arrays, and compare to trade price at market open



    

while True:
    #Get current time and allow purchases if within trading hours
    auto.get_time()
    
    
   
    
  
    
  


    
    



