
def markdown_to_blocks(markdown):
    md_splits = markdown.split("\n\n")
    # print(md_splits)

    new_lines = []

    for line in md_splits:
        # print("Line: " + line)
        length = len(line)
        start_sub = line[:2]
        end_sub = line[(length-3):]
        new_lines.append(line)
    
    return new_lines