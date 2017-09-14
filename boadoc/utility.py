import re

from pdf import PDFDocument

__author__ = 'jbui'


FILENAME_RE = re.compile(r'[^A-Za-z0-9\-\.]+')


def pdf_response(filename, as_attachment=True, pdfdocument=PDFDocument, **kwargs):
    from django.http import HttpResponse

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = '%s; filename="%s.pdf"' % (
        'attachment' if as_attachment else 'inline',
        FILENAME_RE.sub('-', filename),
    )

    return pdfdocument(response, **kwargs), response