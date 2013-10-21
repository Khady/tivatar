#!/usr/bin/env python
# coding: utf-8

import sha
import tivatar
import yaml
from bottle import route, run, template, static_file, request, redirect

CONFIG = {}

@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./img')

@route('/hex/:identifiant')
def generate_hex(identifiant='default'):
    image = tivatar.generate(identifiant)
    image[1].save('%s/%s.%s' % (CONFIG['folder'], image[0], CONFIG['format']))
    return static_file('%s.%s' % (identifiant, CONFIG['format']), root=CONFIG['folder'],
        mimetype='image/%s' % CONFIG['format'])

@route('/:identifiant')
def generate(identifiant='default'):
    return generate_hex(sha.new(identifiant).hexdigest())

@route('/')
def index(identifiant='World'):
    return '''
        <form action="/img" method="post">
            identifiant:    <input type="text" name="identifiant" />
            <input type="submit" value="identifiant" />
        </form>
    '''

@route('/img', method='POST')
def do_login():
    identifiant = request.forms.get('identifiant')
    id_hash = sha.new(identifiant).hexdigest()
    return redirect('/hex/%s' % id_hash)

if __name__ == '__main__':
    with open('tivatar_config.yml', 'r') as f:
        yaml_content = f.read()
        f.close()
        CONFIG = yaml.load(yaml_content)
        print CONFIG
    run(host='0.0.0.0', port=8080)
