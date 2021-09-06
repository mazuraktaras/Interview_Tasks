class ChatRoom:
    """Mediator class."""

    def display_message(self, user, message):
        print(f'[{user} says]: {message}')


class User:
    """A class whose instances want to interact with each other."""

    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room

    def send_message(self, message):
        self.chat_room.display_message(self, message)

    def __str__(self):
        return self.name


mediator = ChatRoom()

taras = User('Taras', mediator)
artem = User('Artem', mediator)
gennadiy = User('Gennadiy', mediator)

taras.send_message("Hi Team! Meeting at 3 PM today.")
artem.send_message("Roger that!")
gennadiy.send_message("Alright.")
