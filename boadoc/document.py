from docxtpl import DocxTemplate

__author__ = 'jbui'


class DocFile(object):
    """
    Class for the document generator.

    Used to create new document.
    """
    TABLE_ALIGNMENT_LEFT = 1
    TABLE_ALIGNMENT_CENTER = 2
    TABLE_ALIGNMENT_RIGHT = 3

    def __init__(self, **kwargs):
        """
        Constructor

        :param kwargs:
        :return:
        """
        self.myDocument = None

        self.logo = kwargs.get('logo', None)
        self.header = kwargs.get('header', None)
        self.footer = kwargs.get('footer', None)

        self.template_path = kwargs.get('template')
        self.context = kwargs.get('context')

        self.pages = []

    def write_docx(self, file_path):
        """
        Write docx.

        :param file_path:
        :return:
        """
        import boadoc.word as wd

        writer = wd.Writer(self, file_path)
        writer.write()

    def write_pdf(self, file_path):
        """
        Write pdf.

        :param file_path:
        :return:
        """
        import boadoc.pdf as pf

        writer = pf.Writer(self, file_path)
        writer.write()

    @property
    def doc(self):
        """

        :return:
        """
        return self.myDocument

    @doc.setter
    def doc(self, value):
        """

        :param value:
        :return:
        """
        self.myDocument = value

    def initialize(self):
        """
        Initialize a new document.

        """
        pass

    def open_document(self, filename):
        """
        Open a new file document json format.

        :param filename:
        """
        pass

    def add_page(self, page):
        """

        :param page:
        :return:
        """
        self.pages.append(page)

    def save(self, file_name):
        """

        :param file_name:
        :return:
        """
        pass

    def set_level(self):
        """

        :return:
        """
        for page in self.pages:
            page.set_level()

    def add_header(self, header):
        """

        :param header:
        :return:
        """
        self.header = header

    def add_footer(self, footer):
        """

        :param footer:
        :return:
        """
        self.footer = footer
