
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        text = ""
        for key in self.props:
            if(text != ""):
                text += " "
            text += key
            text += f'="{self.props[key]}"'

        return text

    def __repr__(self):
        print("HTMLNode:")
        print(f"\tTag: {self.tag}")
        print(f"\tValue: {self.value}")
        print(f"\tChildren: {self.children}")
        print(f"\tProps: {self.props}")
