import flet as ft

from .config import theme_config
from .views.auth import LoginView, RegisterView


def main_page(page: ft.Page) -> None:

    theme_config(flet=ft, page=page)

    login_page = LoginView(page)
    register_page = RegisterView(page)

    def change_route(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(login_page)

        if page.route == "/register":
            page.views.append(register_page)

        page.update()

    page.views.append(login_page)

    page.on_route_change = change_route

    page.update()
