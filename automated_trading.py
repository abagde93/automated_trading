from Robinhood import Robinhood

import re
import datetime
import time

#from ISStreamer.Streamer import Streamer

#Setup
my_trader = Robinhood()
#login
username = input("Username: ")
password = input("Password: ")
my_trader.login(username, password)

    
#streamer = Streamer(bucket_name="Stock Tracker", bucket_key="Stock_Tracker_020817", ini_file_location="./isstreamer.ini")


while True:
    ts = time.time()
    current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
     
    if re.findall(r'[2][0-9]{1}[:][0-9]{2}[:][0-9]{2}', current_time):
        print("peepmeep")
    
    print(current_time)
    my_trader.print_quote("AMD")
    time.sleep(10)





    
    


#print(my_trader.quote_data("AMD"))
#print('\n')
#print(my_trader.positions())
