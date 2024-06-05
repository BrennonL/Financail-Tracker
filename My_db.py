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
            and converts it to a pandas DataFrame. It then returns this DataFrame.
        '''
        if os.path.exists(self.path):
            my_df = pd.read_csv(self.path)
        else:
            my_df = pd.DataFrame(data=None, columns=["Date", "Type", "Amount", "Note"])            
        return my_df
    

    def display_month(self, month):
        '''
        :arg month: int (should be 2 integers representing a month)
        :fun: Uses a regex and df.Date.str.match() function to query the months
            that are passed into the function from the df.
        '''
        regex = f"{self.year}-{month}-[0-9][0-9]"
        print(self.df[self.df.Date.str.match(regex)])

    def display_year(self, year):
        display(self.df)
        

    def plot_month(self, mon):
        ...

    def plot_year(self, year):
        ...
    
    def add_row(self, tran_type, amount, note):
        '''
        :arg tran_type: str (transaction type)
        :arg amount: int
        :arg note: str
        :fun: Takes the following input and creates a new row in the self.df
            using the df.append() function.
        '''
        new_row = {"Date" : self.date, "Type": tran_type, "Amount": amount, "Note": note}
        #TODO -- Change this to Concat instead of append
        self.df = self.df.append(new_row, ignore_index = True)
    
    def delete_row(self, this_index):
        '''
        :arg this_index: int
        :fun: Uses the parameter this_index to delete a row at the specified 
            index on the self.df. For example it 0 was passed in, the first row
            on the self.df would be deleted.
        '''
        self.df = self.df.drop(self.df.index[this_index])

    def put_back_csv(self):
        '''
        :fun: Save the self.df as a CSV file in the files folder. If the folder
            doesn't exist it should create it.
        '''
        self.df.to_csv( f".\\files\\{self.year}.csv", sep=",", index_label=None, index=None )