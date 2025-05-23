
import json
import os
import csv
import inspect
from datetime import datetime
import time
import sys
import shutil
from pathlib import Path
import pandas as pd
import yfinance as yf
import finnhub

def csv_to_book(file_to_load):
    #list = csv_to_book("0upcoming.csv")
    with open(file_to_load, 'r') as f:
        reader = csv.DictReader(f)        
        loaded_list = list(reader)
    return(loaded_list)
def book_to_csv(book,output_file):
    #book_to_csv(dictionary,"0upcoming.csv")
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=book[0].keys())
        writer.writeheader()
        writer.writerows(book)


def get_finnhub_earnings(finnhub_folder,start_date,end_date):
    #get_finnhub_earnings("finnhub_earnings",start_date,end_date)
    cwd = os.getcwd()
    finnhub_directory = os.path.join(cwd, finnhub_folder)
    finnhub_list = os.listdir(finnhub_directory)
    finnhub_file_name = start_date+"."+end_date+".json"
    if finnhub_file_name not in finnhub_list:
        finnhub_client = finnhub.Client(
            api_key="cupjchpr01qk8dnkc8qgcupjchpr01qk8dnkc8r0")
        #print(finnhub_client.earnings_calendar(_from="2025-02-18", to="2025-02-18", symbol="", international=False))
        future_earnings = finnhub_client.earnings_calendar(_from=start_date,
                                                  to=end_date,
                                                  symbol="",
                                                  international=False)
        # Save the response to a JSON file
        output_file = os.path.join(finnhub_directory, finnhub_file_name)
        with open(output_file, 'w') as json_file:
            json.dump(future_earnings, json_file, indent=4)
        print("Earnings data has been saved to " + output_file + ".json")
        print("request made")
    else:
        print("already exists")


def stocks_from_finnhub_data(finnhub_file,upcoming_file):
    # Open and load JSON file
    with open(finnhub_file, 'r') as file:
        data = json.load(file)
    # Print the loaded dictionary
    data2 = data["earningsCalendar"]
    output = []
    for item in data2:
        symbol = item["symbol"]
        date = item["date"]
        new={}    
        new['symbol'] = symbol
        new['date'] = date
        output.append(new)
    for item in output:
        print(item)
    print("finnhub_file",finnhub_file)
    print(str(len(output))+" stocks in file")
    if len(output)==0:
        print("no stocks in file, no stocks for date")
        print("aborting process/operations")
        sys.exit()
    print("output[0]",output[0],output[0].keys())
    #sys.exit()
    with open(upcoming_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)

def most_vol_pri(list_length,file_upcoming,file_master):
    with open(upcoming_file, 'r') as f:
        reader = csv.DictReader(f)        
        list_upcoming = list(reader)
    with open(file_master, 'r') as f:
        reader = csv.DictReader(f)        
        list_master = list(reader)
    print(list_master)    
    count=0
    redone = []
    for val_up in list_upcoming:
        for val_master in list_master: 
            if val_up["symbol"]==val_master["symbol"]:
                count += 1
                print(val_master)
                #print(count,"match",val_up["symbol"],val_master["symbol"])
                new = {}
                new["symbol"]=val_master["symbol"]
                new["date"]=val_up["date"]
                new["vol_pri"]=val_master["vol_pri"]
                redone.append(new)
    redone = sorted(redone, key=lambda x: float(x["vol_pri"]),reverse=True)
    if list_length>0:
        redone=redone[0:list_length]
    book_to_csv(redone,file_upcoming)
    for out in redone:
        print(out)


def get_sec_earn_dates(match_file):
    look_at = []
    with open(match_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            look_at.append(row)  # Add each row to the list
    #get earnings dates
    from pathlib import Path
    cwd = os.getcwd()
    edgar_folder = os.path.join(cwd,"sec-edgar-filings")
    files = os.listdir(edgar_folder)    
    from sec_edgar_downloader import Downloader
    dl = Downloader("MyCompanyName", "my.email@domain.com")
    print(files)
    stocks = csv_to_book(match_file)
    for item in stocks:
        print(item)
        check_stock = item["symbol"]
        k8_directory = os.path.join(edgar_folder,check_stock,"8-K")
        if not os.path.isdir(k8_directory):
            continue
        print(k8_directory)
        k8_list = os.listdir(k8_directory)
        print(len(k8_list))
        print(item)
        if len(k8_list)==0:
            print(item)
            print(len(k8_list))
            remove_folder = os.path.join(edgar_folder,check_stock)
            shutil.rmtree(remove_folder)
    for val in stocks:
        check_stock = val["symbol"]
        stock = check_stock
        if check_stock not in files:
            print("now getting 8k for")
            print(stocks.index(val),len(stocks),"check_stock =",check_stock)
            ticker_symbol = check_stock
            #try:
            dl.get("8-K", ticker_symbol)
            #except Exception as e:
            #    print(f"Error Type: {type(e)}")
            print("now gotten 8k for stock "+ticker_symbol)
            print(stock)
            stock_folder = os.path.join(edgar_folder,stock,"8-K")
            print(stock_folder)
            check_file = '0sec_no_return.txt'
            if not os.path.isdir(stock_folder):
                with open(check_file, 'r') as file:
                    content = file.read()
                text_check = "\n"+check_stock+"\n"
                if text_check not in content:
                    content=content+"\n"+check_stock
                    with open(check_file, 'w') as file:
                        file.write(content)
                continue
            earn_dates = os.listdir(stock_folder)
            print(earn_dates) 
            
            
            #see what is in earnings to see why it gets deleted
            #if have problem, this to diagnostic it
            stop = "DOMH"
            if check_stock==stop:
                print("stopped at",stop)
                sys.exit()
            

            for b,date in enumerate(earn_dates):
                print(len(look_at),b,len(earn_dates))
            #print(earn_dates)
                if "-25-" not in date:
                    if "-24-" not in date:
                        if "-23-" not in date:
                            if "-22-" not in date:
                                if "-21-" not in date:
                                    if "-20-" not in date:
                                        #print(a,len(look_at),b,len(earn_dates))
                                        #print(date)
                                        to_delete = os.path.join(stock_folder,date)
                                        print(to_delete)
                                        shutil.rmtree(to_delete)
            earn_dates = os.listdir(stock_folder)
            for b,date in enumerate(earn_dates):
                print(len(look_at),b,len(earn_dates))
                check_file = os.path.join(stock_folder,date,"full-submission.txt")
                print(check_file)
                with open(check_file, 'r') as file:
                    content = file.read()  # Read the entire content of the file
                    #print(content)
                    if "Results of Operations and Financial Condition" not in content:
                        to_delete = os.path.join(stock_folder,date)
                        print("deleting= "+to_delete)
                        shutil.rmtree(to_delete)
                        continue
                        """
                    if "ITEM INFORMATION:		Regulation FD Disclosure" in content:
                        to_delete = os.path.join(stock_folder,date)
                        print("deleting= "+to_delete)
                        shutil.rmtree(to_delete)
                        continue
                        """
                    #else:
                    with open(check_file, "w") as file:
                        file.write(content[0:1000])   
                                
                   
def get_yahoo_history(upcoming_file,compare_file):
    # Open the CSV file and load it as a dictionary
    with open(upcoming_file, 'r') as f:
        reader = csv.DictReader(f)        
        gotten = list(reader)
    # Print the loaded data
    print(gotten)
    cwd = os.getcwd()
    file_list = os.listdir(cwd)
    for item in gotten:
        symbol = item["symbol"]
        date = item["date"]
        check_file=symbol+"-history.csv"
        if check_file in file_list:
            continue
        data = yf.download(symbol, period="5y", interval="1d").sort_index(ascending=False)
        data.columns = data.columns.get_level_values(0)  # Remove multi-index headers
        # Move "Open" to the second column and round all float values to 2 decimal places
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']].round(2)
        data.to_csv(symbol+'-history.csv', index_label='Date')
        print(symbol+'-history.csv'+" saved")
        print(gotten.index(item),len(gotten))
        time.sleep(2)
    #gen list
    compare = []
    for item in gotten:
        symbol = item["symbol"]
        print(symbol)
        load_file = symbol+"-history.csv"
        with open(load_file, 'r') as f:
            reader = csv.DictReader(f)        
            prices = list(reader)     
            #print(prices)
        print(load_file)
        index = gotten.index(item)
        #if index<55:
        #    continue
        with open(load_file, mode='r') as file:
            reader = csv.DictReader(file)  # Reads CSV as a list of dictionaries
            data = list(reader)
        try:
            price = float(data[0]["Close"])
        except:
            continue
        volume = float(data[0]["Volume"])
        volpri = int(price*volume)
        new = {}
        new["vol*pri"] = volpri
        new["symbol"] = symbol
        new["date"] = date
        print("new",new)
        compare.append(new)
    compare = sorted(compare, key=lambda x: float(x["vol*pri"]),reverse=True)
    print(compare)
    with open(compare_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=compare[0].keys())
        writer.writeheader()
        writer.writerows(compare)

def prices_around_earnings(match_file,cut_off):
    stock_list = csv_to_book(match_file)
    cwd = os.getcwd()
    edgar_folder = os.path.join(cwd,"sec-edgar-filings")          
    continue_pattern= []
    reverse_pattern=[]
    #con_rev={}
    con_rev=[]
    final_cr = []
    final_cr2 = []
    for specific in stock_list:
        print(specific)
        symbol = specific["symbol"]
        stock = specific["symbol"]
        print(symbol)
        print(stock_list.index(specific),len(stock_list))
        k8_dir = os.path.join(edgar_folder,stock,"8-K")  
        try:
            k8_list = os.listdir(k8_dir)
        except:
            continue
        earnings_dates = []
        for k8_code in k8_list:
            if "-25-" not in k8_code and "-24-" not in k8_code and "-23-" not in k8_code: 
                continue
            file_to_load = os.path.join(k8_dir,k8_code,"full-submission.txt")    
            with open(file_to_load, 'r') as file:
                content = file.read()
                if "Results of Operations and Financial Condition" in content and "Financial Statements and Exhibits" in content:
                    what_to_find = "FILED AS OF DATE:"
                    dates_start = content.find(what_to_find)
                    date_end = content.find("\n",dates_start)
                    date = content[dates_start:date_end]
                    earnings_dates.append(date)
        earnings_dates.sort()
        earnings_dates.reverse()
        earnings_dates=earnings_dates[0:8]
        earnings_dates.reverse()
        earnings_dates1 = earnings_dates
        earn_dates2 = []
        for date in earnings_dates1:
            new = date.replace("FILED AS OF DATE:","")
            new = new.replace("\t","")
            earn_dates2.append(new)
        dates_list = earn_dates2
        object_current_datetime = datetime.now()    
        list_prices = []
        prices_file = symbol + "-history.csv"
        with open(prices_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            list_prices = [row for row in csv_reader]   
        continue_list=  []
        reverse_list = []
        continue_dictionary= {}
        reverse_dictionary = {}
        more = {}
        stock_cr = []
        for specific_date in dates_list:
            print("specific_date",specific_date)
            days_surrounding = {}
            for day_prices in list_prices:
                try:
                    day_prices["Date"] = day_prices["Date"].replace("-","")
                except:
                    print("day_prices",day_prices)
                if specific_date in day_prices["Date"]:
                    index_before=list_prices.index(day_prices)+1
                    index_after=list_prices.index(day_prices)-1
                    day_before = list_prices[index_before]
                    day_listed = day_prices
                    day_after = list_prices[index_after]
                    max_vol = ""
                    vol_day_of = int(day_listed["Volume"])
                    vol_day_after = int(day_after["Volume"])                  
                    if vol_day_of>vol_day_after:
                        max_vol = day_listed
                    if vol_day_of<vol_day_after:
                        max_vol = day_after
                    days_surrounding["before"]=day_before
                    days_surrounding["day_of"]=day_listed
                    days_surrounding["after"]=day_after
            for key, day in days_surrounding.items():
                #print(key,day)
                if max_vol==day:
                    for key, out in days_surrounding.items():
                        print(symbol,key,out)
                    print("max_vol",max_vol)
                    get_close=""
                    if key=="after":
                        get_close = "day_of"
                    if key=="day_of":
                        get_close = "before"
                    close_day_before = float(days_surrounding[get_close]["Close"])
                    morning = float(day["Open"])
                    gap = round(float(((morning/close_day_before)-1)*100),2)
                    day_high = float(day["High"])
                    day_low = float(day["Low"])
                    same_direction=""
                    opposite_direction=""
                    if gap>0:
                        same_direction=day_high
                        opposite_direction=day_low
                    if gap<0:
                        same_direction=day_low
                        opposite_direction=day_high
                    if gap==0:
                        continue
                    percent_continue = abs(float(int(((same_direction/morning)-1)*10000)/100))
                    percent_reverse = abs(float(int(((opposite_direction/morning)-1)*10000)/100))
                    if percent_continue==0:
                        percent_continue=1
                    if percent_reverse==0:
                        percent_reverse=1
                    ratio_continue= abs(percent_continue/percent_reverse)
                    ratio_reverse= abs(percent_reverse/percent_continue)
                    ratio_continue= float(int(ratio_continue*100)/100)
                    ratio_reverse= float(int(ratio_reverse*100)/100)
                    new = {}
                    new["Date"]=day["Date"]
                    if ratio_continue>ratio_reverse:
                        new["Direction"]="C"
                        new["Amount"]=ratio_continue
                    if ratio_continue<ratio_reverse:
                        new["Direction"]="R"
                        new["Amount"]=ratio_reverse
                    if ratio_continue==ratio_reverse:
                        new["Direction"]="E"
                        new["Amount"]=ratio_continue
                    stock_cr.append(new)
        stock_cr.sort(key=lambda x: x["Amount"])
        direction = ""
        for item in stock_cr:
            direction=direction+item["Direction"]
            print(item)
        if len(stock_cr)==0:
            continue
        min_value=stock_cr[0]["Amount"]
        min2= int((min_value-1)*100)
        #if min2>cut_off:
        if min2>0: 
            new = {}
            new["symbol"]=symbol
            new["direction"]=direction
            new["ratio"]=min2
            print(specific)
            new["vol*pri"]=int(specific["vol*pri"])
            final_cr2.append(new)
        #abort, leave =="" if you just want it to run
        if symbol=="":
            sys.exit()
    final_cr2 = sorted(final_cr2,key=lambda x: x["vol*pri"])
    for item in final_cr2:
        print(item)    
        """
            final_cr.append([symbol,direction,min2])
    final_cr.sort(key=lambda x: x[1])
    for item in final_cr:
        item[2] = str(item[2])+"%"
    for item in final_cr:
        print(item)
        """
    
def specific_day(start_day,end_day, file_to_load):
    list = []
    with open(file_to_load, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(row)  # Add each row to the list
    correct_date = []
    from datetime import datetime, timedelta
    start_date_str = start_day
    end_date_str = end_day
    start_date_obj = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date_str, "%Y-%m-%d")
    for a,val in enumerate(list):
        if a==0:
            continue
        check_date_str = val[3]   
        check_date_obj = datetime.strptime(check_date_str, "%Y-%m-%d")
        if check_date_obj>=start_date_obj:
             if check_date_obj<=end_date_obj:
                correct_date.append(val)
    correct_date = correct_date[0:30]
    for a,val in enumerate(correct_date):
        print(val)    

finnhub_folder = "finnhub_earnings"
upcoming_file = "0upcoming_earnings.csv"
compare_file = "0compare.csv"
google_vp_file = "0vp_google_data.csv"
history_header = [["date","open","high","low","close","volume"]]
match_file = "0match.csv"
finnhub_start = "2025-04-01"
finnhub_end = "2025-05-01"
finnhub_file = os.path.join(finnhub_folder,finnhub_start+"."+finnhub_end+".json")
file_master = "0all_stocks2.csv"
cut_off=100

#get_finnhub_earnings(finnhub_folder,finnhub_start,finnhub_end)
#stocks_from_finnhub_data(finnhub_file,upcoming_file)
most_vol_pri(300,upcoming_file,file_master)
get_yahoo_history(upcoming_file,compare_file)
get_sec_earn_dates(compare_file)
prices_around_earnings(compare_file,cut_off)
"""
#specific_day(start_date,end_date, match_file)
"""
#push codespace to github repo
#git add . && git commit -m "Replace all files with Codespaces files" && git push --progress origin main  # or master if your default branch is master
"""
| **Economic Data Release**       | **API to Access the Data**                                                                                   |
|----------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Gross Domestic Product (GDP)** | [FRED API](https://fred.stlouisfed.org/docs/api/fred/) (Federal Reserve Economic Data)                         |
| **Consumer Price Index (CPI)**   | [BLS API](https://www.bls.gov/developers/) (Bureau of Labor Statistics)                                        |
| **Non-Farm Payrolls (NFP)**      | [BLS API](https://www.bls.gov/developers/) (Bureau of Labor Statistics)                                        |
| **Retail Sales**                 | [U.S. Census Bureau API](https://www.census.gov/data/developers/guidance/api-user-guide.html)                 |
| **Federal Reserve Statements**   | [Federal Reserve API](https://www.federalreserve.gov/data/releaseschedule.htm) (Federal Reserve)                |
| **Trade Balance**                | [BEA API](https://www.bea.gov/data/developers) (Bureau of Economic Analysis)                                    |
"""