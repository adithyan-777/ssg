import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_text_nodes, extract_markdown_images, extract_markdown_links

class TestMark2Nodes(unittest.TestCase):

    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )
    
    def test_bold_block(self):
        node = TextNode("This is text with a **bold block word", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "invalid Text")

    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](http://example.com/image.png) in it", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "http://example.com/image.png"),
                TextNode(" in it", TextType.TEXT),
            ],
        )
    
    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](http://example.com) in it", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "http://example.com"),
                TextNode(" in it", TextType.TEXT),
            ],
        )

    def test_split_nodes_multiple_images(self):
        node = TextNode("This is text with ![image1](http://example.com/image1.png) and ![image2](http://example.com/image2.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "http://example.com/image1.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "http://example.com/image2.png"),
            ],
        )
    
    def test_split_nodes_multiple_links(self):
        node = TextNode("This is text with [link1](http://example.com/1) and [link2](http://example.com/2)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "http://example.com/1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "http://example.com/2"),
            ],
        )
    
    def test_split_nodes_image_first(self):
        node = TextNode("![image](http://example.com/image.png) is the first part", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("image", TextType.IMAGE, "http://example.com/image.png"),
                TextNode(" is the first part", TextType.TEXT),
            ],
        )

    
    def test_split_nodes_link_first(self):
        node = TextNode("[link](http://example.com) is the first part", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("link", TextType.LINK, "http://example.com"),
                TextNode(" is the first part", TextType.TEXT),
            ],
        )


    def test_text_to_textnodes(self):
        node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_text_nodes(node)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )


    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)" 
        matchs = extract_markdown_images(text)
        self.assertEqual(matchs, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    
    def test_extract_image_empty(self):
        text = ""
        with self.assertRaises(Exception) as context:
            extract_markdown_images(text)
        self.assertTrue("Invalid text!" in str(context.exception))

    def test_extract_image_invalid(self):
        text = None
        with self.assertRaises(Exception) as context:
            extract_markdown_images(text)
        self.assertTrue("Invalid text!" in str(context.exception))

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matchs = extract_markdown_links(text)
        self.assertEqual(matchs, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    
    def test_extract_links_empty(self):
        text = ""
        with self.assertRaises(Exception) as context:
            extract_markdown_links(text)
        self.assertTrue("Invalid text!" in str(context.exception))

    def test_extract_links_invalid(self):
        text = None
        with self.assertRaises(Exception) as context:
            extract_markdown_links(text)
        self.assertTrue("Invalid text!" in str(context.exception))
    
