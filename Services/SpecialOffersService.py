from Models.initialDatabase import *

class SpecialOffersService:
    _cache = {}

    @staticmethod
    def GetSpecialOffersById(id:int):
        specialoffer = None
        try:
            specialoffer = SpecialOffersService._cache[id]
        except:
            specialoffer = SpecialOffersService.GetSpecialOfferInDb(id)
            if specialoffer != None:
                SpecialOffersService._cache[id] = specialoffer


        return specialoffer

    @staticmethod
    def GetSpecialOfferInDb(id):
        try:
            specialoffer = SpecialOffers.get(SpecialOffers.id == id)
            return specialoffer
        except:
            return None

    @staticmethod
    def AddSpecialOffers(name, description, price, endDate, malingDate):
        specialoffer = SpecialOffers.create(name=name, description=description, price=price, endDate=endDate, malingDate=malingDate)
        specialoffer.save()
        LogFactory.logger.info(f"Добавлена новое специальное предложение {name}.")
        return specialoffer

    @staticmethod
    def DelSpecialOffer(id):
        specialoffer = SpecialOffersService.GetSpecialOfferInDb(id)
        if specialoffer != None:
            specialoffer.delete_instance()
            specialoffer.save()
            SpecialOffersService.ClearCache(id)
            LogFactory.logger.info(f"Удалено специальное предложение {specialoffer.name}.")
    @staticmethod
    def UpdateSale(id, name=None,description=None, price=None, endDate=None, malingDate=None):
        if name != None or description != None or price != None or endDate != None or malingDate != None:
            specialoffer = SpecialOffersService.GetSpecialOfferInDb(id)
            if specialoffer != None:
                if name != None and specialoffer.name != name:
                    specialoffer.name = name
                if description != None and specialoffer.description != description:
                    specialoffer.description = description
                if price != None and specialoffer.price != price:
                    specialoffer.price = price
                if endDate != None and endDate.price != endDate:
                    specialoffer.endDate = endDate
                if malingDate != None and malingDate.price != malingDate:
                    specialoffer.malingDate = malingDate
                specialoffer.save()
                SpecialOffersService.ClearCache(id)
    @staticmethod
    def ClearCache(id):
        try:
            del SpecialOffersService._cache[id]
        except:
            return

if __name__ == "__main__":
    specialoffer_not_found = SpecialOffersService.GetSpecialOffersById(42094)
    con.close()