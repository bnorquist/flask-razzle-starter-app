import click
from app import db


@click.command()
def init_db():
    click.echo("Creating database tables")
    db.create_all()
    click.echo("Tables created")


if __name__ == "__main__":
    init_db()
