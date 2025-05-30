
def markdown_to_blocks(markdown):
    md_splits = markdown.split("\n\n")

    blocks = []

    for line in md_splits:
        line = line.strip("\n")
        line = line.strip()
        blocks.append(line)
    
    return blocks