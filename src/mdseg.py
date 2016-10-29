#coding=utf-8

from markdown import markdown

html = markdown("""
A test

# Summary
This is[^a] **just** a _test_.

[^a]:awadaw a

## Guide

```py
cool~

haha
```
""", extensions = ['markdown.extensions.footnotes', 'markdown.extensions.fenced_code'])

print(html)
