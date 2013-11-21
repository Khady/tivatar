#!/usr/bin/env python
# coding: utf-8

import operator
import itertools
import Image
import ImageDraw

def gen_square(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (size, 0), (size, size), (0, size)]
    draw.polygon(tri, color)
    return img

def gen_triangle1(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (size, 0), (0, size)]
    draw.polygon(tri, color)
    return img

def gen_triangle2(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, size), (size / 2, 0), (size, size)]
    draw.polygon(tri, color)
    return img

def gen_rect(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (size / 2, 0), (size / 2, size), (0, size)]
    draw.polygon(tri, color)
    return img

def gen_losange(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(size / 2, 0), (size, size / 2), (size / 2, size), (0, size / 2)]
    draw.polygon(tri, color)
    return img

def gen_weird(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (size, size / 2), (size, size), (size / 2, size)]
    draw.polygon(tri, color)
    return img

def gen_triforce(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, size), (20, size / 2), (size / 2, size)]
    draw.polygon(tri, color)
    tri = [(20, size / 2), (size / 2, 0), (60, size / 2)]
    draw.polygon(tri, color)
    tri = [(size / 2, size), (60, size / 2), (size, size)]
    draw.polygon(tri, color)
    return img

def gen_triangle3(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (size, size / 2), (size / 2, size)]
    draw.polygon(tri, color)
    return img

def gen_littlesquare(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(20, 20), (60, 20), (60, 60), (20, 60)]
    draw.polygon(tri, color)
    return img

def gen_2triangle(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, size), (0, size / 2), (size / 2, size / 2)]
    draw.polygon(tri, color)
    tri = [(size / 2, size / 2), (size / 2, 0), (size, 0)]
    draw.polygon(tri, color)
    return img

def gen_topleftcornsquare(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (size / 2, 0), (size / 2, size / 2), (0, size / 2)]
    draw.polygon(tri, color)
    return img

def gen_bottriangle1(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, size / 2), (size, size / 2), (size / 2, size)]
    draw.polygon(tri, color)
    return img

def gen_bottriangle2(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, size), (size / 2, size / 2), (size, size)]
    draw.polygon(tri, color)
    return img

def gen_toptriangle1(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, size / 2), (size / 2, 0), (size / 2, size / 2)]
    draw.polygon(tri, color)
    return img

def gen_toptriangle2(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tri = [(0, 0), (size / 2, 0), (0, size / 2)]
    draw.polygon(tri, color)
    return img

def gen_empty(color, size):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    return img
