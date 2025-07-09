import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_link_eq(self):
        node = TextNode("This is a Link", TextType.LINK)
        node2 = TextNode("This is a Link", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_link_not_eq(self):
        node = TextNode("This is a Link", TextType.LINK)
        node2 = TextNode("This is a link", TextType.LINK, None)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("this is a link", TextType.LINK, "https://boot.dev")
        self.assertEqual("TextNode(this is a link, link, https://boot.dev)", repr(node)
        )



if __name__ == "__main__":
    unittest.main()
