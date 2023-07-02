from Models.Action import Action
from Models.ActionList import ActionList
from Services.LogFactory import LogFactory
class AboutProcedureGenerator:
    PROC_ABOUT_NAME = "about"
    @staticmethod
    def Generate():
        procedure = ActionList(AboutProcedureGenerator.FinalHandler)
        action = Action(AboutProcedureGenerator.ConvertAbout, AboutProcedureGenerator.AskAbout, AboutProcedureGenerator.PROC_ABOUT_NAME)
        action.action_name = AboutProcedureGenerator.PROC_ABOUT_NAME
        procedure.actions.append(action)
        return procedure

    @staticmethod
    def ConvertAbout(data):
        return data

    @staticmethod
    def AskAbout():
        return "Расскажите о себе."
    @staticmethod
    def FinalHandler(actions):
        for action in actions:
            if action.action_name == AboutProcedureGenerator.PROC_ABOUT_NAME:
                LogFactory.logger.info(action.user_data)

        return "Спасибо за информацию!"