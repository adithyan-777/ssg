from enum import Enum

class BlockType(Enum):
   PARAGRAPH ="paragraph"
   HEADING = "heading"
   CODE = "code"
   QUOTE = "quote"
   UNORDERED_LIST = "unordered_list"
   ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    cleaned_blocks = [block.strip() for block in blocks if block]
    return cleaned_blocks

def block_to_block_type(block: str):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        is_quote_block = True
        for line in block.split("\n"):
            if not line.startswith(">"):
                is_quote_block = False
        return BlockType.QUOTE if is_quote_block else None
    elif block.startswith("-"):
        is_unordered_block = True
        for line in block.split("\n"):
            if not line.startswith("-"):
                is_unordered_block = False
        return BlockType.UNORDERED_LIST if is_unordered_block else None
    elif "." in block:
        parts = block.split(".", 1)
        if len(parts) >= 2:
            number_part = parts[0]
            current_order = 0
            if number_part.isdigit():
                order_list_flag = True
                for line in block.split("\n"):
                    line_part = line.split(".", 1)
                    if len(line_part) >= 2:
                        line_numderpart = line_part[0].strip()
                        order_numder = int(line_numderpart) if line_numderpart.isdigit() else None
                        if not order_numder or current_order+1 != order_numder:
                            order_list_flag = False
                        current_order = order_numder
        return BlockType.ORDERED_LIST if order_list_flag else None
    else:
        return BlockType.PARAGRAPH


