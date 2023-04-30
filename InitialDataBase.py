from peewee import *
con = SqliteDatabase("Roles.SQlite")

class BaseModel(Model):

    class Meta:
        database = con


class User(BaseModel):
    id = AutoField(column_name="UserId")
    username = TextField(column_name="UserName", null=False)
    firstname = TextField(column_name="FirstName", null=True)
    lastname = TextField(column_name="LastName", null=True)
    class Meta:
        table_name = "User"
User.create_table()


class Roles(BaseModel):
    id = AutoField(column_name="RoleId")
    rolename = TextField(column_name="RoleName", null=False)
    userid = ForeignKeyField(User, on_delete="cascade", on_update="cascade", to_field="id")
    class Meta:
        table_name = "Roles"
Roles.create_table()

con.close()