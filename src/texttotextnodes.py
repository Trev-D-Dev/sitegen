from splitdelimiter import split_nodes_delimiter
from splitimagelink import split_nodes_image, split_nodes_link
from textnode import TextNode

def text_to_text_nodes(text):
    node = TextNode(text, "text")
    
    new_nodes = split_nodes_link([node])
    new_nodes = split_nodes_image(new_nodes)
    
    
    new_nodes = split_nodes_delimiter(new_nodes, "`", "code")
    new_nodes = split_nodes_delimiter(new_nodes, "**", "bold")
    new_nodes = split_nodes_delimiter(new_nodes, "_", "italic")
    
    return new_nodes