from textnode import TextNode, TextType
from extract_utils import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    total_new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            total_new_nodes.append(node)
            continue
        print(node.text)
        splited_text = node.text.split(delimiter)
        if len(splited_text) % 2 == 0:
            raise Exception("invalid Text")
        for i, t in enumerate(splited_text):
            if i % 2 == 0:
                total_new_nodes.append(TextNode(t, node.text_type))
            else:
                total_new_nodes.append(TextNode(t, text_type=text_type))
    return total_new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        matchs = extract_markdown_images(node.text)
        node_text = node.text
        for match in matchs:
            imagelink = f"![{match[0]}]({match[1]})"
            sections = node_text.split(imagelink, 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            node_text = sections[1]
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.TEXT))

    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        matchs = extract_markdown_links(node.text)
        node_text = node.text
        for match in matchs:
            hyperlink = f"[{match[0]}]({match[1]})"
            sections = node_text.split(hyperlink, 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            node_text = sections[1]
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.TEXT))

    return new_nodes

def text_to_text_nodes(text):
    newtext = TextNode(text, TextType.TEXT)

    nodes = split_nodes_delimiter(old_nodes=[newtext], delimiter="**", text_type=TextType.BOLD)
    nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="_", text_type=TextType.ITALIC)
    nodes = split_nodes_delimiter(old_nodes=nodes, delimiter="`", text_type=TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes