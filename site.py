import sha
import tivatar
from bottle import route, run, template, static_file, request, redirect

@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./img')

@route('/:identifiant')
def generate(identifiant='World'):
    name = sha.new(identifiant).hexdigest()
    tivatar.generate(name)
    return static_file('%s.png' % name, root='./img', mimetype='image/png')

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
    return redirect('/%s' % identifiant)

run(host='localhost', port=8080)
