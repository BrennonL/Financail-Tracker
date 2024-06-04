from My_db import My_db
import datetime
import pandas as pd


def Insert_row(curr_db):
    transaction_type = input("Type: ")
    amount = input("Amount: ")
    note = input("Note: ")
    curr_db.add_row(transaction_type, amount, note)

def Start_program():
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
        if user_choice.upper() == "Q":
            power_on = False
            break
        
        elif user_choice.upper() == "I":
            Insert_row(curr_db)

        elif user_choice.upper() == "VY":
            print("________View year needs working on___________")

        elif user_choice.upper() == "D":
            index = input("Index: ")
            curr_db.delete_row(index)

        elif user_choice.upper() == "VM":
            print("________View month needs working on__________")
            curr_db.display_month()
        else:
            print()
            print("PLEASE USE A VALID INPUT")
            print()
    curr_db.put_back_csv()

def main():
        Start_program()


if __name__ == "__main__":
    main()