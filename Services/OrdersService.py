from Models.initialDatabase import *


class OrdersService:
    _cache = {} # снестиы

    @staticmethod
    def GetOrderById(id:int):
        order = None
        try:
            order = OrdersService._cache[id]
        except:
            order = OrdersService.GetOrderInDb(id)
            if order != None:
                OrdersService._cache[id] = order


        return order

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
            OrdersService.ClearCache(id)
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
                OrdersService.ClearCache(id)
    @staticmethod
    def ClearCache(id):
        try:
            del OrdersService._cache[id]
        except:
            return

if __name__ == "__main__":
    order_not_found = OrdersService.GetOrderById(42094)
    con.close()