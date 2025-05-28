import unittest

from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        alt_text = "image"
        link = "https://i.imgur.com/zjjcJKZ.png"
        text = f"This is text with an ![{alt_text}]({link})"
        matches = extract_markdown_images(text)
        self.assertListEqual([(alt_text, link)], matches)
    
    def test_extract_markdown_links(self):
        link_text = "to boot dev"
        link = "https://www.boot.dev"
        text = f"This is text with a link [{link_text}]({link})"
        matches = extract_markdown_links(text)
        self.assertListEqual([(link_text, link)], matches)
        
    def test_multiple_images(self):
        alt_text1 = "rick roll"
        link1 = "https://i.imgur.com/aKaOqIh.gif"
        alt_text2 = "obi wan"
        link2 = "https://i.imgur.com/fJRm4Vk.jpeg"
        text = f"This is text with a ![{alt_text1}]({link1}) and ![{alt_text2}]({link2})"
        matches = extract_markdown_images(text)
        self.assertListEqual([(alt_text1, link1), (alt_text2, link2)], matches)
    
    def test_multiple_links(self):
        link_text1 = "to boot dev"
        link1 = "https://www.boot.dev"
        link_text2 = "to youtube"
        link2 = "https://www.youtube.com/@bootdotdev"
        text = f"This is text with a link [{link_text1}]({link1}) and [{link_text2}]({link2})"
        matches = extract_markdown_links(text)
        self.assertListEqual([(link_text1, link1), (link_text2, link2)], matches)
        