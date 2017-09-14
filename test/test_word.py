
import os

from unittest import TestCase

from boadoc.document import DocFile
from boadoc.glyph import Header, Paragraph, Section, Picture, Table, PageBreak
from boadoc.page import Page, CoverPage, TableOfContent

__author__ = 'jbui'


class TestWord(TestCase):
    """

    """
    def setUp(self):
        self.folder_path = os.path.abspath(os.path.dirname(__file__))

        self.word = DocFile()
        self.page = Page()

    def test_add_heading(self):
        self.page.add_header(Header(**{'text': 'Heading 1'}))
        self.page.add_header(Header(**{'text': 'Heading 2'}))
        self.page.add_header(Header(**{'text': 'Heading 3'}))

        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'docx', 'test_add_heading.docx')
        self.word.write_docx(file_path)

        self.assertTrue(os.path.isfile(file_path))

    def test_add_page_break(self):
        self.page.add_page_break(PageBreak())
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'docx', 'test_add_page_break.docx')
        self.word.write_docx(file_path)

        self.assertTrue(os.path.isfile(file_path))

    def test_add_paragraph(self):
        self.page.add_paragraph(
            Paragraph(text='Test 1 Paragraph. \rTest 1 Paragraph. \rTest 1 Paragraph.\r')
        )
        self.page.add_paragraph(
            Paragraph(**{'text': 'Test 2 Paragraph. \rTest 2 Paragraph. \rTest 2 Paragraph.\r', 'style': 'list_bullet'}))
        self.page.add_paragraph(
            Paragraph(**{'text': 'Test 3 Paragraph. \rTest 3 Paragraph. \rTest 3 Paragraph.\r', 'style': 'list_number'}))
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'docx', 'test_add_paragraph.docx')
        self.word.write_docx(file_path)
        self.assertTrue(os.path.isfile(file_path))

    def test_add_picture(self):
        self.page.add_picture(Picture(os.path.join(self.folder_path, "images", "example1.jpg")))
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'docx', 'test_add_picture.docx')
        self.word.write_docx(file_path)
        self.assertTrue(os.path.isfile(file_path))

    def test_add_section(self):
        s1 = Section(title="Section 1")
        s2 = Section(title="Section 2")
        s3 = Section(title="Section 3")

        self.page.add_section(s1)
        self.page.add_section(s2)
        self.page.add_section(s3)

        s1a = Section(title="Section 1.A")
        s1b = Section(title="Section 1.B")
        s3a = Section(title="Section 3.A")
        s1.add_glyph(s1a)
        s1.add_glyph(s1b)
        s3.add_glyph(s3a)

        s3a1 = Section(title="Section 3.A.1")
        s3a.add_glyph(s3a1)

        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'docx', 'test_add_section.docx')
        self.word.write_docx(file_path)
        self.assertTrue(os.path.isfile(file_path))

    def test_add_table(self):
        self.page.add_table(
                Table([['row 1', 1, 2],
                       ['row 2', 3, 4]])
        )
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'docx', 'test_add_table.docx')
        self.word.write_docx(file_path)

        self.assertTrue(os.path.isfile(file_path))

    def test_demo(self):
        page1 = Page(title="Document Title")

        page1.add_glyphs(Paragraph(text='A plain paragraph having some'))
        s1 = Section(title="Heading, level 1")
        page1.add_glyphs(s1)

        s1.add_glyph(Paragraph(text='Intense Quote', style='intense'))

        s1.add_glyph(Picture(os.path.join(self.folder_path, "images", "example1.jpg")))

        s2 = Section(title="Table")
        page1.add_glyphs(s2)

        s2.add_glyph(
            Table([['Qty', 'Id', 'Desc'],
                   [1, 101, 'Spam'],
                   [2, 42, 'Egg'],
                   [3, 631, 'Spam, spam, eggs, and spam']], header_rows=1)
        )

        self.word.add_page(page1)

        file_path = os.path.join(self.folder_path, 'docx', 'test_add_full_page.docx')
        self.word.write_docx(file_path)

        self.assertTrue(os.path.isfile(file_path))
