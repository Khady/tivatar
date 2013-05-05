import sha
import tivatar
from bottle import route, run, template, static_file, request, redirect

@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./img')

@route('/hex/:identifiant')
def generate_hex(identifiant='default'):
    tivatar.generate(identifiant)
    return static_file('%s.png' % identifiant, root='./img', mimetype='image/png')

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
    # id_hash = sha.new(identifiant).hexdigest()
    return redirect('/%s' % identifiant)

run(host='localhost', port=8080)
