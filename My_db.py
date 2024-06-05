import datetime
import os
import pandas as pd
from IPython.display import display
from pandas import plotting as plt

class My_db:
    def __init__(self, curr_date) -> None:
        self.date = curr_date
        self.year = curr_date.year
        self.path = f"files/{self.year}.csv"
        self.df = self.get_csv()


    def get_csv(self) -> pd.DataFrame:
        '''
        :fun: Converts the pre-existing dataset in csv file (corresponding with the year)
            and converts it to a pandas Dataframe.
        '''
        #! Self reading CSV
        # if os.path.exists(self.path):
        #     my_df = pd.DataFrame(data=None, columns=["Date", "Type", "Amount", "Note"])
        #     with open(self.path, "r") as year_file:
        #         for line in year_file:
        #             data = line.split(', ')
        #             new_row = {"Data" : data[0], "Type": data[1], "Amount": data[2], "Note": data[3]}
        #             my_df = my_df.append(new_row, ignore_index = True)
        #! With the Pandas reading CSV
        if os.path.exists(self.path):
            my_df = pd.read_csv(self.path)
        else:
            my_df = pd.DataFrame(data=None, columns=["Date", "Type", "Amount", "Note"])            
        return my_df
    

    def display_month(self, month):
        regex = f"{self.year}-{month}-[0-9][0-9]"
        print(self.df[self.df.Date.str.match(regex)])

    def display_year(self, year):
        display(self.df)
        

    def plot_month(self, mon):
        ...

    def plot_year(self, year):
        ...
    
    def add_row(self, tran_type, amount, note):
        new_row = {"Date" : self.date, "Type": tran_type, "Amount": amount, "Note": note}
        #TODO -- Change this to Concat instead of append
        self.df = self.df.append(new_row, ignore_index = True)
    
    def delete_row(self, this_index):
        self.df = self.df.drop(self.df.index[this_index])

    def put_back_csv(self):
        ''' This will put the df back into the csv file'''
        self.df.to_csv( f".\\files\\{self.year}.csv", sep=",", index_label=None, index=None )