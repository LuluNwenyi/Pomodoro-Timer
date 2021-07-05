#########################
#### imports ############
#########################

from flask import Flask
from flask import render_template, send_from_directory, url_for, send_file
from werkzeug.exceptions import abort


app = Flask(__name__)

######################################
#### where my file is from ############
######################################
path = "Pomodoro Timer.dmg"


#########################
#### routes #############
#########################

@app.route('/')
def index():

    return render_template('home.html')


@app.route('/download', methods=['GET', 'POST'])
def return_files():
    try:
        return send_file(path, as_attachment=True)

    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)