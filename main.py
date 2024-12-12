import pandas as pd

class Item:
    def buy(self, item_id):
        """ Reduces the inventory quantity by one"""
        pass

class Receipt:
    def generate(self, item_id):
        """ Generates a reciept for an item """
        pass


df = pd.read_csv("inventory.csv")
print(df)

purchased_item = input("Choose an item to buy: ")
item = Item()
item.buy(purchased_item)

receipt = Receipt()
receipt.generate(purchased_item)