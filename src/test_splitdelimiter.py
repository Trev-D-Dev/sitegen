import unittest

from splitdelimiter import split_nodes_delimiter
from textnode import TextNode

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter_incorrect(self):
        node = TextNode("This is text with a **bold** word", "text")
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter([node], "`", "bold")
    
    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" word", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_delimiter_code(self):
        node = TextNode("This text has a `code block` in it", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        expected_nodes = [
            TextNode("This text has a ", "text"),
            TextNode("code block", "code"),
            TextNode(" in it", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_delimiter_italic(self):
        node = TextNode("There is _italicized text_ in here", "text")
        new_nodes = split_nodes_delimiter([node], "_", "italic")
        expected_nodes = [
            TextNode("There is ", "text"),
            TextNode("italicized text", "italic"),
            TextNode(" in here", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_multiple_nodes(self):
        node1 = TextNode("Sure hope no one puts **bold words** in here", "text")
        node2 = TextNode("Yeah, **bold words** would be very unfortunate", "text")
        new_nodes = split_nodes_delimiter([node1, node2], "**", "bold")
        expected_nodes = [
            TextNode("Sure hope no one puts ", "text"),
            TextNode("bold words", "bold"),
            TextNode(" in here", "text"),
            TextNode("Yeah, ", "text"),
            TextNode("bold words", "bold"),
            TextNode(" would be very unfortunate", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)