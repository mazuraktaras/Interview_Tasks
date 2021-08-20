class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):

        handler = f'handle_{event}'
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent is not None:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_help(self, event):
        print(f'MainWindow: I handle {event}')

    def handle_default(self, event):
        print(f'MainWindow Default: I can not handle {event} Chosen default handler')


class DialogPanel(Widget):
    def handle_double_click(self, event):
        print(f'DialogPanel: I handle {event}')


class Button(Widget):
    def handle_click(self, event):
        print(f'Button: I handle {event}')


window = MainWindow()
dialog = DialogPanel(window)
button = Button(dialog)

button.handle('double_click')

# help double_click click
