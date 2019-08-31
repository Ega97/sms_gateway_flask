import sqlite3
conn = sqlite3.connect('db_p1.db') #, check_same_thread=False


def create_db():
    conn = sqlite3.connect('db_p1.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
    c.execute('''CREATE TABLE DATA_SISWA
                (
                [ide] INTEGER PRIMARY KEY AUTOINCREMENT,
                [nama] text,        
                [jenis_kelamin] text, 
                [alamat] text, 
                [kelas] text, 
                [hp] text,
                [datenum] integer)''')
    conn.commit()
def edit_data_siswa( nama,jenis_kelamin,alamat,kelas,hp,datenum,id):
    conn.execute('UPDATE DATA_SISWA( nama,jenis_kelamin,alamat,kelas,hp,datenum) values (?,?,?,?,?,?  ) WHERE ide is {}', ( nama,jenis_kelamin,alamat,kelas,hp,datenum,1))
    conn.commit()
    print("updated")
 
   
def add_data_siswa( nama,jenis_kelamin,alamat,kelas,hp,datenum):
    conn.execute('insert into DATA_SISWA( nama,jenis_kelamin,alamat,kelas,hp,datenum) values (?,?,?,?,?,?)', ( nama,jenis_kelamin,alamat,kelas,hp,datenum))
    conn.commit()
    print("done")

def fetch_data_siswa():
    curr=conn.execute("SELECT* from DATA_SISWA")
    data = curr.fetchall ()
    conn.commit()
    for row in data : 
        print(row)
if __name__ == "__main__":
    # create_db()
    # edit_data_siswa("Debay2","pria","Balam","9A","6281278376630",2019083020100,2)
    fetch_data_siswa()