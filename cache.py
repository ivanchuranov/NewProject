
from initialDatabase import *
_cache = {}


def GetInstance(id:int):
    user = None

    try:
        user = _cache[id]
        print("В кэше есть.")
    except:
        print("В кэше нет, ищем в БД.")

        try:
            user = User.get(User.id == id)
            print("В бд есть, кладем в кэш.")
            _cache[id] = user
        except:
            print("В бд нет.")

    return user

if __name__ == "__main__":
    user_not_found = GetInstance(42094)
    con.close()