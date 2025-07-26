import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def text_text_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props["href"], "www.boot.dev")
        self.assertEqual(html_node.value, "This is a link")
    
    def test_text_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")
    
    def test_text_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://example.com/image.png")
        self.assertEqual(html_node.props["alt"], "This is an image")
        self.assertEqual(html_node.value, "")



if __name__ == "__main__":
    unittest.main()
