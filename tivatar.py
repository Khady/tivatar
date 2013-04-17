#!/usr/bin/env python
# coding: utf-8

import random
from shapes import *

def random_shaded_color(color):
    '''
    Take a color and shade it randomly with +50, 0 or -50.
    '''
    shade = itertools.repeat(random.choice((+50, 0, -50)), 3)
    shaded_color = tuple(map(operator.add, color, shade))
    return shaded_color

def main():
    shapes = [gen_square, gen_triangle1, gen_triangle2, gen_rect,
              gen_losange, gen_weird, gen_triforce, gen_triangle3,
              gen_littlesquare, gen_2triangle, gen_topleftcornsquare,
              gen_bottriangle1, gen_bottriangle2, gen_toptriangle1,
              gen_toptriangle2]

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rsc = random_shaded_color(color)
    i = 0
    for fun in shapes:
        fun(color, rsc).save('samples/%s.png' % i)
        i += 1

if __name__ == '__main__':
    main()
