#!/usr/bin/env python
# coding: utf-8

import operator
import itertools
import Image
import ImageDraw

def gen_square(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (80, 0), (80, 80), (0, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_triangle1(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (80, 0), (0, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_triangle2(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 80), (40, 0), (80, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_rect(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (40, 0), (40, 80), (0, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_losange(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(40, 0), (80, 40), (40, 80), (0, 40)]
    draw.polygon(tri, rsc)
    return img

def gen_weird(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (80, 40), (80, 80), (40, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_triforce(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    rsc = rsc
    tri = [(0, 80), (20, 40), (40, 80)]
    draw.polygon(tri, rsc)
    tri = [(20, 40), (40, 0), (60, 40)]
    draw.polygon(tri, rsc)
    tri = [(40, 80), (60, 40), (80, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_triangle3(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (80, 40), (40, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_littlesquare(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(20, 20), (60, 20), (60, 60), (20, 60)]
    draw.polygon(tri, rsc)
    return img

def gen_2triangle(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 80), (0, 40), (40, 40)]
    draw.polygon(tri, rsc)
    tri = [(40, 40), (40, 0), (80, 0)]
    draw.polygon(tri, rsc)
    return img

def gen_topleftcornsquare(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (40, 0), (40, 40), (0, 40)]
    draw.polygon(tri, rsc)
    return img

def gen_bottriangle1(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 40), (80, 40), (40, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_bottriangle2(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 80), (40, 40), (80, 80)]
    draw.polygon(tri, rsc)
    return img

def gen_toptriangle1(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 40), (40, 0), (40, 40)]
    draw.polygon(tri, rsc)
    return img

def gen_toptriangle2(color, rsc):
    img = Image.new('RGB', (80, 80), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (40, 0), (0, 40)]
    draw.polygon(tri, rsc)
    return img
