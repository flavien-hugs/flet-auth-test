import flet as ft
from . import BaseView


class LoginView(BaseView):
    def __init__(
        self,
        page: ft.Page,
        page_route="/",
        page_icon="lock",
        page_title="Login page",
        page_footer="New to the app ? Register",
        route_to="/register"
    ):
        super().__init__(
            page=page,
            page_route=page_route,
            page_icon=page_icon,
            page_title=page_title,
            page_footer=page_footer,
            route_to=route_to
        )
