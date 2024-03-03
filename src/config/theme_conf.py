WIDTH = 550
HEIGHT = 850


def theme_config(flet, page):
    page.scroll = flet.ScrollMode.ADAPTIVE
    instance_theme = flet.Theme()

    instance_theme.page_transitions.ios = flet.PageTransitionTheme.NONE
    instance_theme.page_transitions.macos = flet.PageTransitionTheme.NONE

    instance_theme.page_transitions.windows = flet.PageTransitionTheme.NONE

    instance_theme.page_transitions.linux = flet.PageTransitionTheme.NONE
    instance_theme.page_transitions.android = flet.PageTransitionTheme.NONE

    page.theme = instance_theme

    page.title = "KEYCLOAK AUTH"

    page.window_max_width = WIDTH
    page.window_max_height = HEIGHT

    page.theme_mode = flet.ThemeMode.DARK
