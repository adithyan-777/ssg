
import unittest

from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a", "google.com", props={"href": "https://www.google.com"})
        node2 = HTMLNode("a", "google.com", props={"href": "https://www.google.com"})
        self.assertEqual(node1.props_to_html(), node2.props_to_html())

    def check_error(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html())

    def test_not_eq(self):
        node1 = HTMLNode("H", "HomePage")
        node2 = HTMLNode("a", "google.com", props={"href": "https://www.google.com"})
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Google</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()


