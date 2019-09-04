from flask import Flask, render_template,request,url_for,redirect
from flask_material import Material
from flask_wtf import FlaskForm
from update_data_siswa import update_data
import sqlite3
from _date import timestamp
from update_data_pelanggar import update_pelanggar

conn = sqlite3.connect('db_p1.db', check_same_thread=False) 
app = Flask(__name__)
Material(app)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secrets key"
))
@app.route('/',methods = ['GET','POST'])
def home():
    curr=conn.execute("SELECT* from DATA_SISWA")
    data = curr.fetchall ()
    curr.close()
    return render_template('i_data_siswa.html',form = data)

@app.route('/data_pelanggar',methods = ['GET','POST'])
def data_pelanggar():
    curr=conn.execute("SELECT* from DATA_PELANGGAR")
    data = curr.fetchall ()
    curr.close()
    return render_template('i_siswa_pelanggar.html',data_pelanggar = data)

@app.route('/cari_siswa_pelanggar',methods = ['GET','POST'])
def pelanggar():
    curr=conn.execute("SELECT* from DATA_PELANGGAR")
    data = curr.fetchall ()
    curr.close()
    return render_template('cari_siswa_pelanggar.html',pelanggar = data)

@app.route('/detail_pelanggar',methods = ['GET','POST'])
def detail_pelanggar():
    _id_pelanggar = request.form['id_pelanggar']
    nis = request.form['nis']
    nama = request.form['nama']
    kelas = request.form['kelas']
    jenis = request.form['jenis']
    poin = request.form['poin']
    # update_pelanggar(nis,nama,kelas,jenis,poin,_id_pelanggar)
    return redirect(url_for('/!' ))

@app.route('/simpan_pelanggar',methods = ['POST'])  
def simpan_pelanggar():
    nis = request.form['nis']
    nama = request.form['nama']
    kelas = request.form['kelas']
    jenis = request.form['jenis']
    poin = request.form['poin']
    conn.execute('insert into DATA_PELANGGAR(nis,nama,kelas,jenis,poin,datenum) values (?,?,?,?,?,?)', ( nis,nama,kelas,jenis,poin,timestamp()))
    conn.commit()
    return redirect(url_for('data_pelanggar'))

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

@app.route('/pelanggar',methods = ['POST','GET'])
def edit_pelanggar():
    _id_pelanggar = request.form['id_pelanggar']
    nis = request.form['nis']
    nama = request.form['nama']
    kelas = request.form['kelas']
    jenis = request.form['jenis']
    poin = request.form['poin']
    update_pelanggar(nis,nama,kelas,jenis,poin,_id_pelanggar)
    return redirect(url_for('data_pelanggar' ))

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
    conn.execute("DELETE FROM DATA_SISWA WHERE ide={0}".format((_id)))
    conn.commit()
    return redirect(url_for('home'))

@app.route('/hapus_pelanggar/<string:_id>', methods=["GET"])
def hapus_pelanggar(_id):
    conn.execute("DELETE FROM DATA_PELANGGAR WHERE ide={0}".format((_id)))
    conn.commit()
    return redirect(url_for('data_pelanggar'))

if __name__ == '__main__':
    app.run(debug=True,port=8080)
    

