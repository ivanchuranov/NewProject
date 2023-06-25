from Models.initialDatabase import *
class SpecialOfferProcedureService:
    @staticmethod
    def AddDependence(procedure, specialoffer):
        specialoffer = SpecialOffersProcedures.create(procedure=procedure, specialOffer=specialoffer)
        specialoffer.save()
        LogFactory.logger.info(f"Добавлена зависимость {procedure} и {specialoffer}.")
        return specialoffer

    @staticmethod
    def FindSpecialOffersForProcedure(procedure):
        # у тебя есть процедура, ты должен найти все записи в таблице, где procedure совпадает с procedure.id
        spOffers = SpecialOffersProcedures.select().where(SpecialOffersProcedures.procedure == procedure.id)
        return spOffers

    @staticmethod
    def FindProceduresForSpecialOffer(specialoffer):
        procedures = SpecialOffersProcedures.select().where(SpecialOffersProcedures.specialOffer == specialoffer.id)
        return procedures