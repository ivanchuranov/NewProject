from Models.initialDatabase import *

class ProceduresService:
    _cache = {}

    @staticmethod
    def GetProcedureById(id:int):
        procedure = None
        try:
            procedure = ProceduresService._cache[id]
        except:
            try:
                procedure = Procedures.get(Procedures.id == id)
                ProceduresService._cache[id] = procedure
            except:
                return None

        return procedure

    @staticmethod
    def GetProcedure():
        id = Procedures.id

        procedure = ProceduresService.GetProcedureById(id)

        if procedure is None:
            return ProceduresService.AddProcedure()

        return procedure

    @staticmethod
    def AddProcedure():
        id = Procedures.id
        name = Procedures.name
        description = Procedures.description
        price = Procedures.price

        procedure = Procedures.create(id=id, name=name, description=description, price=price)
        procedure.save()

        return procedure
    @staticmethod
    def DelProcedure():
        procedure = Procedures.delete()
        procedure.delete()


if __name__ == "__main__":
    procedure_not_found = ProceduresService.GetProcedureById(42094)
    con.close()