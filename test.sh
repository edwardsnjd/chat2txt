#! /usr/bin/env bash

cmp --silent <(./chat2txt.py < example/input.cha) example/output.txt \
  && echo "🙂 Yay, test passed." \
  || echo "😢 Oh no!  Test failed because output was not expected."
