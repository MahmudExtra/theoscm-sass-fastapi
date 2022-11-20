from type.UserType import User


def UserSchema(user):
    return User(
        id = (user["_id"]),
        name = user["name"],
        email = user["email"],
        password = user["password"]
        )