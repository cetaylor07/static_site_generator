import re
from textnode import TextNode,TextType


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue
        split_text = node.text.split(delimeter)
        if len(split_text) % 2 == 0:
            raise Exception("Invalid Markdown syntax: missing closing delimiter")
        for i, text in enumerate(split_text):
            if i % 2 == 0:
                split_nodes.append(TextNode(text, TextType.TEXT))
            if i % 2 != 0:
                split_nodes.append(TextNode(text, text_type))

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches