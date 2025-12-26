import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

print("Welcome to My New & Last Project , Expense Tracker")
print("==================================================")

try:
    data = pd.read_csv("expenses.csv")
    data["Date"] = pd.to_datetime(data["Date"])
except FileNotFoundError:
    data = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])


class ExpenseTracker:

    def __init__(self, dataframe):
        self.data = dataframe
        if not self.data.empty:
            self.data["Date"] = pd.to_datetime(self.data["Date"])


    def input_expense(self, date, amount, category, description):

        new_row = {
            "Date": pd.to_datetime(date),
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        self.data.loc[len(self.data)] = new_row

    def take_input(self):

        while True:
            date = input("Enter date (YYYY-MM-DD) : ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format")

        while True:
            try:
                amount = float(input("Enter the Amount : "))
                if amount > 0:
                    break
                else:
                    print("Amount must be positive")
            except ValueError:
                print("Invalid Amount")

        category = input("Enter the Category : ")
        description = input("Enter the Description : ")

        return date, amount, category, description


    def analysis_metrics(self):

        total = self.data["Amount"].sum()
        average = self.data["Amount"].mean()
        category_total = self.data.groupby("Category")["Amount"].sum()

        print("Total Expense Amount :", total)
        print("Average Expense Amount :", average)
        print("Category-Wise Expenses :")
        print(category_total)
        print(self.data.groupby("Category")["Amount"].sum())


    def filter_dataset(self, category):

        filtered = self.data[self.data["Category"] == category]

        if filtered.empty:
            print("No data found for this category")
        else:
            print(filtered)


    def bar_chart(self):

        if self.data.empty:
            print("No data to plot")
            return
        
          
        self.data.groupby("Category")["Amount"].sum().plot(kind="bar")
        plt.title("Expenses by Category")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.show()

    def line_chart(self):

        if self.data.empty:
            print("No data to plot")
            return
        
        
        self.data.groupby("Date")["Amount"].sum().plot()
        plt.title("Expense Trend Over Time")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.show()

    def pie_chart(self):

        if self.data.empty:
            print("No data to plot")
            return
        
          
        self.data.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Expense Distribution")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    def histogram(self):

        if self.data.empty:
            print("No data to plot")
            return
        

        plt.hist(self.data["Amount"], bins = 5)
        plt.title("Expense Amount Distribution")
        plt.xlabel("Amount")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()




E_File = ExpenseTracker(data)

while True:

    print("Enter 1 to Take Input Expense.")
    print("Enter 2 to Analysis & Metrics.")
    print("Enetr 3 to Filter Dataset.")
    print("Enter 4 to Visualize Data(📉📊📈).")
    print("Enter 0 to Exit.")

    try:
        Choice = int(input("Enter your choice : "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if Choice == 1:

        print()
        date, amount, category, description = E_File.take_input()
        E_File.input_expense(date, amount, category, description)

    elif Choice == 2:
        E_File.analysis_metrics()

    elif Choice == 3:

        print()
        cat = input("Enter category to filter : ")
        E_File.filter_dataset(cat)

    elif Choice == 4:

        print()
        print("Enter 1 to Bar Chart.")
        print("Enetr 2 to Line Chart.")
        print("Enetr 3 to Pie Chart.")
        print("Enetr 4 to Histogram.")
        print("Enetr 0  to Go-Back to Main-Menu.")

        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("You Entered Invalid choice 🥺")
            continue

        if choice == 1:

            print()
            E_File.bar_chart()

        elif choice == 2:

            print()
            E_File.line_chart()

        elif choice == 3:

            print()
            E_File.pie_chart()

        elif choice == 4:

            print()
            E_File.histogram()

        elif choice == 0:
            continue

    elif Choice == 0:

        print()
        print("Thanks for visiting My Project")
        break

    else:
        print("Invalid Choice")