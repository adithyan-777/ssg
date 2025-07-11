
import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()


