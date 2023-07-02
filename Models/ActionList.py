import datetime

from Models.Action import Action
class ActionList:
    def __init__(self, final_handler):
        self.actions = list()
        self.final_handler = final_handler
        self.startDate = datetime.datetime.utcnow()
        self.IsStarted = False

    def GetCurrentAction(self):
        for action in self.actions:
            if not action.completed:
                return action
        return None

    def IsCompleted(self):
        return self.GetCurrentAction() is None

    def StartProcedure(self):
        if not self.IsStarted:
            action = self.actions[0]
            return action.InvokeQuestion()

    def TryContinueProcedure(self, user_data):
        action = self.GetCurrentAction()

        if action is not None:
            action.SaveData(user_data)

            next_action = self.GetCurrentAction()

            if next_action is not None:
                return next_action.InvokeQuestion()

        return self.final_handler(self.actions)









