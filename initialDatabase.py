from peewee import *

con = SqliteDatabase("data/NeBana.sqlite")
class BaseModel(Model):

    class Meta:
        database = con

class Roles(BaseModel):
    id = AutoField(column_name="RoleId")
    rolename = TextField(column_name="RoleName", null=False)
    class Meta:
        table_name = "Roles"
Roles.create_table()

class Procedures (BaseModel):
    id = AutoField(column_name="ProceduresId")
    username = TextField(column_name="ProceduresName", null=False)
    class Meta:
        table_name = "Procedures "
Procedures.create_table()

class SpecialOffers (BaseModel):
    id = AutoField(column_name="SpecialOffersId")
    username = TextField(column_name="SpecialOffersName", null=False)
    class Meta:
        table_name = "SpecialOffers "
SpecialOffers.create_table()

class User(BaseModel):
    id = AutoField(column_name="UserId")
    chat_id = IntegerField(column_name="ChatId", null=False)
    is_bot = TextField(column_name="is_bot", null=False)
    first_name = TextField(column_name="first_name", null=False)
    last_name = TextField(column_name="last_name", null=False)
    username = TextField(column_name="username", null=True)
    language_code = TextField(column_name="language_code", null=False)
    roleid = ForeignKeyField(Roles, on_delete="cascade", on_update="cascade", to_field="id")
    class Meta:
        table_name = "User"
User.create_table()

if __name__ == '__main__':
    ''' role1 = Roles.create(rolename="admin")
    role1.save()
    role2 = Roles.create(rolename="client")
    role2.save()'''
    con.close()