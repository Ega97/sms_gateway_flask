from flask import Flask, render_template
from flask_material import Material


app = Flask(__name__)
Material(app)


# Index
@app.route('/i_data_siswa')
def i_data_siswa():
    return render_template('i_data_siswa.html')


@app.route('/')
def index():

    return render_template("index_bk.html")


if __name__ == '__main__':
    app.run(debug=True )
