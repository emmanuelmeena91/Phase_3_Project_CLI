from database import init_db, Session
from user import User
from shopping_list import ShoppingList
from item import Item

def display_menu():
    print("1. Create a new shopping list")
    print("2. Add item to a shopping list")
    print("3. Remove item from a shopping list")
    print("4. Display all shopping lists")
    print("5. Exit")

def create_shopping_list(session):
    name = input("Enter the name of the shopping list: ")
    user_name = input("Enter the user's name: ")

    user = User(name=user_name)
    session.add(user)
    session.commit()

    shopping_list = ShoppingList(name=name, user_id=user.id)
    session.add(shopping_list)
    session.commit()

def add_item(session):
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price: "))
    shopping_list_id = int(input("Enter the shopping list ID: "))
    item = Item(name=name, price=price, shopping_list_id=shopping_list_id)
    session.add(item)
    session.commit()

def remove_item(session):
    item_id = int(input("Enter the item ID: "))
    item = Item.get_by_id(item_id, session)
    if item:
        session.delete(item)
        session.commit()
        print("Item removed successfully.")
    else:
        print("Item not found.")

def display_shopping_lists(session):
    shopping_lists = ShoppingList.get_all() 
    for shopping_list in shopping_lists:
        print(f"Shopping List ID: {shopping_list.id}")
        print(f"Name: {shopping_list.name}")
        print(f"User ID: {shopping_list.user_id}")
        print()

def main():
    init_db()

    session = Session()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_shopping_list(session)
        elif choice == "2":
            add_item(session)
        elif choice == "3":
            remove_item(session)
        elif choice == "4":
            display_shopping_lists(session)
        elif choice == "5":
            print("Exiting...")
            session.close()  # Close the session before exiting
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()