from initialDatabase import *
_cache = {}


def GetInstance(chat_id:int):
    user = None
    try:
        user = _cache[chat_id]
    except:
        try:
            user = User.get(User.chat_id == chat_id)
            _cache[chat_id] = user
        except:
            return None

    return user

if __name__ == "__main__":
    user_not_found = GetInstance(42094)
    con.close()