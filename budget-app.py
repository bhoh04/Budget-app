class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23]
            amount = format(item["amount"], ".2f")
            total += item["amount"]
            items += f"{description:<23}{amount:>7}\n"
        total = format(total, ".2f")
        return title + items + "Total: " + str(total)


def create_spend_chart(categories):
    withdrawals = [sum(item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories]
    total_spent = sum(withdrawals)
    percentages = [(withdrawal / total_spent) * 100 for withdrawal in withdrawals]
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    category_names = [category.name for category in categories]
    max_name_length = max(len(name) for name in category_names)
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"
    return chart


# Example usage:
food_category = Category("Food")
clothing_category = Category("Clothing")
auto_category = Category("Auto")
categories = [food_category, clothing_category, auto_category]

food_category.deposit(1000, "Initial deposit")
food_category.withdraw(100, "Groceries")
clothing_category.withdraw(200, "Shoes")
auto_category.withdraw(50, "Gas")

print(create_spend_chart(categories))

