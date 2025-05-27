from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if(self.tag == None):
            raise ValueError("all parent nodes must have a tag")
        elif(self.children == None):
            raise ValueError("all parent nodes must have children")
        
        return_string = ""
        return_string += f"<{self.tag}>"
        
        for child in self.children:
            return_string += child.to_html()
            
        return_string += f"</{self.tag}>"
        
        return return_string