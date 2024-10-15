#! /usr/bin/env python3

# USAGE:
#   ./chat2txt.py cha_file
#   ./chat2txt.py < cha_file

import re
import sys

body_line_regex = re.compile(r'^\*PAR\d+:  (.*) \. \S+_\S+$')

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as file:
    for line in file:
        utterance_match = body_line_regex.match(line)
        if utterance_match:
            text = utterance_match.group(1)
            print(text)
