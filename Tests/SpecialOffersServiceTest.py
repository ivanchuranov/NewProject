from Services.SpecialOffersService import SpecialOffersService

# Кейс 1
print("case 1")
proc = SpecialOffersService.GetSpecialOfferInDb(1990876)
print(proc)

# Кейс 2
print("case 2")

procedure = SpecialOffersService.UpdateSpecialOffer(name="ad", description="da", price=2, endDate=None, malingDate=None)
print(procedure.name, procedure.price, procedure.description, procedure.endDate, procedure.malingDate)


#Keйс 4
print("case 4")
procedure = SpecialOffersService.GetSpecialOfferInDb(id)
print(procedure.name, procedure.price, procedure.description, procedure.endDate, procedure.malingDate)

#Кейс 5
print("case 5")
SpecialOffersService.DelSpecialOffer(id)
procedure = SpecialOffersService.GetSpecialOfferInDb(id)
print(procedure)