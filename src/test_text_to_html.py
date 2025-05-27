import unittest

from main import text_node_to_html_node
from textnode import TextNode
from leafnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        print(html_node)

    def test_bold(self):
        node = TextNode("This is a bold text node", "bold")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_bad_text(self):
        with self.assertRaises(Exception):
            node = TextNode("This is a div", "text")
            node.text_type = "div"
            html_node = text_node_to_html_node(node)