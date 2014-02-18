Lexor Language: XML min style writer
====================================

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
