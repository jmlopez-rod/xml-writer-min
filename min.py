"""XML: MIN Writer Style

The minimum style removes all the extra blank spaces and comments to
have a compressed document.

There are a few comments that we may want to keep. To make a few
exceptions we can modify the default `comment`.

For instance if driver.xml is:

    <!--Copyright: ML-->
    <parent>
    <!--This comment is not copied in the min style-->
    <child/>
    <!--ML: My comment-->
    content.
    <!--JS: My name is John Smith-->
    </parent>

Then the output of

    lexor driver.xml to xml~min@comment="Copyright:"~

will be

    <!--Copyright: ML--><parent><child/> content. </parent>

"""

from lexor import init, load_aux

INFO = init(
    version=(0, 0, 1, 'final', 0),
    lang='xml',
    type='writer',
    description='Writes XML files to minimize the file size.',
    url='http://jmlopez-rod.github.io/lexor-lang/xml-writer-min',
    author='Manuel Lopez',
    author_email='jmlopez.rod@gmail.com',
    license='BSD License',
    path=__file__
)
MOD = load_aux(INFO)['nw']
DEFAULTS = {
    'comment': '',
}
MAPPING = {
    '#text': MOD.TextNW,
    '#comment': MOD.CommentNW,
    '#doctype': MOD.DoctypeNW,
    '#cdata-section': MOD.CDataNW,
    '__default__': MOD.DefaultNW,
}
