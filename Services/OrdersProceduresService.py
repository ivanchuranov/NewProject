from Models.initialDatabase import *
class OrdersProceduresService:
    @staticmethod
    def AddDependence(order,procedure):
        order = OrdersProcedures.create(order=order, procedure=procedure)
        order.save()
        LogFactory.logger.info(f"Добавлена зависимость {order} и {procedure}.")
        return order

    @staticmethod
    def FindOrdersForProcedure(procedure):
        # у тебя есть процедура, ты должен найти все записи в таблице, где procedure совпадает с procedure.id
        order = OrdersProcedures.select().where(OrdersProcedures.procedure == procedure.id)
        return order

    @staticmethod
    def FindProceduresForOrder(order):
        procedures = OrdersProcedures.select().where(OrdersProcedures.order == order.id)
        return procedures