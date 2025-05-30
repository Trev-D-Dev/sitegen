from enum import Enum

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "ulist"
    OLIST = "olist"

def block_to_block_type(block):
    block = block.strip()
    if(len(block) < 1):
        raise ValueError("block is empty")

    lines = block.split("\n")
    current_line = lines[0]
    first_char = current_line[0:1]

    if(first_char.isdigit() == True):
        print(f"{current_line} is an ordered list item")
        second_char = current_line[1:2]
        if(second_char == "."):
            pass
        elif(second_char.isdigit() == True):
            pass
        else:
            pass
        return

    match first_char:
        case "#":
            print(f"{current_line} is a header")
        case "`":
            print(f"{current_line} is a code block")
        case ">":
            print(f"{current_line} is a quote")
        case "-":
            print(f"{current_line} is an unordered list item")
        case _:
            print(f"{current_line} is a paragraph")