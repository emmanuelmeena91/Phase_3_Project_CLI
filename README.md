# Phase_3_Project_CLI
# Shopping Management System
This is a command-line interface (CLI) application that allows users to effectively manage their shopping lists. The application is designed to solve the problem of disorganized shopping experiences and forgotten items by providing a convenient way to create, modify, and view shopping lists.

# Features
Create new shopping lists with unique names.
Add and remove items from shopping lists.
View all shopping lists associated with a user.
View the items within a specific shopping list.



# Relationships Features:

Shopping_list and User: This is a one-to-many relationship, where one user can have multiple shopping lists. The user_id in the Shopping_list table references the user_id in the User table.

Shopping_list and Item: This is a one-to-many relationship, where one shopping list can have multiple items. The shoping_list_id in the Item table references the shoping_list_id in the Shopping_list table.

# Technologies Used
1. Python
2. SQLAlchemy ORM
3. Pipenv (virtual environment and dependency management)
4. Installation


# Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.


# Installation
1. Clone the repository:

-git clone
# https://github.com/emmanuelmeena91/Phase_3_Project_CLI


2. Navigate to the project directory:

-cd shopping-management


3. Set up a virtual environment and install dependencies:

-pipenv install


4. Activate the virtual environment:

-pipenv shell



# Usage


1. Open Terminal and run :
   -python main.py

2. The application will display a menu with the following options:
    1. Create a new shopping list
    2. Add an item to a shopping list
    3. Remove an item from a shopping list
    4. Display all shopping lists
    5. Exit

3. Choose the desired option by entering the corresponding number and following the prompts.

6. To exit the application, choose option 5 from the menu.

#  Viewing Database Data

1. Install an SQL viewer or SQL editor extension 
2. Open the `database.db` file with the SQL viewer or editor extension


# License
This project is licensed under the MIT License.