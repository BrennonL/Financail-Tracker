from My_db import My_db
import datetime
import pandas as pd

def Display_spacing():
    '''
    :fun: Simply prints 3 spaces then some underlines then 3 more spaces. Like
        the following



        _______________________________________




    '''
    print()
    print()
    print()
    print("______________________________________")
    print()
    print()
    print()    

def Insert_row(curr_db):
    '''
    :arg curr_db: My_db class
    :fun: Gets the user info for a new row and calls the function add_row()
        from the My_db class or the curr_db object.
    '''
    transaction_type = input("Type: ")
    amount = input("Amount: ")
    note = input("Note: ")
    curr_db.add_row(transaction_type, amount, note)

def View_Month(curr_db):
    '''
    :arg curr_db: My_db class
    :fun: Gets the month from the user in a 2 digit format like 06 for June.
        Then it calls the display_month() function from the My_db class or
        the curr_db object.
    '''
    month = input("SELECT MONTH: ")
    curr_db.display_month(month)
    Display_spacing()

def Delete_row(curr_db):
    '''
    :arg curr_db: My_db class
    :fun: Gets the index for the row that the user wants to delete. Then it
        calls the delete_row() function from the My_db class or the curr_db 
        object.
    '''
    index = int(input("Index: "))
    curr_db.delete_row(index)

def Start_program():
    '''
    :fun: Starts a new instance of the My_db() class with the current date.
        Then it gets the users input as far as which action they would like to
        do. They will get the following prompt:

            What do you want to do?
            Q: quit
            I: insert new row
            VM: view months finances
            VY: View year finances
            D: delete a row
            INPUT:
        
        If they put 'q' or 'Q' then end the program. IF they put 'I' or 'i' 
        call the Insert_row() function. If they put 'vm', 'Vm', 'VM', or 'vM'
        call the View_Month() function. IF they put 'D' or 'd' then call
        Delete_row() function. If they put 'vy', 'Vy', 'VY', or 'vY' call the
        View_Year() function.
    '''
    #TODO--Split this up into separate functions to make it easier to read 
    date = datetime.date.today()
    curr_db = My_db(date)
    power_on = True
    while power_on:
        print("What do you want to do?")
        print("Q: quit")
        print("I: insert new row")
        print("VM: view months finances")
        print("VY: View year finances")
        print("D: delete a row")
        user_choice = input("INPUT: ")
        Display_spacing()
        if user_choice.upper() == "Q":
            power_on = False
            break
        
        elif user_choice.upper() == "I":
            Insert_row(curr_db)

        elif user_choice.upper() == "VY":
            print("________View year needs working on___________")

        elif user_choice.upper() == "D":
            Delete_row(curr_db)

        elif user_choice.upper() == "VM":
            View_Month(curr_db)
        else:
            print()
            print("PLEASE USE A VALID INPUT")
            print()
    curr_db.put_back_csv()

def main():
        Start_program()


if __name__ == "__main__":
    main()