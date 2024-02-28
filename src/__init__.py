import flet as ft

from src.config import themeConfig
from .views.login import LoginView


async def mainPage(page: ft.Page) -> None:
    page.title = "KEYCLOAK AUTH"
    page.theme_mode = ft.ThemeMode.DARK

    await themeConfig(flet=ft, page=page)

    login_page = LoginView(page)
    page.views.append(login_page)

    await page.add_async()
    await page.update_async()
