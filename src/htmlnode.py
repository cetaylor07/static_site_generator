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