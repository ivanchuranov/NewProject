from Models.initialDatabase import *
from Services.LogFactory import LogFactory
class SpecialOffersService:
    @staticmethod
    def GetSpecialOfferInDb(id):
        try:
            specialoffer = SpecialOffers.get(SpecialOffers.id == id)
            return specialoffer
        except Exception as ex:
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
            LogFactory.logger.info(f"Удалено специальное предложение {specialoffer.name}.")
    @staticmethod
    def UpdateSpecialOffer(id, name=None,description=None, price=None, endDate=None, malingDate=None):
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


    @staticmethod
    def GetSpecialOfferText(id):
        specialoffer = SpecialOffersService.GetSpecialOfferInDb(id)
        text = "Такого специального предложения не существует."

        if specialoffer != None:
            text = f"{specialoffer.name} ...\n"
            connections = SpecialOffersProcedures.select().where(SpecialOffersProcedures.specialOffer == id)
            if len(connections) > 0:
                text += "Процедуры участвующии в спец предложении:\n"

                for connection in connections:
                    text += f"* {connection.procedure.name}"
        return text



if __name__ == "__main__":
    con.close()