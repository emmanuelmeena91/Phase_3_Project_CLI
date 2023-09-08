from database import init_db
from user import User
from shopping_list import ShoppingList
from item import Item

def display_menu():
    print("1. Create a new shopping list")
    print("2. Add item to a shopping list")
    print("3. Remove item from a shopping list")
    print("4. Display all shopping lists")
    print("5. Exit")

def create_shopping_list():
    name = input("Enter the name of the shopping list: ")
    user_name = input("Enter the user's name: ")

    user = User(name=user_name)
    user.save()

    shopping_list = ShoppingList(name=name, user_id=user.id)
    shopping_list.save()

def add_item():
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price: "))
    shopping_list_id = int(input("Enter the shopping list ID: "))
    item = Item(name=name, price=price, shopping_list_id=shopping_list_id)
    item.save()

def remove_item():
    item_id = int(input("Enter the item ID: "))
    item = Item.get_by_id(item_id)
    if item:
        item.delete()
    else:
        print("Item not found.")

def display_shopping_lists():
    shopping_lists = ShoppingList.get_all()
    for shopping_list in shopping_lists:
        print(f"Shopping List ID: {shopping_list.id}")
        print(f"Name: {shopping_list.name}")
        print(f"User ID: {shopping_list.user_id}")
        print()

def main():
    init_db()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_shopping_list()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            display_shopping_lists()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()