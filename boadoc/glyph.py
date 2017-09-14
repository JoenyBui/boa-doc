
__all__ = [
    "glyph",
    "header"
]

__author__ = 'jbui'


class Glyph(object):
    """
    Inherit Glyphs.  Used as a chunks in a document to organize each other.

    """
    def __init__(self, parent=None, **kwargs):
        self.meta_data = None
        self.back_stop = False      # A flag telling the glyph if is nestable or not.

        self.id = kwargs.get('id', None)
        self.class_id = kwargs.get('class_id', None)
        self.level = kwargs.get('level', 1)

        self.parent = parent
        self.child = []

        # Link the parent with the child.
        if parent:
            parent.child.append(self)

    def write(self, driver):
        print("Must Inherit %s" % self.__class__)

    def add_parent(self, parent):
        """
        Adding parent after initialization.
        """
        self.parent = parent
        parent.child.append(self)

    def set_level(self, level):
        self.level = level

        for child in self.child:
            child.set_level(level+1)


class Header(Glyph):
    """
    Write the header of the file.

    """
    def __init__(self, parent=None, **kwargs):
        Glyph.__init__(self, parent)

        self.text = kwargs.get('text', "")
        self.back_stop = True

    def write(self, driver):
        driver.write_heading(self.text)


class Paragraph(Glyph):
    """
    Add new paragraph.

    """
    def __init__(self, parent=None, **kwargs):
        Glyph.__init__(self, parent)

        self.text = kwargs.get('text', "")
        self.style = kwargs.get('style', None)

    def add_texts(self, texts):
        """
        Add the new set of style.

        :param texts:
        """
        self.text = texts

    def write(self, driver):
        """
        Write the paragraph into the document file.

        :param driver:
        """
        driver.write_paragraph(self.text, style=self.style)


class Section(Glyph):
    """
    Section of the model.

    """
    def __init__(self, parent=None, **kwargs):
        """

        :param parent:
        :param kwargs:
        """
        Glyph.__init__(self, parent)

        self.title = kwargs.get('title', None)

        self.glyphs = []

    def add_glyph(self, glyph):
        """
        A general push of the glyphs.

        :param glyph:
        """
        if self.level:
            glyph.level = self.level + 1

        self.glyphs.append(glyph)
        glyph.add_parent(self)

    def add_paragraph(self, paragraph):
        self.add_glyph(paragraph)

    def add_section_header(self, header):
        self.add_glyph(header)

    def add_subsection(self, section):
        self.add_glyph(section)

    def add_image(self, image):
        self.add_glyph(image)

    def write(self, driver):
        """
        Write the heading information.
        """
        # Loop through the section to write out the section.
        if self.title:
            driver.write_heading(self.title, level=self.level)

        for glyph in self.glyphs:
            glyph.write(driver)


class Picture(Glyph):
    """
    Picture Glyph's.

    """
    def __init__(self, file_path, parent=None, **kwargs):
        Glyph.__init__(self, parent)

        self.back_stop = True

        self.file_path = file_path

        self.width = kwargs.get('width', None)
        self.height = kwargs.get('height', None)

    def write(self, driver):
        """
        Write the paragraph into the document file.
        """
        driver.write_picture(self.file_path, width=self.width, height=self.height)


class Table(Glyph):
    """
    Table Glyph's.

    """
    def __init__(self, data=None, parent=None, **kwargs):
        Glyph.__init__(self, parent)

        self.header_rows = kwargs.get('header_rows', 0)
        self.data = data

    def add_new_row(self, row, row_index=-1):
        self.data[row_index].append(row)

    def add_row_in_index(self, table, row, row_index):
        pass

    def add_rows(self, table, data):
        pass

    def add_table_data(self, data, **kwargs):
        pass

    def write(self, driver):
        driver.write_table(self.data)


class PageBreak(Glyph):
    """
    Page Break Glyph's.

    """
    def __init__(self, parent=None, **kwargs):
        Glyph.__init__(self, parent)

    def write(self, driver):
        driver.write_page_break()
