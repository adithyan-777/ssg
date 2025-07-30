import re

def extract_markdown_images(text: str):
    if text:
        matchs = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        return matchs
    else:
        raise Exception("Invalid text!")

def extract_markdown_links(text: str):
    if text:
        matchs = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        return matchs
    else:
        raise Exception("Invalid text!")

