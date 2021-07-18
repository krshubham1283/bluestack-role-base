from resources import ResourceManager
from roles import RolesManager
from scripts import create_admin_role
from users import UsersManager, User

print("Creating Resources...")
ResourceManager.create_resources()
print("Resources created")

create_admin_role()

current_user = UsersManager.get_user(name="Admin")

print("\nWelcome!! {}\n".format(current_user))

while True:
    _welcome_str = (
        "\nPress 1 to Open Resource List"
        "\nPress 2 to Add Role"
        "\nPress 3 to Create User"
        "\nPress 4 to Change User"
        "\nPress 0 to Kill Program"
        "\n"
    )

    user_input = input(_welcome_str)

    if user_input == "0":
        print("\nAdios {}....".format(current_user))
        break
    if user_input == "1":
        ResourceManager.print_resources(current_user)
    elif user_input == "2":
        RolesManager.create_role()
    elif user_input == "3":
        UsersManager.create_user()
    elif user_input == "4":
        current_user = UsersManager.change_user()
        print("\nWelcome!! {}\n".format(current_user))
    else:
        print("Please choose valid option")


