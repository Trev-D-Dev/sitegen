from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_link(nodes):
    new_nodes = []
    
    for node in nodes:
        node_text = node.text
        reg_match = extract_markdown_links(node_text)
        
        # sanitize the string of any markdown symbols
        node_text = node_text.replace("[", "")
        node_text = node_text.replace("](", " ")
        node_text = node_text.replace(")", "")
        
        new_nodes = split_nodes(new_nodes, reg_match, node_text, "link")
            
    return new_nodes

def split_nodes_image(nodes):
    new_nodes = []
    
    for node in nodes:
        node_text = node.text
        reg_match = extract_markdown_images(node_text)
        
        # sanitize the strong of any markdown symbols
        node_text = node_text.replace("![", "")
        node_text = node_text.replace("](", " ")
        node_text = node_text.replace(")", "")
        
        new_nodes = split_nodes(new_nodes, reg_match, node_text, "image")
        
    return new_nodes

def split_nodes(new_nodes, reg_match, node_text, text_type):
    start_index = 0
    current_index = 0
    
    for tuple in reg_match:
        text = tuple[0]
        link = tuple[1]
        
        if(text_type == "link"):
            link_substring = f"[{text}]({link})"
        elif(text_type == "image"):
            link_substring = f"![{text}]({link})"
        
        
        current_index = node_text.find(link_substring)
        
        if(current_index != start_index):
            substring = node_text[start_index:current_index]
            new_nodes.append(TextNode(substring, "text"))
            
            
        # change order of finding index, then sanitize the strings so that way the wrong stuff isn't removed
        if(text_type == "link"):
            link_substring
        elif(text_type == "image"):
            pass
        
        
        length = len(link_substring)
            
        new_nodes.append(TextNode(text, text_type, link))
        
        node_text = node_text[(current_index+length):]
        
    if(len(node_text) != 0):
        new_nodes.append(TextNode(node_text, "text"))
        
    return new_nodes