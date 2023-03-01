import mongoengine as mg
from datetime import datetime
from mongoengine.connection import _get_db
from constant import password

password = password
db = mg.connect(
    # db="simple_test",
    # username="Phong",
    # password="123123",
    host=f"mongodb+srv://Phong:{password}@cluster0.gqprlls.mongodb.net/?retryWrites=true&w=majority",
)

db.drop_database("simple_test")
mg.disconnect()

mg.connect(
    db="simple_test",
    # username="Phong",
    # password="123123",
    host=f"mongodb+srv://Phong:{password}@cluster0.gqprlls.mongodb.net/?retryWrites=true&w=majority",
)


class User(mg.Document):
    user_name = mg.StringField(
        unique=True,
        require=True,
    )
    email = mg.StringField(
        unique=True,
        require=True,
    )
    passward = mg.StringField(require=True)
    phone_number = mg.StringField()
    age = mg.IntField(min=0, max=150)

    date_created = mg.DateTimeField(default=datetime.now())

    meta = {
        "indexes": [
            "user_name",
            "email",
        ],
        "ordering": ["date_created"],
    }


class BlogPost(mg.DynamicDocument):
    title = mg.StringField(
        unique=True,
        require=True,
    )
    content = mg.StringField(
        require=True,
    )
    author = mg.ReferenceField(User)
    date_created = mg.DateField(default=datetime.now())


# print(host1)

user1 = User(
    user_name="phong1",
    email="phong1@gmail.com",
    passward="123123",
    phone_number="232",
    # age=20,
).save()

user2 = User(
    user_name="phong0",
    email="phong2@gmail.com",
    passward="123123",
).save()

user3 = User(
    user_name="phong3",
    email="phong0@gmail.com",
    passward="123123",
).save()

user4 = User(
    user_name="phong01",
    email="phong12@gmail.com",
    passward="123123",
).save()

try:
    user5 = User(
        user_name="phong1",
        email="phong1@gmail.com",
        passward="123123",
    )
    user5.save()
except mg.NotUniqueError:
    print("Not unique error!")


blog1 = BlogPost(
    title="post1",
    content="dlskfjsdfdsfsfssdfsdfsdfsdfsdfsdfsdfsdfsdsdfsd",
    author=user1,
).save()

blog1 = BlogPost(
    title="post0",
    content="dlskfjsdfdsfsfssdfsdfsdfsdfsdfsdfsdfsdfsdsdfsd",
    author=user2,
).save()


blog1 = BlogPost(
    title="post3",
    content="dlskfjsdfdsfsfssdfsdfsdfsdfsdfsdfsdfsdfsdsdfsd",
    author=user1,
).save()

print("done")
