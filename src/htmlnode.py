class HTMLNode:
    def __init__(self, tag=None, value=None, childern=None, props=None):
        self.tag = tag
        self.value = value
        self.childern = childern
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        propstring = ""
        for prop in self.props:
            propstring += f' {prop}="{self.props[prop]}"'
        return propstring

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.childern}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, childern = None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError 
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
            return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, childern, props=None):
        super().__init__(tag, value=None, childern=childern, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.childern is None:
            raise ValueError
        children_html = ""
        for child in self.childern:
            children_html = children_html+ child.to_html()
        return f"<{self.tag}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"