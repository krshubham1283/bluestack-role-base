from constants import ALLOWED_ACTIONS


class RolesManager(object):
    """Class to manager roles operations"""

    role_list = dict()

    @classmethod
    def create_role(cls):
        """
        Create a role taking user input
        :return:
        """
        _role_name = input("\nEnter role name and press enter:")
        _all_resources = cls._get_resources().keys()
        while True:
            print("\n".join(_all_resources))
            _resource = input("\nEnter a resource and press enter:")
            if _resource in _all_resources:
                break
            else:
                print("\n Please select valid resource")
        print(
            "\nAllowed Actions: {}".format(", ".join(ALLOWED_ACTIONS))
        )
        _allowed_action = input("\nGive comma separated list of actions:").split(",")
        _save_actions = filter(lambda x: x in ALLOWED_ACTIONS, _allowed_action)
        if _save_actions:
            cls.save_role(_role_name, _resource, _allowed_action)

    @classmethod
    def save_role(cls, role_name, resource, actions):
        """
        Save role detail given as input
        :param role_name: Name of the role
        :param resource: Resource role can access
        :param actions: Actions allowed for the role
        :return:
        """
        if role_name in cls.role_list.keys():
            _role = cls.role_list[role_name]
        else:
            _role = Role(name=role_name)
        _role.add_permission(resource, actions)
        cls.role_list.update({role_name: _role})

    @classmethod
    def get_role_list(cls):
        """
        Get all the roles
        :return: Role details
        """
        return cls.role_list

    @classmethod
    def _get_resources(cls):
        """
        Get list of all resources
        :return:
        """
        from resources import ResourceManager
        _available_resources = ResourceManager.get_resources()
        return _available_resources

    @classmethod
    def get_allowed_actions(cls, role_names, resource):
        """
        Get list of allowed actions for any role and resource
        :param role_names: name of the role
        :param resource: Name of the resource
        :return:
        """
        _allowed_actions = []
        for role in role_names:
            _permissions = cls.role_list[role].permissions
            _allowed_actions.extend(_permissions.get(str(resource), []))
        return set(_allowed_actions)


class Role(object):
    """Create role"""

    def __init__(self, name):
        self.name = name
        self.permissions = dict()

    def add_permission(self, resource: str, actions: list):
        """
        Add permissions to role for the resource
        :param resource:
        :param actions:
        :return:
        """
        _actions = self.permissions.get(resource, [])
        _actions.extend(actions)
        self.permissions[resource] = _actions


