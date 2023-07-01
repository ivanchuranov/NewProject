from Models.initialDatabase import *
from Services.LogFactory import LogFactory

class OrdersService:


    @staticmethod
    def GetOrderInDb(id):
        try:
            order = Orders.get(Orders.id == id)
            return order
        except:
            return None

    @staticmethod
    def AddOrder(total, user, date, comment):
        order = Orders.create(total=total, user=user, date=date, comment=comment)
        order.save()
        LogFactory.logger.info(f"Добавлен заказ {total} на пользователя {user}.")
        return order

    @staticmethod
    def DelOrder(id):
        order = OrdersService.GetOrderInDb(id)
        if order != None:
            order.delete_instance()
            order.save()
            LogFactory.logger.info(f"Удален заказ {order.total} на пользователя {order.user}.")
    @staticmethod
    def UpdateOrder(id, total=None, user=None, date=None, comment=None):
        if total != None or user != None or date != None or comment != None:
            order = OrdersService.GetOrderInDb(id)
            if order != None:
                if total != None and order.total != total:
                    order.total = total
                if user != None and order.user != user:
                    order.user = user
                if date != None and date.price != date:
                    order.date = date
                if comment != None and comment.price != comment:
                    order.comment = comment
                order.save()

if __name__ == "__main__":
    con.close()