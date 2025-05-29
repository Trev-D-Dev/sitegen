import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("a", "Google", None, { "href": "https://google.com", "target": "_blank", })
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_print(self):
        node = HTMLNode("div", "Bing", None, { "x": "gonna give it to ya" })
        
    def test_print_child(self):
        c_node = HTMLNode("h1", "Title", None, { "class:" "mainTitle" })
        p_node = HTMLNode("div", None, c_node, { "class": "mainDiv" })

if __name__ == "__main__":
    unittest.main()
