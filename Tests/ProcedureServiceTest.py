from Services.ProceduresService import ProceduresService

# Кейс 1
print("case 1")
proc = ProceduresService.GetProcedureInDb(1990876)
print(proc)

# Кейс 2
print("case 2")

procedure = ProceduresService.AddProcedure(name="ad", description="da", price=2)
print(procedure.name, procedure.price, procedure.description)


#Keйс 4
print("case 4")
procedure = ProceduresService.GetProcedureInDb(id)
print(procedure.name, procedure.price, procedure.description)

#Кейс 5
print("case 5")
ProceduresService.DelProcedure(id)
procedure = ProceduresService.GetProcedureInDb(id)
print(procedure)

