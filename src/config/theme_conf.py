HEIGHT = 800


def themeConfig(flet, page):
    instance_theme = flet.Theme()

    instance_theme.page_transitions.ios = flet.PageTransitionTheme.NONE
    instance_theme.page_transitions.macos = flet.PageTransitionTheme.NONE

    instance_theme.page_transitions.windows = flet.PageTransitionTheme.NONE

    instance_theme.page_transitions.linux = flet.PageTransitionTheme.NONE
    instance_theme.page_transitions.android = flet.PageTransitionTheme.NONE

    page.theme = instance_theme

    page.auto_scroll = True
    page.title = "KEYCLOAK AUTH"

    page.window_max_width = HEIGHT/2
    page.window_max_height = HEIGHT
    # page.window_resizable = False

    page.theme_mode = flet.ThemeMode.DARK
