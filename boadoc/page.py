from .glyph import PageBreak

__author__ = 'jbui'


class Page(object):
    """
    Page of the model.

    """
    def __init__(self, **kwargs):
        self.use_header = True
        self.use_footer = False

        self.title = kwargs.get('title', None)
        self.glyphs = []

    def set_level(self):
        for glyph in self.glyphs:
            glyph.set_level(1)

    def add_glyphs(self, glyph, **kwargs):
        glyph.level = 1
        self.glyphs.append(glyph)

    def add_table(self, table, **kwargs):
        self.add_glyphs(table)

    def add_section(self, section, **kwargs):
        self.add_glyphs(section)

    def add_picture(self, picture, **kwargs):
        self.add_glyphs(picture)

    def add_paragraph(self, paragraph, **kwargs):
        self.add_glyphs(paragraph)

    def add_header(self, header, **kwargs):
        self.add_glyphs(header)

    def add_page_break(self, page_break, **kwargs):
        self.add_glyphs(page_break)

    def write(self, driver):
        """
        Write out the glyphs on the page.
        """
        # Add page-break.
        self.add_glyphs(PageBreak())

        for glyph in self.glyphs:
            glyph.write(driver)


class CoverPage(Page):
    """
    Cover Page of the model.
    """
    def __init__(self, **kwargs):
        Page.__init__(self)


class TableOfContent(Page):
    """
    Table of Content Page with relative linking.

    """
    def __init__(self, **kwargs):
        Page.__init__(self)
