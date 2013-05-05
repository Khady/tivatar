#!/usr/bin/env python
# coding: utf-8

import random
from shapes import *

shapes = [gen_square, gen_triangle1, gen_triangle2, gen_rect,
          gen_losange, gen_weird, gen_triforce, gen_triangle3,
          gen_littlesquare, gen_2triangle, gen_topleftcornsquare,
          gen_bottriangle1, gen_bottriangle2, gen_toptriangle1,
          gen_toptriangle2, gen_empty]
centers = [0, 4, 8, 15]


def random_shaded_color(color):
    '''
    Take a color and shade it randomly with +50, 0 or -50.
    '''
    shade = itertools.repeat(random.choice((+50, 0, -50)), 3)
    shaded_color = tuple(map(operator.add, color, shade))
    return shaded_color

def gen_references_shapes():
    i = 0
    for fun in shapes:
        fun(color, rsc).save('samples/%s.png' % i)
        i += 1

def generate(ident):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rsc = random_shaded_color(color)
    img = Image.new('RGB', (320, 320), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    center = shapes[centers[random.randint(0, 3)]](color, rsc)
    img1 = shapes[random.randint(0, 13)](color, rsc)
    img2 = shapes[random.randint(0, 13)](color, rsc)
    img3 = shapes[random.randint(0, 13)](color, rsc)
    img.paste(img1, (0, 0)) # l1
    img.paste(img2, (80, 0))
    img.paste(img2, (160, 0))
    img.paste(img1.rotate(270), (240, 0))
    img.paste(img2.rotate(90), (0, 80)) # l2
    img.paste(center, (80, 80))
    img.paste(center, (160, 80))
    img.paste(img2.rotate(270), (240, 80))
    img.paste(img2.rotate(90), (0, 160)) # l3
    img.paste(center, (80, 160))
    img.paste(center, (160, 160))
    img.paste(img2.rotate(270), (240, 160))
    img.paste(img1.rotate(90), (0, 240)) # l4
    img.paste(img2.rotate(180), (80, 240))
    img.paste(img2.rotate(180), (160, 240))
    img.paste(img1.rotate(180), (240, 240))
    img.save('img/%s.png' % ident)

if __name__ == '__main__':
    generate()
