import flet as ft
from src.views import BaseView


class RegisterView(BaseView):
    def __init__(
        self,
        page: ft.Page,
        page_route="/register",
        page_icon=ft.icons.PERSON_2_SHARP,
        page_btn_text="S'inscrire",
        page_title="Hello ! Entrez votre mot de passe pour continuer.",
        page_footer="Vous aviez déjà un compte ? Connectez-vous.",
        route_to="/",
    ):
        super().__init__(
            page=page,
            page_route=page_route,
            page_icon=page_icon,
            page_title=page_title,
            page_footer=page_footer,
            page_btn_text=page_btn_text,
            route_to=route_to,
        )
