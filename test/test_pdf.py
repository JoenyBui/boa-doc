
from unittest import TestCase

import os

from boadoc.document import DocFile
from boadoc.glyph import Header, Paragraph, Section, Picture, Table, PageBreak
from boadoc.page import Page, CoverPage, TableOfContent

__author__ = 'jbui'


class TestPdf(TestCase):

    def setUp(self):
        self.folder_path = os.path.abspath(os.path.dirname(__file__))

        self.word = DocFile()        # Pdf file
        self.page = Page()

    def test_add_heading(self):
        self.page.add_header(Header(**{'text': 'Heading 1'}))
        self.page.add_header(Header(**{'text': 'Heading 2'}))
        self.page.add_header(Header(**{'text': 'Heading 3'}))

        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'pdf', 'test_add_heading.pdf')
        self.word.write_pdf(file_path)

        self.assertTrue(os.path.isfile(file_path))

    def test_add_page_break(self):
        self.page.add_page_break(PageBreak())
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'pdf', 'test_add_page_break.pdf')
        self.word.write_pdf(file_path)

        self.assertTrue(os.path.isfile(file_path))

    def test_add_paragraph(self):
        self.page.add_paragraph(
            Paragraph(**{'text': 'Test 1 Paragraph. \rTest 1 Paragraph. \rTest 1 Paragraph.\r'}))
        self.page.add_paragraph(
            Paragraph(**{'text': 'Test 2 Paragraph. \rTest 2 Paragraph. \rTest 2 Paragraph.\r', 'style': 'list_bullet'}))
        self.page.add_paragraph(
            Paragraph(**{'text': 'Test 3 Paragraph. \rTest 3 Paragraph. \rTest 3 Paragraph.\r', 'style': 'list_number'}))
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'pdf', 'test_add_paragraph.pdf')
        self.word.write_pdf(file_path)

        # Check file exist and then creation time.
        self.assertTrue(os.path.isfile(file_path))

    def test_add_picture(self):
        self.page.add_picture(Picture(os.path.join(self.folder_path, "images", "example1.jpg")))
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'pdf', 'test_add_picture.pdf')
        self.word.write_pdf(file_path)
        self.assertTrue(os.path.isfile(file_path))

    def test_add_section(self):
        self.page.add_section(Section(title="Section 1"))
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'pdf', 'test_add_section.pdf')
        self.word.write_pdf(file_path)
        self.assertTrue(os.path.isfile(file_path))

    def test_add_table(self):
        self.page.add_table(
                Table([['row 1', 1, 2],
                       ['row 2', 3, 4]])
        )
        self.word.add_page(self.page)

        file_path = os.path.join(self.folder_path, 'pdf', 'test_add_table.pdf')
        self.word.write_pdf(file_path)

        self.assertTrue(os.path.isfile(file_path))

    def test_hello(self):
        import boadoc.pdf as pf

        file_path = os.path.join(self.folder_path, 'pdf', 'hello-world.pdf')
        pdf = pf.PDFDocument(file_path=file_path)
        pdf.init_report()
        pdf.h1('Hello World')
        pdf.p('Creating PDFs made easy.')
        pdf.generate()
