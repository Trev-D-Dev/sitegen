import unittest

from splitdelimiter import split_nodes_delimiter
from textnode import TextNode

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter_incorrect(self):
        node = TextNode("This is text with a **bold** word", "text")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", "bold")
    
    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", "text")
        split_nodes_delimiter([node], "**", "bold")

    def test_split_delimiter_code(self):
        node = TextNode("This text has a `code block` in it", "text")
        split_nodes_delimiter([node], "`", "code")

    def test_split_delimiter_italic(self):
        node = TextNode("There is _italicized text_ in here", "text")
        split_nodes_delimiter([node], "_", "italic")

    def test_multiple_nodes(self):
        node1 = TextNode("Sure hope no one puts **bold words** in here", "text")
        node2 = TextNode("Yeah, **bold words** would be very unfortunate", "text")
        split_nodes_delimiter([node1, node2], "**", "bold")