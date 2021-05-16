import os
import sys
import pandas as pd
from bs4 import BeautifulSoup as bs


def retrieve():
    path = 'table.html'
    
    # empty list
    data = []
    
    # for getting the header from the HTML file
    list_header = []
    soup = bs(open(path),'html.parser')
    header = soup.find_all("table")[0].find("tr")
    
    for items in header:
        try:
            list_header.append(items.get_text())
        except:
            continue
    
    # for getting the data 
    HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
    
    for element in HTML_data:
        sub_data = []
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except:
                continue
        data.append(sub_data)
    
    # Storing the data into Pandas DataFrame 
    dataFrame = pd.DataFrame(data = data, columns = list_header)
    
    # Converting Pandas DataFrame into CSV file
    dataFrame.to_csv('rates.csv')

def store(): #NOTE: ALWAYS USE A ARRAY TO STORE THE RETURNED DATA
    #reading a csv file with pandas
    data_frame = pd.read_csv("rates.csv")   
    
    #give the datatype of a pandas object
    type(data_frame) 
    
    #this function gives us a brief view of the data.
    data_frame.head
    
    #converting pandas dataframe to a numpy array.
    arr = data_frame.to_numpy()
    #print(arr)

    return arr


#test site
#retrieve()
#store()