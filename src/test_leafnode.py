import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        leaf = LeafNode("p", "Hello, world!")
        self.assertEqual(leaf.to_html(), "<p>Hello, world!</p>")
    
    def test_no_value(self):
        leaf = LeafNode("a", None)
        with self.assertRaises(ValueError):
            self.assertNotEqual(leaf.to_html(), "<a></a>")
        
    def test_no_tag(self):
        leaf = LeafNode(None, "This is a test.")
        self.assertEqual(leaf.to_html(), "This is a test.")