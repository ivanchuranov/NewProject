from Services.ProceduresService import ProceduresService

# Кейс 1
print("case 1")
proc = ProceduresService.GetProcedureById(1990876)
print(proc)

# Кейс 2
print("case 2")

procedure = ProceduresService.AddProcedure(name="ad", description="da", price=2)
print(procedure.name, procedure.price, procedure.description)

#Кейс 3
print("case 3")

id = procedure.id
print(ProceduresService._cache)
procedure = ProceduresService.GetProcedureById(id)
print(ProceduresService._cache)
print(procedure)
print(procedure.name, procedure.price, procedure.description)

#Keйс 4
print("case 4")

ProceduresService.UpdateProcedure(id, name="dada", price=3)
print(ProceduresService._cache)
procedure = ProceduresService.GetProcedureById(id)
print(procedure.name, procedure.price, procedure.description)

#Кейс 5
print("case 5")

ProceduresService.DelProcedure(id)
print(ProceduresService._cache)
procedure = ProceduresService.GetProcedureById(id)
print(procedure)
procedure = ProceduresService.GetProcedureInDb(id)
print(procedure)

