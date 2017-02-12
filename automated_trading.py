from Robinhood import Robinhood

import re
#from datetime import datetime
import datetime
import time

from ISStreamer.Streamer import Streamer

import threading


class automate():


  #global variable that is set in get_time - decides whether stocks can be bought
  #depending on if market is open
  can_buy = False
  
  #store contents of quote_array_2D in price_window to access globally
  global_quote_matrix = 0
  
  #store contents of quote average for each stock over time period
  avg_quotes = []
  
  
  
  def get_time(self):

    #Get current 24HR timestamp
    ts = time.time()
    
    current_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    timestring_split = map(int, re.split(r"[:,]", current_time))
    current_time = timestring_split[0]*3600+timestring_split[1]*60+timestring_split[2]
    
    #Check if we are within trading hours(6:30:00 --> 23400 & 13:00:00 --> 46800). Times range between 0 - 86399
    if(0 < current_time < '86399'):
        self.can_buy = True
        
  def price_window(self, stock_list, time_interval, quote_array_2D):
    
    #In this function, populate an matrix of quotes for each stock. The quote will be updated every minute, and added to array for each stock
    #Matrix should be of the form of below
    
    #[[12.04, 12.05, 12.04, 12.07, 12.07, 12.08, 12.10, 12.03, 12.03],
    # [13.24, 13.25, 13.26, 13.27, 13.21, 13.22, 13.24, 13.21, 13.20],
    # [1.67, 1.68, 1.66, 1.65, 1.64, 1.62, 1.66, 1.69, 1.64],
    # [8.06, 8.09, 8.04, 8.03, 8.02, 8.01, 7.99, 8.01, 8.02]]
    
    #Create index to keep track of which stock we are processing
    stock_index = 0
    for item in stock_list:
      quote = float(my_trader.last_trade_price(item))
      
      
      #Figure out way to push values through array - in FILO architecture. If array is full, last value should be deleted/popped off, and new value should be the
      #first item in the array. Try doing this with an array containing 10 quotes
      
      while len(quote_array_2D[stock_index]) <= 10:
          quote_array_2D[stock_index].insert(0, quote)
      quote_array_2D[stock_index].pop()
      stock_index = stock_index + 1
      #print(quote_array_2D)
      
      
      self.global_quote_matrix = quote_array_2D
    print(self.global_quote_matrix)
      
    #Call this function every time interval(1 minute or so). Make sure this is the last line in the function
    threading.Timer(time_interval, auto.price_window, [stock_list, time_interval, quote_array_2D]).start()

  def compare_price(self, time_interval, stocks_to_monitor):
      self.avg_quotes = [None] * len(stocks_to_monitor)
      #print(self.avg_quotes)
      for stock in range(0, len(stocks_to_monitor)):
          self.avg_quotes[stock] = sum(self.global_quote_matrix[stock]) / float(len(self.global_quote_matrix[stock]))
      
      print(self.avg_quotes)
      auto.buy_sell()
      
      #Call this function every time interval(1 minute or so). Make sure this is the last line in the function  
      threading.Timer(time_interval, auto.compare_price, [time_interval, stocks_to_monitor]).start()
   
  def buy_sell(self):
      print "in buysell"
    
    
        
    


#Import class Robinhood from Robinhood.py file
my_trader = Robinhood()

#Make instance of class automate
auto = automate()

#login
username = raw_input("Username: ")
password = raw_input("Password: ")
my_trader.login(username, password)


#Get a quote for stocks every 60 seconds - this function has its own thread
stocks_to_monitor = ['AMD', 'TGB', 'MSTX', 'NAK']
time_window_quote = 6.0 #Time window in seconds

#Initializing quote matrix. Each stock has it's own row with 10 quotes at a time
cols_count,rows_count = 10,len(stocks_to_monitor)
quote_matrix = [[0 for x in range(cols_count)] for x in range(rows_count)]

auto.price_window(stocks_to_monitor, time_window_quote, quote_matrix)

#Every 10 minutes take average of quotes for each stock, and compare to trade price at market open
#This function also has it's own thread
time_window_compare = 60.0
auto.compare_price(time_window_compare, stocks_to_monitor)



    

while True:
    #Get current time and allow purchases if within trading hours
    auto.get_time()
    
    
   
    
  
    
  


    
    



