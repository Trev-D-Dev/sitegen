from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    delimiter_type = ""
    match delimiter:
        case "`":
            delimiter_type = "code"
        case "**":
            delimiter_type = "bold"
        case "_":
            delimiter_type = "italic"
        case _:
            raise ValueError("invalid delimiter")
        
    if(delimiter_type != text_type):
        raise ValueError("delimiter and text type do not match")

    new_nodes = []

    for node in old_nodes:
        node_text_type = node.text_type
        node_text = node.text
        delim_len = len(delimiter)
        
        if(not delimiter in node_text):
            # raise ValueError("delimiter not present in text")
            new_nodes.append(node)
            continue
        else:
            first_index = node_text.index(delimiter)
            start_text = node_text[:first_index]
            middle_end_text = node_text[first_index+delim_len:]
            
            second_index = middle_end_text.index(delimiter)
            middle_text = middle_end_text[:second_index]
            end_text = middle_end_text[second_index+delim_len:]

            new_nodes.append(TextNode(start_text, node_text_type))
            new_nodes.append(TextNode(middle_text, text_type))
            new_nodes.append(TextNode(end_text, node_text_type))
        
    return new_nodes
        