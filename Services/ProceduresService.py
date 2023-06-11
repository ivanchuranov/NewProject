from Models.initialDatabase import *

class ProceduresService:
    _cache = {}

    @staticmethod
    def GetProcedureById(id:int):
        procedure = None
        try:
            procedure = ProceduresService._cache[id]
        except:
            procedure = ProceduresService.GetProcedureInDb(id)
            if procedure != None:
                ProceduresService._cache[id] = procedure


        return procedure

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

        return procedure

    @staticmethod
    def DelProcedure(id):
        procedure = ProceduresService.GetProcedureInDb(id)
        if procedure != None:
            procedure.delete_instance()
            procedure.save()
            ProceduresService.ClearCache(id)

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
                ProceduresService.ClearCache(id)
    @staticmethod
    def ClearCache(id):
        try:
            del ProceduresService._cache[id]
        except:
            return

if __name__ == "__main__":
    procedure_not_found = ProceduresService.GetProcedureById(42094)
    con.close()