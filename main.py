import pandas as pd
from fpdf import FPDF

class Item:
    def buy(self, item_id):
        """ Reduces the inventory quantity by one"""
        pass

class Receipt:
    def __init__(self, item_id, item_name, item_price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price

        print(self.item_id)

    def generate(self):
        """ Generates a reciept for an item """

        # Generate pdf    
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{str(self.item_id)}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.item_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {str(self.item_price)}", ln=1)

        pdf.output("receipt.pdf")

df = pd.read_csv("inventory.csv", dtype=str)
print(df)

purchased_item = input("Choose an item to buy: ")
item = Item()
item.buy(purchased_item)

row = df.loc[df["id"] == purchased_item, ["id", "name", "price"]].values[0]
receipt = Receipt(row[0], row[1], row[2])
receipt.generate()
