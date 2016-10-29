#coding=utf-8

from markdown import markdown

SEG_SIZE = 30
PLACEHOLDER = 'drY4afbChGVZmD5PWunlgc3FX9KMsRtBExvS1oT2z7JHIyAqQO'
PLACEHOLDER_INDEX_LEN = 5
PLACEHOLDER_TEMPLATE = '{{0}}{{1:0>{0}}}'.format(PLACEHOLDER_INDEX_LEN)

def preprocess(text):
    text_index = list(range(0, len(text), SEG_SIZE))
    segments = [ text[i: i + SEG_SIZE] + PLACEHOLDER_TEMPLATE.format(PLACEHOLDER, i//SEG_SIZE) for i in text_index ]
    text_index.append(len(text))
    return text_index, ''.join(segments)

def findPlaceholderIndex(text, placeholder_count):
    placeholders = map(lambda i: (i, PLACEHOLDER_TEMPLATE.format(PLACEHOLDER, i)), range(0, placeholder_count))
    placeholder_len = len(PLACEHOLDER) + PLACEHOLDER_INDEX_LEN
    return [0] + list(map(lambda p: text.find(p[1]) - p[0]*placeholder_len, placeholders))

def generateMapping(text, extensions):
    extensions = filter(lambda e: e != 'markdown.extensions.footnotes', extensions)

    text_index, modified = preprocess(text)
    html_modified = markdown(modified, extensions=extensions)
    modified_index = findPlaceholderIndex(html_modified, len(text_index) - 1)
    return zip(*[text_index, modified_index])





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
