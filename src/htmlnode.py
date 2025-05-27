
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
            text += " "
            text += key
            text += f'="{self.props[key]}"'

        return text

    def __repr__(self):
        return_string = ""
        return_string += "HTMLNode:"
        return_string += f"\n\tTag: {self.tag}"
        return_string += f"\n\tValue: {self.value}"
        return_string += f"\n\tChildren: {self.children}"
        return_string += f"\n\tProps: {self.props}"
        return return_string
