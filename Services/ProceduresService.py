from Models.initialDatabase import *
from Services.SpecialOffersProceduresService import SpecialOfferProcedureService
from Services.SpecialOffersService import SpecialOffersService
from Services.LogFactory import LogFactory

class ProceduresService:

    @staticmethod
    def GetProcedureInDb(id):
        try:
            procedure = Procedures.get(Procedures.id == id)
            return procedure
        except:
            return None

    @staticmethod
    def AddProcedure(name, description, price):
        procedure = Procedures.create(name=name, description=description, price=price)
        procedure.save()

        LogFactory.logger.info(f"Добавлена новая процедура {name}.")

        return procedure

    @staticmethod
    def DelProcedure(id):
        procedure = ProceduresService.GetProcedureInDb(id)
        if procedure != None:
            name = procedure.name
            procedure.delete_instance()
            procedure.save()
            LogFactory.logger.info(f"Удалена процедура {name}.")
    @staticmethod
    def UpdateProcedure(id, name=None, description=None, price=None):
        if name != None or description != None or price != None:
            procedure = ProceduresService.GetProcedureInDb(id)
            if procedure != None:
                if name != None and procedure.name != name:
                    procedure.name = name
                if description != None and procedure.description != description:
                    procedure.description = description
                if price != None and procedure.price != price:
                    procedure.price = price
                procedure.save()


    @staticmethod
    def GetProceduresText():
        procedures  = Procedures.select()
        # Процедура 1
        # Описание. цена и т.п.
        #
        # Процедура 2

        text = "Сейчас процедур нет."

        if len(procedures) > 0:
            text = "Вот наш список процеду:\n"
            for procedure in procedures:
                discription = ProceduresService.GetProcedureText(id)
                text += f"\n{discription}\n"

        return text

    @staticmethod
    def GetProcedureText(id):
        procedure = ProceduresService.GetProcedureInDb(id)
        text = "Такой процедуры не существует."

        if procedure != None:
            text = f"{procedure.name}\n{procedure.price} рублей"

            sOffersIds = SpecialOfferProcedureService.FindSpecialOffersForProcedure(procedure)

            if len(sOffersIds) > 0:
                text += "\nУчаствует в спец предложениях:\n"

            for id in sOffersIds:
                sOffer = SpecialOffersService.GetSpecialOfferInDb(id)

                if sOffer != None:
                    text += f"* {sOffer.name}\n"


        return text


# Запускается код, если ты запускаешь этот файл
# Прикол в томЮ что когда ты импортируешь этот файл
# то кодЮ не занесенный в этот if запустится

if __name__ == "__main__":
    con.close()