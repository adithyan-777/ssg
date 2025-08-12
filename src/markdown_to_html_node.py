from htmlnode import HTMLNode


from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks()

    for block in markdown_blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            pass

    

def text_to_children(text: str, block_type):
    if block_type == BlockType.HEADING:
        pass