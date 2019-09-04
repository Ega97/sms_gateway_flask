import sqlite3

 
def update_task(conn, task): #No	NIS	Nama	Kelas	Jenis Pelanggaran	Poin	Aksi
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql =  ''' UPDATE DATA_PELANGGAR
                SET nis = ? ,  nama = ? ,  kelas = ? ,  jenis = ? , poin = ? 
                WHERE ide  = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except TypeError as e:
        print(e)
    return None

def update_pelanggar(nama,jenis_kelamin,alamat,kelas,hp_ortu,_id):
    database = 'db_p1.db'
    conn = create_connection(database)
    with conn:
        update_task(conn, (nama,jenis_kelamin,alamat,kelas,hp_ortu,_id))
        print('update selesai')
        
 
if __name__ == '__main__':
    update_pelanggar("nis","nama","kelas","jenis", 1 ,1)
    pass