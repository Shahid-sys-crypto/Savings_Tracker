import matplotlib.pyplot as plt
from collections import defaultdict

expenses=[]

def set_savings_goal():
    goal=float(input("enter the monthly savings goal"))
    print(f"your savings goal is set to ${goal:.2f}")
    return goal

def add_income():
    income=float(input("enter your income amount"))
    print(f"income of ${income:.2f} added")
    return income

def add_expense():
    category=input("enter expense category").capitalize()
    amount=float(input("enter expense amount"))
    expenses.append({"category":category,"amount":amount})
    print(f"expense of ${amount:.2f} added under {category}")

def view_expenses_by_category():
    category_totals=defaultdict(float)
    for expense in expenses:
        category_totals[expense["category"]]+=expense["amount"]
    print("\nexpenses by category:")
    for category,total in category_totals.items():
        print(f"{category} : {total:.2f}")

def calculate_remaining_budget(income,expenses):
    total_expenses=sum(expense["amount"] for expense in expenses)
    remaining_budget=income-total_expenses
    print(f"total expenses : ${total_expenses:.2f}")
    print(f"remaining budget : ${remaining_budget:.2f}")
    return remaining_budget

def check_savings_goal(remaining,goal):
    if remaining>goal:
        print(f"congratulations! you have met your savings goal with ${remaining-goal:.2f} extra")
    else:
        print(f"you are ${goal-remaining:.2f} away from your savings goal")

def plot_expenses():
    category_totals=defaultdict(float)
    for expense in expenses:
        category_totals[expense["category"]]+=expense["amount"]
    labels=category_totals.keys()
    sizes=category_totals.values()
    plt.pie(sizes,labels=labels,autopct="%1.1f%%")
    plt.title("expense distribution")
    plt.show()

def main():
    goal=set_savings_goal()
    income=add_income()
    while True:
        print("1.add expense")
        print("2 view expense by category")
        print("3. calculate remaining budget")
        print("4. check savings goal")
        print("5.plot expenses")
        print("6.exit")
        choice=int(input("enter your choice"))
        if choice==1:
            add_expense()
        elif choice==2:
            view_expenses_by_category()
        elif choice==3:
            calculate_remaining_budget(income,expenses)
        elif choice==4:
            remaining=calculate_remaining_budget(income,expenses)
            check_savings_goal(remaining,goal)
        elif choice==5:
            plot_expenses()
        elif choice==6:
            print("exiting the budget planner")
            break
