#! /usr/bin/env python3

# USAGE: ./chat2txt.py < cha_file

import re
import sys

body_line_regex = re.compile(r'^\*PAR\d+:  (.*) \. \S+_\S+$')

for line in sys.stdin:
    utterance_match = body_line_regex.match(line)
    if utterance_match:
        text = utterance_match.group(1)
        print(text)
