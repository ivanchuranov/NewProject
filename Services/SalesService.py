from Models.initialDatabase import *
from Services.LogFactory import LogFactory

class SalesService:




    @staticmethod
    def GetSaleInDb(id):
        try:
            sale = SpecialOffer.get(SpecialOffer.id == id)
            return sale
        except:
            return None

    @staticmethod
    def AddSale(procedure, price, endDate, malingDate):
        sale = Sales.create(procedure=procedure, price=price, endDate=endDate, malingDate=malingDate)
        sale.save()
        LogFactory.logger.info(f"Добавлена скидка на {procedure}.")
        return sale

    @staticmethod
    def DelSale(id):
        sale = SalesService.GetSaleInDb(id)
        if sale != None:
            sale.delete_instance()
            sale.save()
            LogFactory.logger.info(f"Удалена скидка на {sale.procedure}.")
    @staticmethod
    def UpdateSale(id, procedure=None, price=None, endDate=None, malingDate=None):
        if procedure != None or price != None or endDate != None or malingDate != None:
            sale = SalesService.GetSaleInDb(id)
            if sale != None:
                if procedure != None and sale.procedure != procedure:
                    sale.procedure = procedure
                if price != None and sale.price != price:
                    sale.price = price
                if endDate != None and endDate.price != endDate:
                    sale.endDate = endDate
                if malingDate != None and malingDate.price != malingDate:
                    sale.malingDate = malingDate
                sale.save()



if __name__ == "__main__":
    con.close()