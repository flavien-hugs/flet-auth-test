def themeConfig(flet, page):
    instance_theme = flet.Theme()

    instance_theme.page_transitions.ios = flet.PageTransitionTheme.NONE
    instance_theme.page_transitions.macos = flet.PageTransitionTheme.NONE

    instance_theme.page_transitions.windows = flet.PageTransitionTheme.NONE

    instance_theme.page_transitions.linux = flet.PageTransitionTheme.NONE
    instance_theme.page_transitions.android = flet.PageTransitionTheme.NONE

    page.theme = instance_theme
