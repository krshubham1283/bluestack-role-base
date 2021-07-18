from constants import ALLOWED_ACTIONS
from resources import ResourceManager
from roles import RolesManager
from users import UsersManager

all_resources = ResourceManager.get_resources()


def create_admin_role():
    for res in all_resources:
        RolesManager.save_role("admin", res, ALLOWED_ACTIONS)
    UsersManager.save_user(user_name="Admin", roles=["admin"])