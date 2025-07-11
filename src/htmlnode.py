class HTMLNode:
    def __init__(self, tag=None, value=None, childern=None, props=None):
        self.tag = tag
        self.value = value
        self.childern = childern
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            propstring = ""
            for i in self.props.keys():
                propstring+i+'="'+self.props[i]+'" '
            return propstring

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.childern}, props={self.props})"
