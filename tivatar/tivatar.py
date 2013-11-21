#!/usr/bin/env python
# coding: utf-8

import Image
import ImageDraw
import sha
import random
import shapes
from inspect import getmembers, isfunction

class Tivatar:
    def __init__(self, ident, size, filetype="", ident_hex=""):
        if ident_hex == "":
            self.ident = sha.new(ident).hexdigest()
        else:
            self.ident = ident_hex
        if filetype == "":
            self.filetype = "png"
        else:
            self.filetype = filetype
        self.shapes = [o[1] for o in getmembers(shapes) if isfunction(o[1])]
        self.size = size

    def gen_references_shapes(self, dir="./"):
        i = 0
        for fun in shapes:
            fun(color).save('%s/%s.png' % (dir, i))
            i += 1

    def generate(self):
        """ident should be an hexdigest of a sha1
        """
        n = 5
        subsize = self.size / 4
        unique_values = [int(self.ident[i:i+n], 16) for i in xrange(0, len(self.ident), n)]
        color = (unique_values[0] % 256, unique_values[1] % 256, unique_values[2] % 256)
        self.img = Image.new('RGB', (self.size, self.size),
                    (unique_values[3] % 256,
                    unique_values[3] % 256,
                    unique_values[3] % 256)
                )
        center = self.shapes[unique_values[4] % 14](color, subsize)
        img1 = self.shapes[unique_values[5] % 14](color, subsize)
        img2 = self.shapes[unique_values[6] % 14](color, subsize)
        img3 = self.shapes[unique_values[7] % 14](color, subsize)
        self.img.paste(img1, (0, 0)) # l1
        self.img.paste(img2, (subsize, 0))
        self.img.paste(img2, (subsize * 2, 0))
        self.img.paste(img1.rotate(270), (subsize * 3, 0))
        self.img.paste(img2.rotate(90), (0, subsize)) # l2
        self.img.paste(center, (subsize, subsize))
        self.img.paste(center.rotate(270), (subsize * 2, subsize))
        self.img.paste(img2.rotate(270), (subsize * 3, subsize))
        self.img.paste(img2.rotate(90), (0, subsize * 2)) # l3
        self.img.paste(center.rotate(90), (subsize, subsize * 2))
        self.img.paste(center.rotate(180), (subsize * 2, subsize * 2))
        self.img.paste(img2.rotate(270), (subsize * 3, subsize * 2))
        self.img.paste(img1.rotate(90), (0, subsize * 3)) # l4
        self.img.paste(img2.rotate(180), (subsize, subsize * 3))
        self.img.paste(img2.rotate(180), (subsize * 2, subsize * 3))
        self.img.paste(img1.rotate(180), (subsize * 3, subsize * 3))

    def save(self, folder):
        self.img.save('%s/%s.%s' % (folder, self.ident, self.filetype))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print "this tool takes 1 arg"
    else:
        image = Tivatar(sys.argv[1], 320)
        image.generate()
        image.save("./")
