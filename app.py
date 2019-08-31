from flask import Flask, render_template,request,url_for,redirect
from flask_material import Material
from flask_wtf import FlaskForm
from update_sql import update_data
import sqlite3
conn = sqlite3.connect('db_p1.db', check_same_thread=False) 
app = Flask(__name__)
Material(app)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
@app.route('/home',methods = ['GET','POST'])
def home():
    curr=conn.execute("SELECT* from DATA_SISWA")
    data = curr.fetchall ()
    curr.close()
    return render_template('i_data_siswa.html',form = data)

@app.route('/simpan',methods = ['POST'])
def simpan():
    nama = request.form['nama']
    jenis_kelamin = request.form['jk']
    alamat = request.form['alamat']
    kelas = request.form['kelas']
    hp_ortu = request.form['hp_ortu']
    conn.execute('insert into DATA_SISWA( nama,jenis_kelamin,alamat,kelas,hp,datenum) values (?,?,?,?,?,?)', ( nama,jenis_kelamin,alamat,kelas,hp_ortu,1))
    conn.commit()
    return redirect(url_for('home'))

@app.route('/edit',methods = ['POST'])
def edit():
    _id = request.form['id']
    nama = request.form['nama']
    jenis_kelamin = request.form['jk']
    alamat = request.form['alamat']
    kelas = request.form['kelas']
    hp_ortu = request.form['hp_ortu']
    update_data(nama,jenis_kelamin,alamat,kelas,hp_ortu,_id)
    return redirect(url_for('home'))

@app.route('/hapus/<string:_id>', methods=["GET"])
def hapus(_id):
    # sql = '''SELECT* FROM {0} WHERE hp= {1} AND status= {2}'''.format("'MITRA'",query ,"'ON'")
    conn.execute("DELETE FROM DATA_SISWA WHERE ide={0}".format((_id)))
    conn.commit()
    return redirect(url_for('home'))

 
@app.route('/i_data_siswa',methods = ['GET','POST'])
def i_data_siswa():
    return render_template('i_data_siswa.html')
 
@app.route('/')
def index():

    return render_template("index_bk.html")
 
if __name__ == '__main__':
    app.run(debug=True,port=8080)
    

