RESOURCES = ["RS1", "RS2", "RS3", "RS4"]

ALLOWED_ACTIONS = ["READ", "WRITE", "DELETE"]

ROLES = [
    {
        "name": "Role1",
        "permissions": {
            "resource": "RS1",
            "actions": ["READ", "WRITE", "DELETE"]
        }
    }
]

USERS = ["Admin"]

