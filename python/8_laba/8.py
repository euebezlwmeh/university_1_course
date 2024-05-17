import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class PasswordManager(toga.App):
    def __init__(self, **kwargs):
        super().__init__(formal_name="Password Manager", app_id="pswrdmngr", **kwargs)

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        service_input = toga.TextInput(placeholder='Service')
        username_input = toga.TextInput(placeholder='Username')
        password_input = toga.PasswordInput(placeholder='Password')

        save_button = toga.Button('Save', on_press=self.save_password)

        self.table = toga.Table(
            headings=["Service", "Username", "Password"],
        )

        main_box.add(service_input)
        main_box.add(username_input)
        main_box.add(password_input)
        main_box.add(save_button)
        main_box.add(self.table)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()    

    def save_password(self, widget):
        service = widget.parent.children[0].value
        username = widget.parent.children[1].value
        password = widget.parent.children[2].value

        try:
            if not service or not username or not password:
                raise ValueError('Service, username, and password are required fields')

            self.table.data.append([service, username, password])
        
        except ValueError as e:
            print(f'Error: {e}')


def main():
    return PasswordManager()

if __name__ == '__main__':
    main().main_loop()