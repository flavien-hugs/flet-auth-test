import typer
import flet
from src import mainPage

app = typer.Typer(pretty_exceptions_enable=False)


@app.command()
def run():
    flet.app(target=mainPage, name="auth")


if __name__ == "__main__":
    app()
