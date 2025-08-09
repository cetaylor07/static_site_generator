import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a",  "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_nv(self):
        node = LeafNode(tag="b", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_nt(self):
        node = LeafNode(tag=None, value="Hello, world!")
        self.assertEqual(node.to_html(), node.value)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    