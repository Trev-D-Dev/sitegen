import unittest

from mdtoblocks import markdown_to_blocks

class TestMDToBlock(unittest.TestCase):
    def test_md_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        new_lines = markdown_to_blocks(md)
        print(new_lines)