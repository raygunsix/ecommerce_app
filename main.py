import pandas as pd
from fpdf import FPDF

df = pd.read_csv("inventory.csv")

class Item:
    def __init__(self, item_id):
        self.item_id = int(item_id)

    def buy(self):
        """ Reduces the inventory quantity by one"""
        quantity = df.loc[df["id"] == self.item_id, "in stock"].squeeze()
        df.loc[df["id"] == self.item_id, "in stock"] = quantity - 1
        df.to_csv("inventory.csv", index=False)

    def available(self):
        """ Checks to see if an item is in stock """
        in_stock = df.loc[df["id"] == self.item_id, "in stock"].squeeze()
        if in_stock > 0:
            return True
        else:
            return False
    

class Receipt:
    def __init__(self, item_id, item_name, item_price):
        self.item_id = str(item_id)
        self.item_name = str(item_name)
        self.item_price = str(item_price)

    def generate(self):
        """ Generates a reciept for an item """

        # Generate pdf    
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.item_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.item_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.item_price}", ln=1)

        pdf.output("receipt.pdf")


print(df)

purchased_item = input("Choose an item to buy: ")
item = Item(purchased_item)

if item.available():
    item.buy()
    name, price = df.loc[df["id"] == int(purchased_item), ["name", "price"]].squeeze()
    receipt = Receipt(purchased_item, name, price)
    receipt.generate()
else:
    print("Sorry, that item is out of stock")
