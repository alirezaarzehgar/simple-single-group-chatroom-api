from ..common import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('ID', 'username', 'password', 'first_name', 'last_name', 'profile')

users_schema = UserSchema(many=True)
