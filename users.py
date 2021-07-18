from roles import RolesManager


class UsersManager(object):
    """Class to manage the users"""

    all_users = dict()

    @classmethod
    def create_user(cls):
        """Create user by user input"""
        while True:
            _user_name = input("\nEnter User Name:").strip()
            if len(_user_name) > 0:
                break
            else:
                print("\nBlank name in not allowed")
        print("\n Assign roles to user")
        _role_list = RolesManager.get_role_list()
        print("\n".join(_role_list.keys()))
        _user_role = input("Give comma separated list:").split(",")
        cls.save_user(user_name=_user_name, roles=_user_role)

    @classmethod
    def save_user(cls, user_name, roles):
        """
        Save user with all the data
        :param user_name: Name of the user
        :param roles: Roles for the users
        :return:
        """
        if user_name in cls.all_users.keys():
            _user = cls.all_users[user_name]
        else:
            _user = User(name=user_name)
        for _role in roles:
            _user.add_roles(_role)
        cls.all_users.update({user_name: _user})

    @classmethod
    def get_all_users(cls):
        """Get all the users"""
        return cls.all_users

    @classmethod
    def get_user(cls, name):
        """Get user with given name"""
        return cls.all_users[name]

    @classmethod
    def change_user(cls):
        """Change user fir the session"""
        print("\n".join(cls.all_users.keys()))
        while True:
            _new_user = input("\nEnter user name from the list:")
            if _new_user in cls.all_users.keys():
                break
            else:
                print("\nPLease select valid user")
        return cls.all_users[_new_user]


class User(object):
    """User class"""

    def __init__(self, name):
        self.name = name
        self.roles = list()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def add_roles(self, role: str):
        """
        Assign role to user
        :param role: Role to assign to user
        :return:
        """
        self.roles.append(role)

