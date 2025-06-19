from tkinter import *

# initializing global variables
counter = 0 # tracking number of expenses added by user
frequency = None # storing the frequency of income
monthly_income = None # storing the total income in a month
salary = None # storing the amount earned in a particular time period
expense_amounts_var = [] # storing vars of expense amounts
expense_categories_var = [] # storing vars of expense categories
expense_amounts = [] # the actual value of expense amounts entered by the user
expense_categories = [] # the actual value of expense categories entered by the user
total_expense = 0.0 # storing the total expenses

# initializing the window
window = Tk()
window.geometry("500x500")
window.title("EXPENSE TRACKER")

# Creating the first window
# intro message
welcome_label = Label(window, text = "WELCOME TO YOUR EXPENSE TRACKER!", font = ("Times New Roman", 16, "bold"), fg = "black", justify = CENTER)
welcome_label.grid(row = 0, column = 0, sticky = NSEW, pady = 25)

# asking user to input their income
income_label = Label(window, text = "Enter your income in US Dollars:")
income_label.grid(row = 1, column = 0, sticky = W)

# entry space
entry_salary = Entry(window, width = 50)
entry_salary.grid(row = 2, column = 0, sticky = W, pady = 5)

# a label to display error message if wrong data type is used
error_label_1 = Label(window, text = "")
error_label_1.grid(row = 3, column = 0, sticky = W)

# asking user to input their frequency of income
frequency_label = Label(window, text = "Frequency of income:")
frequency_label.grid(row = 4, column = 0, sticky = W, pady = 5)

# creating an option menu to choose the frequency
frequency_options = ["weekly", "biweekly", "monthly", "yearly", "other"]
frequency_variable = StringVar(window) # storing the user's choice as a variable
frequency_variable.set(frequency_options[0]) # adding the default value of frequency to be weekly
frequency_optionmenu = OptionMenu(window, frequency_variable, *frequency_options)
frequency_optionmenu.grid(row = 5, column = 0, sticky = W)

# a label to maintain space
space_label = Label(window, text = "")
space_label.grid(row = 6, column = 0)

# a label to ask for the reporting period of expense
month_label = Label(window, text = "Reporting Month:")
month_label.grid(row = 7, column = 0, sticky = W, pady = 5)

# creating an option menu to choose the month
month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = StringVar(window)
month.set(month_options[0])
month_optionmenu = OptionMenu(window, month, *month_options)
month_optionmenu.grid(row = 8, column = 0, sticky = W)

# calcualtions from the first window and checking whether the input value is valid or not
def calculations_1():
    # storing the user's input of income as a variable
    salary_input = entry_salary.get()
    global frequency, monthly_income, salary 

    # runs the code if the value is numerical
    try:
        salary = float(salary_input)
        error_label_1.config(text="") # removing any error message displayed earlier
        
        # checking if the value is positive
        if salary > 0:
            # calcualting the monthly salary and storing the frequency
            if frequency_variable.get() == "weekly":
                frequency = "week"
                monthly_income = salary * 4
            
            elif frequency_variable.get() == "biweekly":
                frequency = "two weeks"
                monthly_income = salary * 2
            
            elif frequency_variable.get() == "monthly":
                frequency = "month"
                monthly_income = salary
            
            elif frequency_variable.get() == "yearly":
                frequency = "year"
                monthly_income = salary / 12
            
            else:
                monthly_income = 0.0
                frequency = ""

            return True
        
        # if negative show the error message
        else:
            error_label_1.config(text="Please enter a positive numeric salary.", fg="red")
            return False

    # displays error message if the value is non-nuemrical
    except ValueError:
        error_label_1.config(text="Please enter a valid numeric salary.", fg="red")
        return False

# making a new window (window2) to be displayed after next is pressed
def expense_page():
    # clears all the previous widgets
    clear_screen(window)

    # the list of options of expense categories for the user
    expense_options = ["food", "health", "transportation", "clothing", "entertainment", "rent", "utilities", "others"]

    # a label to display error message if wrong data type is used
    error_label_2 = Label(window, text = "")
    error_label_2.grid(row = 34, column = 0, sticky = W)

    # a function to run when adding new expenses
    def add_expense():
        # a variable to keep count of number of expenses added
        global counter

        # to not let users have more expenses than 8
        if (counter < 8):
            # a label that asks the category of expense
            category_label = Label(window, text = f"Expense category {counter + 1}:")
            category_label.grid(row = (counter * 4) + 1, column = 0, sticky = W)

            # the optionmenu for categories of expense
            expense = StringVar(window) # stores the user's choice
            expense_optionmenu = OptionMenu(window, expense, *expense_options)
            expense_categories_var.append(expense)
            expense_optionmenu.grid(row = (counter * 4) + 2, column = 0, sticky = W, pady = 5)

            # a label that asks amount of expense
            amount_label = Label(window, text = f"Expenditure amount {counter + 1} monthly (USD):")
            amount_label.grid(row = (counter * 4) + 3, column = 0, sticky = W)

            # an entry to enter the expense amount
            entry_expenditure = Entry(window, width = 50)
            expense_amounts_var.append(entry_expenditure)
            entry_expenditure.grid(row = (counter * 4) + 4, column = 0, sticky = W)

            # increasing the counter after a new addition of expense
            counter += 1

            # giving a new position for the buttons
            add_expense_button.grid(row = (counter * 4) + 1, column = 0, sticky = W, pady = 10) 
            next_button_2.grid(row = (counter * 4) + 2, column = 1, sticky = E) 

        else:
            # an error message if more than 8 expenses added
            error_label_2.config(text = "You cannot add more than 8 expenses.", fg = "red")
    
    # a button that gives option to add more expenses
    add_expense_button = Button(window, text = "Add a new expense", command = add_expense)

    # a new window to show the final assessment of the income and expeses
    def result_page():
        # first clears all the previous widgets
        clear_screen(window)

        # title at the top of the screen
        summary_label = Label(window, text = "YOUR FINANCIAL SNAPSHOT: A SUMMARY", font = ("Times New Roman", 14, "bold"), fg = "red")
        summary_label.grid(row = 0, column = 0, pady = 5)

        # some intro information
        intro_label = Label(window, text = "Here's a breakdown of your financial activity for this period, helping you\nunderstand where your money went and what your current financial standing is.", \
                         font = ("Times New Roman", 12), justify = LEFT)
        intro_label.grid(row = 1, column = 0, pady = 5, sticky = W)

        # sub heading for income overview
        income_overview_label = Label(window, text = f"Income Overview of {month.get()}", font = ("Times New Roman", 14, "italic"), fg = "blue", justify = LEFT)
        income_overview_label.grid(row = 2, column = 0, sticky = W)

        # income information
        income_label = Label(window, text = income_result(), font = ("Times New Roman", 12), justify = LEFT)
        income_label.grid(row = 3, column = 0, sticky = W)

        # sub heading for expenditure breakdown
        expenditure_breakdown_label = Label(window, text = f"Expenditure Breakdown of {month.get()}", font = ("Times New Roman", 14, "italic"), fg = "blue", justify = LEFT)
        expenditure_breakdown_label.grid(row = 4, column = 0, sticky = W)

        # expense information
        expenditure_label = Label(window, text = expenditure_result(), font = ("Times New Roman", 12), justify = LEFT)
        expenditure_label.grid(row = 5, column = 0, sticky = W)

        # sub heading for financial position
        financial_position_label = Label(window, text = f"Net Financial Position of {month.get()}", font = ("Times New Roman", 14, "italic"), fg = "blue", justify = LEFT)
        financial_position_label.grid(row = 6, column = 0, sticky = W)

        # final financial report
        report_label = Label(window, text = final_result(), font = ("Times New Roman", 12), justify = LEFT)
        report_label.grid(row = 7, column = 0, sticky = W)

    # checking whether the input value is valid or not
    def calculations_2():
        # clearing any previous values
        error_label_2.config(text = "")
        expense_amounts.clear()
        expense_categories.clear()

        for i in range(len(expense_categories_var)):
            # storing every var's actual values in the list
            amount_str = expense_amounts_var[i].get()
            category = expense_categories_var[i].get()

            try:
                amount = float(amount_str)
                # checking if the value is positive or not
                if amount > 0:
                    expense_amounts.append(amount)
                    expense_categories.append(category)
                # else show the error message
                else:
                    error_label_2.config(text = "Please enter a valid positive numeric value", fg = "red")
                    return False

            except ValueError:
                error_label_2.config(text = "Please enter a valid positive numeric value", fg = "red")
                return False
            
        return True

    # a command that checks if the user input is numerical via calculation_2 function
    # And forms the third window
    def next_command2():
        if calculations_2():
            result_page()

    # a next button to go to the final summary window
    next_button_2 = Button(window, text = "Next", justify = RIGHT, command = next_command2)

    # running the function add_expense to have one entry of expenditure after the window runs
    add_expense()
    
# a command that checks if the user input is numerical via calculation_1 function
# And forms the second window
def next_command():
    if calculations_1():
            expense_page()

# a next button to go to the second window
next_button_1 = Button(window, text = "Next", justify = RIGHT, command = next_command)
next_button_1.grid(row = 10, column = 1, sticky = E)

# function to create the text of income overview
def income_result():
    assessment = f"""Total Income in {frequency}: ${salary}
Average Monthly Income: ${monthly_income}
"""
    return assessment

# # calcualtions from the second window and checking whether the value input is valid or not
def expenditure_result():
    global total_expense
    total_expense = sum(expense_amounts) # adding all expenses

    assessment = f"""Total Expenses: ${total_expense}
Top 3 Highest Spending Categories:"""
    
    # sorting both the expense amount and category in ascending order using selection sort 
    # to keep track of category and the amount together
    for i in range(len(expense_amounts)):
        min_pos = i
        for j in range(i+1, len(expense_amounts)):
            if expense_amounts[min_pos] > expense_amounts[j]:
                min_pos = j

        temp = expense_amounts[min_pos]
        expense_amounts[min_pos] = expense_amounts[i]
        expense_amounts[i] = temp

        # changing the index of category associated with the amount
        temp = expense_categories[min_pos] 
        expense_categories[min_pos] = expense_categories[i]
        expense_categories[i] = temp

    # if the expenses category are more than three then only choosing the last 
    # three categories as the highest expenses from the sorted list
    if len(expense_amounts) >= 3:
        for i in range(len(expense_amounts)-1, len(expense_amounts) - 4, -1):
            assessment += f"""
\tCategory {len(expense_amounts)-i}:
                {expense_categories[i]} = ${expense_amounts[i]}
"""
    # else using all the available categories
    else:
        for i in range(len(expense_amounts)-1, -1, -1):
            assessment += f"""
\tCategory {len(expense_amounts)-i}:
                {expense_categories[i]} = ${expense_amounts[i]}
"""

    return assessment

# a function to create the text of net financial position
def final_result():
    result = monthly_income - total_expense

    if result > 0:
        assessment = f"""Net Savings: ${result}
Interpretation:
You saved ${result} this period! """
    elif result < 0:
        assessment = f"""Net Deficit: ${(result) * -1 }
Interpretation:
You spend ${result * -1} more this period! """
    else:
        assessment = f"You are breakeven!!!"

    return assessment

# function to clear all the widgets from the frame
def clear_screen(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# to destroy the window when escape key is pressed
def escape_function (event = None):
    window.destroy() 
window.bind('<Escape>', escape_function)

window.mainloop()
