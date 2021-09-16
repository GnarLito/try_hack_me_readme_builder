#!/usr/bin/env python3

import re

HTML_TAGS = [
  'span'      , '/span'
  , 'p'       , '/p'
  , 'a'       , '/a'
  , 'em'      , '/em'
  , 'b'       , '/b'
  , 'strong'  , '/strong'
  , 'br'
]

REPLACE_TAGS = [
  ['&amp;', '']
  , ['&lt;', '<']
  , ['&gt;', '>']
  , ['<code>', '`']
  , ['</code>', '`']
  , ['\n`', '`']
]

def deHTML(in_put, replace=''):
  in_put = re.sub(r"\n", '', in_put);
  for t in HTML_TAGS:
    in_put = re.sub(r"<"+ t +"[^<]*>", replace, in_put);
  for t in REPLACE_TAGS:
    in_put = re.sub(t[0], t[1], in_put);
  return in_put

def newlined(in_put):
  if not in_put.endswith("\n", -3):
    in_put += "\n"
  return in_put
