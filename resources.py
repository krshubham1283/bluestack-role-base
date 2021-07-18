from constants import RESOURCES
from roles import RolesManager


class ResourceManager(object):

    resources_list = dict()

    @classmethod
    def create_resources(cls):
        resources = [Resource(name=_res) for _res in RESOURCES]
        cls.resources_list.update({
            res.name: res for res in resources
        })

    @classmethod
    def get_resources(cls):
        return cls.resources_list

    @classmethod
    def print_resources(cls, user):
        print("\nAll Resources\n")
        print("\n".join(cls.resources_list.keys()))
        cls.access_resources(user.roles)

    @classmethod
    def access_resources(cls, user_role):
        while True:
            print("\nEnter \"back\" to go to previous menu.")
            print("\n".join(cls.resources_list.keys()))
            _resource = input("\nSelect a resource:")
            if _resource == "back":
                break
            elif _resource in cls.resources_list.keys():
                current_resource = cls.resources_list[_resource]
                cls.take_action(current_resource, user_role)
            else:
                print("\nPLease select valid resource")

    @classmethod
    def take_action(cls, resource, user_role):
        _allowed_actions = RolesManager.get_allowed_actions(resource=resource, role_names=user_role)
        print("\nEnter \"back\" to go to previous menu.")
        print("\nAllowed actions: " + ", ".join(_allowed_actions))
        while True:
            action = input("\nEnter action: ")
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
