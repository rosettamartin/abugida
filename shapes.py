from xml.etree import ElementTree


class Path:
    def __init__(self, d, **attrib):
        self.d = d
        self.attrib = {
            'stroke': 'black',
            'fill': 'none',
            'stroke-width': '5px',
            **attrib}

    def create_element(self):
        return ElementTree.Element(
            'path',
            attrib={
                'd': self.d,
                **self.attrib})


class Circle:
    def __init__(self, cx, cy, r, **attrib):
        self.cx, self.cy, self.r = cx, cy, r
        self.attrib = attrib

    def create_element(self):
        return ElementTree.Element(
            'circle',
            attrib={
                'cx': self.cx,
                'cy': self.cy,
                'r': self.r,
                **self.attrib})


class Group:
    def __init__(self, *items, **attrib):
        self.items = items
        self.attrib = attrib

    def create_element(self):
        element = ElementTree.Element('g', attrib=self.attrib)
        for item in self.items:
            element.insert(1, item.create_element())
        return element


class Consonant:
    def __init__(self, shape,
                 medial_bar=False, final_bar=False, final_shift=None):
        """
        A consonant character. `shape` is either a Path, Circle, or
        Group. The boolean value `medial_bar` specifies whether the
        consonant's base shape requires a vertical bar. The boolean
        value `final_bar` specifies whether the consonant's final form
        requires a vertical bar. `final_shift` is a 2-tuple of x and y
        values; if provided, the consonant's final form will be shifted
        by x and y, rather than flipped horizontally.

        :param shape: A Path, Circle, or Group
        :param medial_bar: A boolean
        :param final_bar: A boolean
        :param final_shift: a 2-tuple of x and y values
        """

        self.shape = shape
        self.medial_bar = medial_bar
        self.final_bar = final_bar
        self.final_shift = final_shift
