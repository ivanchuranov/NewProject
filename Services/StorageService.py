from Models.initialDatabase import *

class StorageService:
    _cache = {}

    @staticmethod
    def GetUserByChatId(chat_id:int):
        user = None
        try:
            user = StorageService._cache[chat_id]
        except:
            try:
                user = Users.get(Users.chat_id == chat_id)
                StorageService._cache[chat_id] = user
            except:
                return None

        return user

    @staticmethod
    def GetUserByContext(context:dict):
        chat_id = context["chat"]["id"]

        user = StorageService.GetUserByChatId(chat_id)

        if user is None:
            return StorageService.AddUser(context)

        return user

    @staticmethod
    def AddUser(context:dict):
        chat_id = context["chat"]["id"]
        first_name = context['from']["first_name"]
        last_name = context['from']["last_name"]
        username = context['from']["username"]
        language_code = context['from']["language_code"]

        user = Users.create(chat_id=chat_id, is_bot=True, first_name=first_name, last_name=last_name, username=username,
                           language_code=language_code, roleid=2)
        user.save()

        return user


if __name__ == "__main__":
    user_not_found = StorageService.GetUserByChatId(42094)
    con.close()