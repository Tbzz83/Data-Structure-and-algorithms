# Simple exercise working with an array
expenses = ["January", 2200, "February", 2350, "March", 2600, "April", 2130, "May", 2190, "August", 2000]

def how_much_extra(month1, month2):
    solution = 0
    month1_index = expenses.index(month1) + 1
    month2_index = expenses.index(month2) + 1

    solution = expenses[month1_index] - expenses[month2_index]
    print(solution)

def first_quarter_expenses():
    jan_index = expenses.index("January") + 1
    feb_index = expenses.index("February") + 1
    march_index = expenses.index("March") + 1
    solution = expenses[jan_index] + expenses[feb_index] + expenses[march_index]
    print(solution)

def spent_two_thousand():
    if 2000 in expenses:
        print("Exactly $2000 was spent in", expenses[expenses.index(2000) - 1])

    else:
        print("Exactly $2000 was not spent in any month")

def add_month(month, val):
    expenses.append(month)
    expenses.append(val)

def refund(month, ref_amnt):
    new_val = expenses[expenses.index(month) + 1] - ref_amnt
    expenses.pop(expenses.index(month) + 1)
    expenses.insert(expenses.index(month) + 1, new_val)


how_much_extra("February", "January")
first_quarter_expenses()
spent_two_thousand()
add_month("July", 2349)
print(expenses)
refund("April", 200)
print(expenses)
