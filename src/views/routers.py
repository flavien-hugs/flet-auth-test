from src.views.auth import LoginView, RegisterView


def change_route(page):

    login_page = LoginView(page)
    register_page = RegisterView(page)

    page.views.clear()
    if page.route == "/":
        page.views.append(login_page)

    if page.route == "/login":
        page.views.append(register_page)

    page.update()
