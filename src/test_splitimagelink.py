import unittest

from splitimagelink import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType
'''
class TestSplitImageLink(unittest.TestCase):
    def test_split_link(self):
        link_text = "boot dev's"
        link = "https://www.boot.dev"
        text = f"This is text with a link to [{link_text}]({link}) website"
        node = TextNode(text, "text")
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link to ", "text"),
            TextNode("boot dev's", "link", "https://www.boot.dev"),
            TextNode(" website", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)
        
    def test_split_mult_links(self):
        link_text1 = "boot dev's"
        link1 = "https://www.boot.dev"
        link_text2 = "youtube's"
        link2 = "https://www.youtube.com"
        text = f"This text has a link to [{link_text1}]({link1}) website and [{link_text2}]({link2}) website"
        node = TextNode(text, "text")
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This text has a link to ", "text"),
            TextNode("boot dev's", "link", "https://www.boot.dev"),
            TextNode(" website and ", "text"),
            TextNode("youtube's", "link", "https://www.youtube.com"),
            TextNode(" website", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)
        
    def test_split_mult_link_nodes(self):
        link_text1 = "boot dev's"
        link1 = "https://www.boot.dev"
        link_text2 = "youtube's"
        link2 = "https://www.youtube.com"
        text1 = f"This text has a link to [{link_text1}]({link1}) website"
        text2 = f"This text has a link to [{link_text2}]({link2}) website"
        node1 = TextNode(text1, "text")
        node2 = TextNode(text2, "text")
        new_nodes = split_nodes_link([node1, node2])
        expected_nodes = [
            TextNode("This text has a link to ", "text"),
            TextNode("boot dev's", "link", "https://www.boot.dev"),
            TextNode(" website", "text"),
            TextNode("This text has a link to ", "text"),
            TextNode("youtube's", "link", "https://www.youtube.com"),
            TextNode(" website", "text"),
        ]
        self.assertEqual(new_nodes, expected_nodes)
        
    def test_split_image(self):
        alt_text1 = "rick roll"
        link1 = "https://i.imgur.com/aKaOqIh.gif"
        text = f"This is text with a ![{alt_text1}]({link1}) image"
        node = TextNode(text, "text")
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" image", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)
        
    def test_split_mult_images(self):
        alt_text1 = "rick roll"
        link1 = "https://i.imgur.com/aKaOqIh.gif"
        alt_text2 = "obi wan"
        link2 = "https://i.imgur.com/fJRm4Vk.jpeg"
        text = f"This is text with a ![{alt_text1}]({link1}) image and an ![{alt_text2}]({link2}) image"
        node = TextNode(text, "text")
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" image and an ", "text"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" image", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)
        
    def test_split_mult_image_nodes(self):
        alt_text1 = "rick roll"
        link1 = "https://i.imgur.com/aKaOqIh.gif"
        alt_text2 = "obi wan"
        link2 = "https://i.imgur.com/fJRm4Vk.jpeg"
        text1 = f"This is text with a ![{alt_text1}]({link1}) image"
        text2 = f"This is text with an ![{alt_text2}]({link2}) image"
        node1 = TextNode(text1, "text")
        node2 = TextNode(text2, "text")
        new_nodes = split_nodes_image([node1, node2])
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" image", "text"),
            TextNode("This is text with an ", "text"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" image", "text")
        ]
        self.assertEqual(new_nodes, expected_nodes)
        
'''