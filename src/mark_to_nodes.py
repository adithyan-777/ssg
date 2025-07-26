from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    total_new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            total_new_nodes.append(node)
            continue
        splited_text = node.text.split(delimiter)
        if len(splited_text) % 2 == 0:
            raise Exception("invalid Text")
        for i, t in enumerate(splited_text):
            if i % 2 == 0:
                total_new_nodes.append(TextNode(t, node.text_type))
            else:
                total_new_nodes.append(TextNode(t, text_type=text_type))
    return total_new_nodes
