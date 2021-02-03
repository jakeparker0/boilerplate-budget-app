import os, sys


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.expense = 0
        self.income = 0

    def __str__(self):
        out = ""
        stars = (30 - len(self.name))//2
        out += "*"*stars + self.name + "*"*stars + '\n'
        for trans in self.ledger:
            d = trans["description"]
            line = ""
            num = "{:.2f}".format(trans["amount"])
            if len(d) > 23:
                line += d[:23] + " " + num + '\n'
            else:
                line += d + num.rjust(23) + '\n'
            out += line

        out += "Total: " + "{:.2f}".format(self.get_balance())
        return out

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description" : description})
        self.income += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.expense += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.income - self.expense

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

def create_spend_chart(categories):
    total = 0
    for c in categories:
        total += c.expense
    out = "Percentage spent by category\n"
    percentages = []
    for c in categories:
        percentages.append((c.name, ((c.expense/total)*100)//10))

    for i in range(11):
        line = (str((10 - i)*10) + "|").rjust(4) + ' '
        for x in percentages:
            if x[1] >= (10-i):
                line += "o"
            else:
                line += " "
            line += "  "
        out += line + '\n'

    out += " "*4 + "-"*((3 * len(categories)) + 1) + '\n'

    names = [x[0] for x in percentages]
    max_length = max(map(len, names))
    for i in range(max_length):
        line = " "*4
        for n in names:
            if i < len(n):
                line += " " + n[i] + " "
            else:
                line += "   "
        out += line + ' '
        if i != max_length -1:
            out += '\n'

    return out








