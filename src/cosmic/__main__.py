"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Cosmic."""


if __name__ == "__main__":
    main(prog_name="cosmic")  # pragma: no cover
