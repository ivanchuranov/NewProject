from Models.initialDatabase import *
from Services.LogFactory import LogFactory
class RolesService:


    @staticmethod
    def GetRoleInDb(id):
        try:
            role = Roles.get(Roles.id == id)
            return role
        except:
            return None

    @staticmethod
    def AddRole(rolename):
        role = Roles.create(rolename=rolename)
        role.save()
        LogFactory.logger.info(f"Добавлена роль {rolename}.")
        return role

    @staticmethod
    def DelRole(id):
        role = RolesService.GetRoleInDb(id)
        if role != None:
            role.delete_instance()
            role.save()
            LogFactory.logger.info(f"Удалена роль {role.rolename}.")
    @staticmethod
    def UpdateRole(id, rolename=None):
        if rolename != None:
            role = RolesService.GetRoleInDb(id)
            if role != None:
                if rolename != None and role.rolename != rolename:
                    role.rolename = rolename
                role.save()


if __name__ == "__main__":
    con.close()