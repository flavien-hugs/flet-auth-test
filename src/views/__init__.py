import flet as ft


class BaseView(ft.View):

    def __init__(
        self,
        page: ft.Page,
        page_route: str,
        page_icon: str,
        page_title: str,
        page_footer: str,
        route_to: str
    ):
        self.page = page
        self.icon = page_icon
        self.intro = page_title
        self.footer = page_footer
        self.route_to = route_to

        self.image = ft.Icon(
            scale=ft.Scale(4),
            name=self.icon,
            animate_scale=ft.Animation(duration=900, curve="decelerate")
        )

        super().__init__()

        self.controls = [
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            alignment="end",
                            controls=[
                                ft.IconButton(
                                    scale=0.85,
                                    icon=ft.icons.DARK_MODE_ROUNDED
                                )
                            ]
                        )
                    ]
                )
            )
        ]
