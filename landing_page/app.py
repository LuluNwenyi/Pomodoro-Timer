#########################
#### imports ############
#########################

from flask import Flask
from flask import render_template, send_from_directory, url_for
from flask.helpers import send_file
from werkzeug.exceptions import abort

app = Flask(__name__)

######################################
#### wheremy file is from ############
######################################
timer_app = "/Users/user/Desktop/pomdoro_landing_page/static/Pomodoro Timer.zip"


#########################
#### routes #############
#########################

@app.route('/')
def index():

    return render_template('home.html')


@app.route('/download', methods=['GET', 'POST'])
def return_files():
    try:
        return send_file(timer_app, as_attachment=True)

    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)