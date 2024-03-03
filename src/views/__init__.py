import time

import flet as ft


class BaseView(ft.View):
    def __init__(
        self,
        page: ft.Page,
        page_route: str,
        page_icon: str,
        page_title: str,
        page_footer: str,
        page_btn_text: str,
        route_to: str,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.page = page
        self.page_icon = page_icon
        self.page_title = page_title
        self.page_footer = page_footer
        self.page_btn_text = page_btn_text
        self.route_to = route_to

        self.image = ft.Icon(
            scale=ft.Scale(4),
            name=self.page_icon,
            animate_scale=ft.Animation(duration=900, curve="decelerate"),
        )

        self.password_field = ft.TextField(
            autofocus=True,
            password=True,
            max_lines=1,
            can_reveal_password=True,
            cursor_color=ft.colors.WHITE,
            border_color=ft.colors.WHITE,
            label="Entrer votre mot de passe",
            tooltip="Entrer votre mot de passe",
            on_focus=lambda e: self.start_animation(),
            on_blur=lambda e: self.stop_animation(),
        )

        self.btn_submit = ft.ElevatedButton(text=self.page_btn_text)

        self.running: bool

        self.controls = [
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.IconButton(
                                    scale=0.85,
                                    icon=ft.icons.DARK_MODE_ROUNDED,
                                    on_click=lambda e: self.toggle_theme(e),
                                )
                            ],
                        ),
                        ft.Divider(height=50, color=ft.colors.TRANSPARENT),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            height=150,
                            controls=[self.image],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[ft.Text(self.page_title, size=16, weight="bold")],
                        ),
                        ft.Divider(height=40, color=ft.colors.TRANSPARENT),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Column(
                                    controls=[self.password_field, self.btn_submit]
                                )
                            ],
                        ),
                        ft.Divider(height=50, color=ft.colors.TRANSPARENT),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    self.page_footer,
                                    spans=[
                                        ft.TextSpan(
                                            " ici.",
                                            style=ft.TextStyle(
                                                italic=False,
                                                decoration_style="solid",
                                                weight="w100",
                                            ),
                                            on_click=lambda e: self.routing(),
                                        )
                                    ],
                                )
                            ],
                        ),
                    ]
                )
            )
        ]

    def routing(self):
        self.stop_animation()
        time.sleep(1.9)
        if not self.running:
            self.page.go(self.route_to)

    def start_animation(self):
        self.running = True
        self.run_animation()

    def stop_animation(self):
        self.running = False
        self.run_animation()

    def run_animation(self):
        if self.running:
            self.image.scale = ft.transform.Scale(4.9)
            self.image.update()
            time.sleep(0.9)

            self.image.scale = ft.transform.Scale(4)
            self.image.update()
            time.sleep(0.9)
            self.run_animation()
        else:
            self.image.scale = ft.transform.Scale(4)
            self.image.update()

    def toggle_theme(self, e):
        if e.control.icon == ft.icons.LIGHT_MODE_ROUNDED:
            self.page.theme_mode = ft.ThemeMode.DARK
            e.control.icon = ft.icons.DARK_MODE_ROUNDED

            self.password_field.border_color = ft.colors.WHITE
            self.password_field.cursor_color = ft.colors.WHITE

        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            e.control.icon = ft.icons.LIGHT_MODE_ROUNDED

            self.password_field.border_color = ft.colors.BLACK
            self.password_field.cursor_color = ft.colors.BLACK

        self.page.update()
