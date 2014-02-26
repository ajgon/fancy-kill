#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

pchars = u"abcdefghijklmnopqrstuvwxyz,.?!'()[]{}"
fchars = u"ɐqɔpǝɟƃɥıɾʞlɯuodbɹsʇnʌʍxʎz'˙¿¡,)(][}{"
flipper = dict(zip(pchars, fchars))

def flip(s):
  charList = [ flipper.get(x, x) for x in s.lower() ]
  charList.reverse()
  return u"\n(╯°□°)╯︵ " + "".join(charList)

os.system("pkill " + " ".join(sys.argv[2::]))
print flip(" ".join(sys.argv[2::]))
