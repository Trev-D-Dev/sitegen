import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertAlmostEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_family(self):
        grandchild1 = LeafNode("h1", "I am grandchild 1")
        grandchild2 = LeafNode("p", "I am grandchild 2")
        grandchild3 = LeafNode("h2", "I am grandchild 3")
        grandchild4 = LeafNode("h3", "I am grandchild 4")

        child1 = ParentNode("div", [grandchild1, grandchild2])
        child2 = ParentNode("span", [grandchild3, grandchild4])

        parent = ParentNode("main", [child1, child2])

        self.assertEqual(
            parent.to_html(),
            "<main><div><h1>I am grandchild 1</h1><p>I am grandchild 2</p></div><span><h2>I am grandchild 3</h2><h3>I am grandchild 4</h3></span></main>"
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            self.assertNotEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_no_tag(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            self.assertNotEqual(parent_node.to_html(), "<b>child</b>")