#coding=utf-8

from markdown import markdown

SEG_SIZE = 30
PLACEHOLDER = 'drY4afbChGVZmD5PWunlgc3FX9KMsRtBExvS1oT2z7JHIyAqQO'
PLACEHOLDER_INDEX_LEN = 5
PLACEHOLDER_TEMPLATE = '{{0}}{{1:0>{0}}}'.format(PLACEHOLDER_INDEX_LEN)

def preprocess(text):
    """
    Insert placeholders into source text after every SEG_SIZE characters, and will always insert a
        placeholder at the end of the text.

    @param text: source text
    @returns: a new string generated from source text with the inserted placeholders
    """
    text_index = list(range(0, len(text), SEG_SIZE))
    segments = [
        text[i: i + SEG_SIZE] + PLACEHOLDER_TEMPLATE.format(PLACEHOLDER, i//SEG_SIZE)
        for i in text_index
    ]
    text_index.append(len(text))
    return text_index[1:], ''.join(segments)

def findPlaceholderIndex(text, placeholder_count):
    """
    Given a text, find all indexes of placeholder in it.

    @param text: the text
    @param placeholder_count: count of placeholders inserted in the text
    @returns: a list contains the indexes.
    """
    placeholders = map(
        lambda i: (i, PLACEHOLDER_TEMPLATE.format(PLACEHOLDER, i)),
        range(0, placeholder_count)
    )
    placeholder_len = len(PLACEHOLDER) + PLACEHOLDER_INDEX_LEN
    return list(map(lambda p: text.find(p[1]) - p[0]*placeholder_len, placeholders))

def generateMapping(text, extensions):
    """
    1. Given a source text, insert placeholders into it using funtion `preprocess`
    2. Generate HTML with the modified text
    3. Find all indexes of placeholders in the HTML
    4. Generate the mapping relation

    @param text: the source text
    @param extensions: mark down extensions, will exlude footnotes extension
    @returns: the mapping relation represented by a tuple list
    """
    extensions = filter(lambda e: e != 'markdown.extensions.footnotes', extensions)

    text_index, modified = preprocess(text)
    html_modified = markdown(modified, extensions=extensions)
    modified_index = findPlaceholderIndex(html_modified, len(text_index))
    return zip(text_index, modified_index)





text = """waf
wafiwajfoiwaj iewa oiawjfoaw
awofejowa if
waf owa fowae jfpowajefowa
aw eofjawf
awojfwaoejfowajfeaw
fwajoeifjwaf
wafkoawjefoiwajfoijwa eoifjwa
fjawoiejfaw

```py
import re
```
    """
    
print(preprocess(text)[1])

mapping = generateMapping(text, extensions=['markdown.extensions.footnotes', 'markdown.extensions.fenced_code'])
print(list(mapping))
