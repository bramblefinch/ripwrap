from pathlib import Path
import typer
from functions import rip
import rich

def main(filename: str):
    rich.print(f"ripping {filename}")
    ripped = rip(f"{filename}")
    rich.print(ripped)
    print(ripped)
    text_filename = Path(filename).with_suffix('.txt')
    f = open(f"{text_filename}", "x")
    f.write(ripped)
    f.close()


if __name__ == "__main__":
    typer.run(main)
