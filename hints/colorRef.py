#!/usr/bin/python
# coding=utf-8
bold   = "\033[1;38;5;%sm"
normal = "\033[38;5;%sm"
block  = u"\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588"
reset  = "\033[0m"

for i in range(0, 16):
  idx = (bold   + "%03d:"              + reset) % (i, i)
  tag = (normal + block + " system %d" + reset) % (i, i)
  print idx, tag

for i in range(16, 231):
  r = i - 16
  b = r % 6 ; r -= b ; r /= 6
  g = r % 6 ; r -= g ; r /= 6
  idx = (bold   + "%03d:"             + reset) % (i, i)
  tag = (normal + block + " %d/%d/%d" + reset) % (i, r, g, b)
  print idx, tag

for i in range(232, 256):
  idx = (bold   + "%03d:"                 + reset) % (i, i)
  tag = (normal + block + " grayscale %d" + reset) % (i, i - 232)
  print idx, tag
