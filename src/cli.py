import typer
import flet
from src import main_page

app = typer.Typer(pretty_exceptions_enable=False)


@app.command()
def run():
    flet.app(target=main_page, name="auth")


if __name__ == "__main__":
    app()
