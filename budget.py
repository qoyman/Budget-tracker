'''Track Income & Expenses:

Allow users to input income and categorize expenses (e.g., rent, groceries, utilities, etc.).
Store these as variables and update them regularly.
Use Data Types & Variables:

Use appropriate data types for different inputs (e.g., floats for income/expenses, strings for categories).
Conditionals:

Ensure budget limits are not exceeded and warn users if they are spending too much in certain categories.
Offer a comparison if monthly spending exceeds income.
Functions:

Create modular functions for adding income, recording expenses, and viewing a summary of finances.
Use built-in functions like sum() for total spending.
Lists, Dictionaries, Tuples:

Store transactions using a dictionary (category as key, amount as value).
Keep track of past expenses with a list, where each is a tuple (category, amount, date).
Exceptions:

Handle errors gracefully, such as invalid input types (e.g., entering a string when a number is expected).'''

'''category = input('\n Enter the expense category (e.g.  grocries, rent): ')
expense = float(input('enter the expense amount: '))

thedict = {
    'bobo':'hello',
    'me':'yins'
}

thedict.update({category: expense})

print(thedict)'''

Category = None
Expense = 0
income = 0

thisdict =	{
  "Rent: ":30,
  "temp" :12
}

def add_income():
    global income
    
    while True:
        try:  
            tempIncome = input('enter the amount of income: ')
            income += float(tempIncome)
            print(f'income of {income} added successfully!')
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            addIncome()

    my_function()    

def add_expense():
    global Category
    global Expense
    
    while True:
        try:
            Category = input("Enter the expense category (e.g., groceries, rent): ")

            if Category.isalpha():
                break
            else:
                print("to value error")               
        except ValueError:
            print("Invalid input! Please enter a string with only letters.")
            #Category = input('Enter the expense category (e.g.  grocries, rent): ') 

    while True:
        try:
            tempExpence = input('Enter the expense amount: ')
            Expense = float(tempExpence)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print(f'expense of {Expense} added to {Category}')
    
    thisdict.update({Category: Expense})
    print(thisdict)     

    my_function ()  
   
    

def summary():
    print("---- Personal Budget Tracker ----")
    print(f"Total income: {income} ")
    print(f"Total expenses: {Expense}")
    print("\n--Expense by category:")
    for x, y in thisdict.items():
        print(f'{x}: {y}')
        
    spent = sum(thisdict.values())
    
    dif = spent - income
    
    if spent >  income:   
        print(f'you are spending {dif} over the budget')
    else:
        print()

    my_function()



def my_function():
    print("\n\n ---- Personal Budget Tracker ----")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

    while True:
        try:
            othervaries = input("Enter your choice(1-4): ")
            varies = int(othervaries)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if varies == 1 :
        add_income()
    elif varies == 2 :
        add_expense()
    elif varies == 3 :
        summary()
    elif varies == 4 :
        print("Exiting the program, GOODBYE!")
    else:
        print('\ninvalid option')
        my_function() 

my_function()
    