import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = "This is a block.\n\nThis is another block."
        expected = ["This is a block.", "This is another block."]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block(self):
        unordered = """- This is a list
- with items"""
        orderd = """1. test1
        2.test2
        3.test3"""
        code_block = """```python
print("Hello, World!")
```"""
        quote = """> This is a quote"""
        h1heading = """# This is a heading"""
        h2heading = """## This is a subheading"""
        h3heading = """### This is a sub-subheading"""
        h6heading = """###### This is a sub-sub-sub-sub-sub-subheading"""
        paragraph = "hi hi hi"

        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(unordered))
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(orderd))
        self.assertEqual(BlockType.CODE, block_to_block_type(code_block))
        self.assertEqual(BlockType.QUOTE, block_to_block_type(quote))
        self.assertEqual(BlockType.HEADING, block_to_block_type(h1heading))
        self.assertEqual(BlockType.HEADING, block_to_block_type(h2heading))
        self.assertEqual(BlockType.HEADING, block_to_block_type(h3heading))
        self.assertEqual(BlockType.HEADING, block_to_block_type(h6heading))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(paragraph))