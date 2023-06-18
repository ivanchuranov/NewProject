from Models.initialDatabase import *


class RolesService:
    _cache = {} # снестиы

    @staticmethod
    def GetRoleById(id:int):
        role = None
        try:
            role = RolesService._cache[id]
        except:
            role = RolesService.GetRoleInDb(id)
            if role != None:
                RolesService._cache[id] = role


        return role

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
            RolesService.ClearCache(id)
            LogFactory.logger.info(f"Удалена роль {role.rolename}.")
    @staticmethod
    def UpdateRole(id, rolename=None):
        if rolename != None:
            role = RolesService.GetRoleInDb(id)
            if role != None:
                if rolename != None and role.rolename != rolename:
                    role.rolename = rolename
                role.save()
                RolesService.ClearCache(id)
    @staticmethod
    def ClearCache(id):
        try:
            del RolesService._cache[id]
        except:
            return

if __name__ == "__main__":
    role_not_found = RolesService.GetRoleById(42094)
    con.close()