from constants import RESOURCES
from roles import RolesManager


class ResourceManager(object):
    """Class to manage all the resources"""

    resources_list = dict()

    @classmethod
    def create_resources(cls):
        """
        Create resources defined in constants.py file
        :return:
        """
        resources = [Resource(name=_res) for _res in RESOURCES]
        cls.resources_list.update({
            res.name: res for res in resources
        })

    @classmethod
    def get_resources(cls):
        """
        List of resources available
        :return: {_resource_name: _resource}
        """
        return cls.resources_list

    @classmethod
    def print_resources(cls, user):
        """
        Print list of resources
        :param user: Current user
        :return:
        """
        print("\nAll Resources\n")
        print("\n".join(cls.resources_list.keys()))
        cls.access_resources(user.roles)

    @classmethod
    def access_resources(cls, user_role):
        """
        Method to access resources based on user role
        :param user_role: Roles of current user
        :return:
        """
        while True:
            print("\nEnter \"back\" to go to previous menu.")
            print("\nAll Resources\n")
            print("\n".join(cls.resources_list.keys()))
            _resource = input("\nType resource name and press enter (PLease type exactly same name):")
            if _resource == "back":
                break
            elif _resource in cls.resources_list.keys():
                current_resource = cls.resources_list[_resource]
                cls.take_action(current_resource, user_role)
            else:
                print("\nPLease select valid resource")

    @classmethod
    def take_action(cls, resource, user_role):
        """
        Take action on some resource based on the role
        :param resource: Resource
        :param user_role: Role list of the user
        :return:
        """
        _allowed_actions = RolesManager.get_allowed_actions(resource=resource, role_names=user_role)
        print("\nEnter \"back\" to go to previous menu.")
        if len(_allowed_actions) > 0:
            print("\nAllowed actions: " + ", ".join(_allowed_actions))
        else:
            print("\nYou are not allowed to take any action on this resource")
        while True:
            action = input("\nType action and press enter: ")
            if action == "back":
                break
            elif action in _allowed_actions:
                print("\n{} done..".format(action))
            else:
                print("\nPermission Denied")


class Resource(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
