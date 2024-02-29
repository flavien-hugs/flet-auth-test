import flet as ft
from src.views import BaseView


class LoginView(BaseView):
    def __init__(
        self,
        page: ft.Page,
        page_route="/",
        page_icon=ft.icons.LOCK,
        page_title="Veuillez-vous connecter à votre compte.",
        page_footer="Vous n'avez pas de compte ? Inscrivez-vous",
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
