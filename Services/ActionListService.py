from Models.ActionList import ActionList
from Services.CustomProcedures.AboutProcedureGenerator import AboutProcedureGenerator

class ActionListService:
    user_actions = {}

    @staticmethod
    def StartProcedure(user, procedure_name):
        proc = None
        if procedure_name == AboutProcedureGenerator.PROC_ABOUT_NAME:
            proc = AboutProcedureGenerator.Generate()

        if proc is not None:
            ActionListService.user_actions[user.chat_id] = proc
            return proc.StartProcedure()

    @staticmethod
    def TryContinueProcedure():
        pass

    @staticmethod
    def RemoveProcedure():
        pass