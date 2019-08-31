import sqlite3
 
def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql =  ''' UPDATE DATA_SISWA
                SET nama = ? ,  jenis_kelamin = ? ,  alamat = ? ,  kelas = ? , hp = ? 
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

def update_data(nama,jenis_kelamin,alamat,kelas,hp_ortu,_id):
    database = 'db_p1.db'
    conn = create_connection(database)
    with conn:
        update_task(conn, (nama,jenis_kelamin,alamat,kelas,hp_ortu,_id))
        print('selesai')
        
 
if __name__ == '__main__':
    update_data("denis","pria","jakarta","1A","62811518818888",1)
    pass