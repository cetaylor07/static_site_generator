class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_list = []
        if self.props:
            for k, v in self.props.items():
                props_list.append(f'{k}="{v}"')
        props_string =  " ".join( props_list)
        if props_string:
            props_string = ' ' + props_string
        return props_string
    def __repr__(self):
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children={self.children}, props={self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have children")
        else:
            opening_tag = f'<{self.tag}>'
            child_html = []
            for child in self.children:
                html = child.to_html()
                child_html.append(html)
            child_html = "".join(child_html)
            ending_tag = f'</{self.tag}>'
            return opening_tag + child_html + ending_tag
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"