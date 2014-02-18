"""XML: MIN writer NW test

Testing suite to write XML in the MIN style.

"""

import lexor
from lexor.command.test import compare_with

DOCUMENT = """
<!--Copyright: Manuel Lopez-->
<parent>
<!--This comment is not copied in the min style-->
<child/>
<!--ML: My comment-->
This is some content.
<!--JS: My name is John Smith-->
</parent>
"""

EXPECTED = """<parent><child/> This is some content. </parent>"""
EXPECTED_CR = """<!--Copyright: Manuel Lopez--><parent><child/> This \
is some content. </parent>"""
EXPECTED_USER = """<parent><child/><!--ML: My comment--> This is some \
content. <!--JS: My name is John Smith--></parent>"""


def test_min():
    """xml.writer.min.nw """
    doc, _ = lexor.parse(DOCUMENT, 'xml')
    doc.style = 'min'
    compare_with(str(doc), EXPECTED)
    doc.defaults = {'comment': 'Copyright:'}
    compare_with(str(doc), EXPECTED_CR)
    doc.defaults['comment'] = 'ML:|JS:'
    compare_with(str(doc), EXPECTED_USER)
