from app.api import bp
from flask import current_app, jsonify, render_template, send_from_directory, url_for, redirect
from flask import request
from flask import render_template
from flask import flash

@bp.route('/test/flutter')
def serve_index():
    print("current_app.static_folder = "+ current_app.static_folder)
    return send_from_directory(current_app.static_folder, 'index.html')

@bp.route('/static/<path:filename>')
def serve_static(filename):
    print(f"Serving static file: {filename}")
    return send_from_directory(current_app.static_folder, filename)


@bp.route('/test')
def test():
    return jsonify({"status":"ok"})

@bp.route('/test/<username>')
def username(username):
    return jsonify({"user":username})

@bp.route('/test/listAPI')
def listAPI():
    routes = []
    for rule in current_app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods - {'HEAD', 'OPTIONS'}),
            'rule': str(rule)
        })
    return jsonify(routes)

@bp.route('/a')
def url_for_a():
    return 'here is a'

@bp.route('/b')
def b():
    return redirect(url_for('url_for_a'))

@bp.route('/test/age')
def userage():
    age = 3
    return 'i am '+age+'years'

@bp.route('/index')
def index():
    return render_template('abc.html')

@bp.route('/index/<user>')
def index_user(user):
    return render_template('abc.html', user_template=user)


@bp.route('/test/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return  'Hello' + request.values['username']

    return "<form method='post' action='/api/test/login'><input type='text' name='username' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"

@bp.route('/test/login_template', methods=['GET', 'POST'])
def login_template():
    if request.method == 'POST':
        return 'Hello ' + request.values['username']

    return render_template('login.html')

@bp.route('/test/login_switch', methods=['GET', 'POST'])
def login_switch():
    if request.method == 'POST':
        return redirect(url_for('api.index_user', user=request.form.get('username')))

    return render_template('login.html')

@bp.route('/test/login_hello', methods=['GET', 'POST'])
def login_hello():
    if request.method == 'POST':
        if(login_check(request.form['username'], request.form['password'])):
            flash('Login Success!')
            return render_template('hello.html', username=request.form.get('username'))

    print('login_hello')
    return render_template('login_user.html')

def login_check(username, password):
    if username == 'admin' and password == 'hello':
        return True
    else: 
        return False


