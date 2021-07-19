from resources import ResourceManager
from roles import RolesManager
from scripts import create_admin_role
from users import UsersManager, User

print("Creating Resources...")
ResourceManager.create_resources()
print("Resources created")

create_admin_role()

current_user = UsersManager.get_user(name="Admin")

print("\nWelcome!! {}".format(current_user))

while True:
    _welcome_str = (
        "\nType 0 & Press Enter -- Kill Program"
        "\nType 1 & Press Enter -- Open Resource List"
        "\nType 2 & Press Enter -- Change User"
    )

    if current_user.name == "Admin":
        _welcome_str += ("\nType 3 & Press Enter -- Create User"
                         "\nType 4 & Press Enter -- Create Role")

    _welcome_str += "\n"

    user_input = input(_welcome_str)

    if user_input == "0":
        print("\nAdios {}....".format(current_user))
        break
    if user_input == "1":
        ResourceManager.print_resources(current_user)
    elif user_input == "2":
        current_user = UsersManager.change_user()
        print("\nWelcome!! {}".format(current_user))
    elif user_input == "3":
        UsersManager.create_user()
    elif user_input == "4":
        RolesManager.create_role()
    else:
        print("Please choose valid option")


