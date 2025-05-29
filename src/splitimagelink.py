from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_link(nodes):
    new_nodes = []
    
    for node in nodes:
        node_text = node.text
        reg_match = extract_markdown_links(node_text)
        
        new_nodes = split_nodes(new_nodes, reg_match, node, "link")
            
    return new_nodes

def split_nodes_image(nodes):
    new_nodes = []
    
    for node in nodes:
        node_text = node.text
        reg_match = extract_markdown_images(node_text)
        
        new_nodes = split_nodes(new_nodes, reg_match, node, "image")
        
    return new_nodes

def split_nodes(new_nodes, reg_match, node, text_type):
    if(node.text_type != TextType.TEXT):
        new_nodes.append(node)
        return new_nodes
           
    start_index = 0
    current_index = 0
    
    node_text = node.text
    
    for tuple in reg_match:
        text = tuple[0]
        link = tuple[1]
        
        link_substring = ""
        if(text_type == "link"):
            link_substring = f"[{text}]({link})"
        elif(text_type == "image"):
            link_substring = f"![{text}]({link})"
        
        current_index = node_text.find(link_substring)
        
        if(current_index != start_index):
            substring = node_text[start_index:current_index]
            new_nodes.append(TextNode(substring, "text"))
            node_text = node_text[current_index:]
        
        new_nodes.append(TextNode(text, text_type, link))
        
        node_text = node_text.replace(link_substring, "")
        
    if(len(node_text) != 0):
        new_nodes.append(TextNode(node_text, "text"))
        
    return new_nodes