from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if(not self.value):
            raise ValueError("all leaf nodes must have a value")
        
        if(self.tag == None):
            return self.value
        else:
            return_html = f"<{self.tag}>{self.value}</{self.tag}>"
            return return_html