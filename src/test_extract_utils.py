import unittest

from extract_utils import extract_markdown_images, extract_markdown_links


class TestExtractUtils(unittest.TestCase):

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
    

