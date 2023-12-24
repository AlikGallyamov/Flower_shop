import dataclasses


@dataclasses.dataclass
class LoginWindow:
    title: str
    number: str


login_window = LoginWindow(title='Введите телефон, чтобы войти', number='1231231231')
