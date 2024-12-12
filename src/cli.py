import typer
from functions import rip
import rich

def main(filename: str):
    rich.print(f"ripping {filename}")
    rich.print(rip(f"{filename}"))


if __name__ == "__main__":
    typer.run(main)
