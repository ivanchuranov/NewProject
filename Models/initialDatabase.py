from peewee import *

con = SqliteDatabase("data/NeBana.sqlite")

class BaseModel(Model):

    class Meta:
        database = con

class Roles(BaseModel):
    id = AutoField(column_name="id")
    rolename = TextField(column_name="name", null=False)
    class Meta:
        table_name = "Roles"

Roles.create_table()

class Procedures(BaseModel):
    id = AutoField(column_name="id")
    name = TextField(column_name="name", null=False)
    description = TextField(column_name="description", null=True)
    price = IntegerField(column_name="price",null=False)

    class Meta:
        table_name = "Procedures"

Procedures.create_table()

class Sales(BaseModel):
    id = AutoField(column_name="id")
    procedure = ForeignKeyField(Procedures, on_delete="cascade", on_update="cascade", to_field="id")
    price = IntegerField(column_name="price", null=False)
    description = TextField(column_name="description", null=True)
    endDate = DateTimeField(column_name="endDate", null=False)
    malingDate = DateTimeField(column_name="malingDate", null=False)

    class Meta:
        table_name = "Sales"

Sales.create_table()

class SpecialOffers(BaseModel):
    id = AutoField(column_name="id")
    name = TextField(column_name="name", null=False)
    description = TextField(column_name="description", null=True)
    price = IntegerField(column_name="price", null=False)
    endDate = DateTimeField(column_name="endDate",null=False)
    malingDate = DateTimeField(column_name="malingDate",null=False)
    class Meta:
        table_name = "SpecialOffers"

SpecialOffers.create_table()
class Sales(BaseModel):
    id = AutoField(column_name="id")
    procedure = TextField(column_name="procedure", null=False)
    price = IntegerField(column_name="price", null=False)
    endDate = DateTimeField(column_name="endDate",null=False)
    malingDate = DateTimeField(column_name="malingDate",null=False)

    class Meta:
        table_name = "Sales"

Sales.create_table()
class SpecialOffersProcedures(BaseModel):
    specialOffer = ForeignKeyField(SpecialOffers, on_delete="cascade", on_update="cascade", to_field="id")
    procedure = ForeignKeyField(Procedures, on_delete="cascade", on_update="cascade", to_field="id")

    class Meta:
        table_name = "SpecialOffersProcedures"

SpecialOffersProcedures.create_table()

class Users(BaseModel):
    id = AutoField(column_name="id")
    chat_id = IntegerField(column_name="chatId", null=False)
    is_bot = TextField(column_name="isBot", null=False)
    first_name = TextField(column_name="firstName", null=False)
    last_name = TextField(column_name="lastName", null=False)
    username = TextField(column_name="username", null=True)
    language_code = TextField(column_name="languageCode", null=False)
    description = TextField(column_name="description", null=True)
    role = ForeignKeyField(Roles, on_delete="cascade", on_update="cascade", to_field="id")
    class Meta:
        table_name = "Users"

Users.create_table()

class Orders(BaseModel):
    id = AutoField(column_name="id")
    total = IntegerField(column_name="total", null=False)
    user = ForeignKeyField(Users, on_delete="cascade", on_update="cascade", to_field="id")
    date = DateTimeField(column_name="date", null=True)
    comment = TextField(column_name="comment",null=True)

    class Meta:
        table_name = "Orders"

Orders.create_table()

class OrdersProcedures(BaseModel):
    order = ForeignKeyField(Orders, on_delete="cascade", on_update="cascade", to_field="id")
    procedure = ForeignKeyField(Procedures, on_delete="cascade", on_update="cascade", to_field="id")
    class Meta:
        table_name = "OrdersProcedures"

OrdersProcedures.create_table()

if __name__ == '__main__':
    ''' role1 = Roles.create(rolename="admin")
    role1.save()
    role2 = Roles.create(rolename="client")
    role2.save()'''

    connections = SpecialOffersProcedures.select().where(SpecialOffersProcedures.specialOffer == 1)
    for conn in connections:
        print(conn.procedure.name)
    con.close()