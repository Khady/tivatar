#!/usr/bin/env python
# coding: utf-8

import sha
import random
from shapes import *

shapes = [gen_square, gen_triangle1, gen_triangle2, gen_rect,
          gen_losange, gen_weird, gen_triforce, gen_triangle3,
          gen_littlesquare, gen_2triangle, gen_topleftcornsquare,
          gen_bottriangle1, gen_bottriangle2, gen_toptriangle1,
          gen_toptriangle2, gen_empty]
centers = [0, 4, 8, 15]

def gen_references_shapes():
    i = 0
    for fun in shapes:
        fun(color, rsc).save('samples/%s.png' % i)
        i += 1

# ident doit etre un hexdigest d'un sha1
def generate(ident):
    n = 5
    unique_values = [int(ident[i:i+n], 16) for i in xrange(0, len(ident), n)]
    color = (unique_values[0] % 256, unique_values[1] % 256, unique_values[2] % 256)
    img = Image.new('RGB', (320, 320), (unique_values[3] % 256, unique_values[3] % 256, unique_values[3] % 256))
    draw = ImageDraw.Draw(img)
    center = shapes[unique_values[4] % 14](color)
    img1 = shapes[unique_values[5] % 14](color)
    img2 = shapes[unique_values[6] % 14](color)
    img3 = shapes[unique_values[7] % 14](color)
    img.paste(img1, (0, 0)) # l1
    img.paste(img2, (80, 0))
    img.paste(img2, (160, 0))
    img.paste(img1.rotate(270), (240, 0))
    img.paste(img2.rotate(90), (0, 80)) # l2
    img.paste(center, (80, 80))
    img.paste(center.rotate(270), (160, 80))
    img.paste(img2.rotate(270), (240, 80))
    img.paste(img2.rotate(90), (0, 160)) # l3
    img.paste(center.rotate(90), (80, 160))
    img.paste(center.rotate(180), (160, 160))
    img.paste(img2.rotate(270), (240, 160))
    img.paste(img1.rotate(90), (0, 240)) # l4
    img.paste(img2.rotate(180), (80, 240))
    img.paste(img2.rotate(180), (160, 240))
    img.paste(img1.rotate(180), (240, 240))
    img.save('img/%s.png' % ident)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print "this tool takes 1 arg"
    else:
        generate(sha.new(sys.argv[1]).hexdigest())
