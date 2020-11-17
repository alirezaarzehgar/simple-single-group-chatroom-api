from ..common import ma


class MessageSchema(ma.Schema):
    class Meta:
        fields = ('ID', 'user_id', 'text', 'file_name', 'file_type', 'time')

messages_schema = MessageSchema(many=True)
