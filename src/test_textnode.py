import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_noteq_different_url(self):
        node = TextNode("Test Link", TextType.LINK, "http://boot.dev")
        node2 = TextNode("Test Link", TextType.LINK, None)
        self.assertNotEqual(node,node2)
    def test_noteq_different_text(self):
        node = TextNode("Test Link", TextType.LINK, "http://boot.dev")
        node2 = TextNode("Different Text", TextType.LINK, "http://boot.dev")
        self.assertNotEqual(node, node2)
    def test_eq_all_equal(self):
        node = TextNode("Testing", TextType.LINK, url=None )
        node2 = TextNode("Testing", TextType.LINK, url=None )
        self.assertEqual(node,node2)
    
if __name__ == "__main__":
    unittest.main()