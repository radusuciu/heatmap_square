from flask import Blueprint, jsonify, request, render_template, send_file, make_response
from flask_security import login_required
from heatmap_square import db
import heatmap_square.api as api
import base64


home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')


@home.route('/')
def index():
    bootstrap = None
    return render_template('index.html', bootstrap=bootstrap)

@home.route('/heatmap', methods=['POST'])
def heatmap():
    print('hello')
    data = request.get_json()['data']
    img_io = api.heatmap(data)
    img = 'data:image/png;base64,{}'.format(
        base64.b64encode(img_io.read()).decode('UTF-8')
    )
    img_io.close()
    return make_response(img)

@home.route('/private')
@login_required
def private():
    return 'hello'


@home.before_app_first_request
def create_db():
    db.create_all()
    db.session.commit()
