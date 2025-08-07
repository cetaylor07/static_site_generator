import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_htmltwo(self):
        node = HTMLNode(props={"testing":1,"test":2}).props_to_html()
        node2 = ' testing="1" test="2"'
        self.assertEqual(node,node2)
    def test_props_to_htmlemp(self):
        node = HTMLNode().props_to_html()
        node2 = ''
        self.assertEqual(node,node2)
    def test_props_to_htmlone(self):
        node = HTMLNode(props={"testing":1}).props_to_html()
        node2 = ' testing="1"'
        self.assertEqual(node,node2)
        