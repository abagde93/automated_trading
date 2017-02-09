from Robinhood import Robinhood

import re
#from datetime import datetime
import datetime
import time

from ISStreamer.Streamer import Streamer

#Setup
my_trader = Robinhood()

#login
username = raw_input("Username: ")
password = raw_input("Password: ")
my_trader.login(username, password)

    
streamer = Streamer(bucket_name="Stock Tracker", bucket_key="Stock_Tracker_020817", ini_file_location="./isstreamer.ini")


while True:

    #Get current 24HR timestamp
    ts = time.time()
    current_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    
    #Look for timstamp 06:3x:xx - This is when the market opens
    if re.findall(r'[0][6][:][3][0-9]{1}[:][0-9]{2}', current_time):
        open_time = current_time
        print "Market has opened"
      
    #Look for timstamp 13:00:xx - This is when the market closes
    if re.findall(r'[0][6][:][0][0][:][0-9]{2}', current_time):
        close_time = current_time
        print "Market has closed"
        
    #Convert open_time and close_time to minute notation - 1440 minutes in a day
    
    
    
        
    
    print(current_time)
    quote = my_trader.last_trade_price("AMD")
    print(quote)
    #re.findall(r'\d+', quote)
    
    
    streamer.log("Current AMD quote", "{value}".format(value=quote))
    #streamer.log("Altitude", "{value}".format(value=quote))
    time.sleep(10)





    
    


#print(my_trader.quote_data("AMD"))
#print('\n')
#print(my_trader.positions())
