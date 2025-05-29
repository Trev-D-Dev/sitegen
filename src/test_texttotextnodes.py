import unittest

from textnode import TextNode
from texttotextnodes import text_to_text_nodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_node(self):
        link_text = "boot dev"
        link1 = "https://www.boot.dev"
        
        alt_text = "click here"
        link2 = "https://i.imgur.com/aKaOqIh.gif"
        text = f"My **favorite** website is definitely [{link_text}]({link1}). I have learned _soooo_ much from their courses, such as `python`! I highly recommend it, ![{alt_text}]({link2})"
        
        new_nodes = text_to_text_nodes(text)