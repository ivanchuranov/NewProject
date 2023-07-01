class Action:
    def __init__(self, data_converter, question):
        self.user_data = None
        self.data_converter = data_converter
        self.completed = False
        self.question = question
        self.isInvoked = False
        # в 17:00
        # 10:00
        # 10
        # какое время написано : {prompt}, напиши ответ в формате hh:mm

    def SaveData(self, data):
        self.user_data = self.data_converter(data)
        self.completed = True

    def InvokeQuestion(self):
        res = self.question()
        self.isInvoked = True
        return res
