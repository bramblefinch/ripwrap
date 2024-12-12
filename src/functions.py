from rich.console import Console
from rich.table import Table

from PIL import Image

from pytesseract import image_to_data, Output


target_data = ["page_num", "block_num", "par_num", "line_num", "word_num", "text"]

def rip(filename: str):
    tess_dict = image_to_data(image=Image.open(f"{filename}"), config='--psm 3', output_type=Output.DICT,)
    stripped = {k: v for k, v in tess_dict.items() if k in target_data}
    page_num = stripped["page_num"]
    block_num = stripped["block_num"]
    par_num = stripped["par_num"]
    line_num = stripped["line_num"]
    word_num = stripped["word_num"]
    text = stripped["text"]
    inlined = list(zip(page_num, block_num, par_num, line_num, word_num, text))
    table = Table(title="Rip")
    collapsed = []
    for item in inlined:
        if item[2] == 0:
            collapsed.append(item) 
        elif item[3] != 0 and item[4] !=0:
            collapsed.append(item)
    for item in target_data:
        table.add_column(item)
    for item in collapsed:
        renderable = (str(item[0]), str(item[1]), str(item[2]), str(item[3]), str(item[4]), item[5])
        table.add_row(*renderable)
    console = Console()
    console.print(table)
    
