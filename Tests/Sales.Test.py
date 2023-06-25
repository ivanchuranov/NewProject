from Services.SalesService import SalesService
# Кейс 1
print("case 1")
proc = SalesService.GetSaleInDb(1990876)
print(proc)

# Кейс 2
print("case 2")

procedure = SalesService.UpdateSale(procedure="da", price=2, endDate=None, malingDate=None)
print(procedure.name, procedure.price, procedure.description, procedure.endDate, procedure.malingDate)


#Keйс 4
print("case 4")
procedure = SalesService.GetSaleInDb(id)
print(procedure.name, procedure.price, procedure.description, procedure.endDate, procedure.malingDate)

#Кейс 5
print("case 5")
SalesService.DelSale(id)
procedure = SalesService.GetSaleInDb(id)
print(procedure)