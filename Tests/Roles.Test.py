from Services.RolesService import RolesService
# Кейс 1
print("case 1")
proc = RolesService.GetRoleInDb(1990876)
print(proc)

# Кейс 2
print("case 2")

procedure = RolesService.UpdateRole(rolename="da")
print(procedure.rolename)


#Keйс 4
print("case 4")
procedure = RolesService.GetRoleInDb(id)
print(procedure.rolename)

#Кейс 5
print("case 5")
RolesService.DelRole(id)
procedure = RolesService.GetRoleInDb(id)
print(procedure)