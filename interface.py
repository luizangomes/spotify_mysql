from flask import Flask, render_template, request, json
import mysql.connector
from flaskext.mysql import MySQL

mysql = MySQL()
interface = Flask(__name__)

@interface.route('/')
def main():
    return render_template('index.html')

@interface.route('/create/')
def create():
    return render_template('create.html')

@interface.route('/api/create-gravadora', methods=['POST'])
def createGravadora():
    try:
        _nomeGravadora = request.form['inputNomeGravadora']
        _bioGravadora = request.form['inputBioGravadora']
        _dataGravadora = request.form['inputDataGravadora']
        _statusGravadora = request.form['inputStatusGravadora']
        _paisGravadora = request.form['inputPaisGravadora']
        if _nomeGravadora and _bioGravadora and _dataGravadora and _statusGravadora and _paisGravadora:
            mysql.init_app(interface)
            
            # MySQL configurations
            interface.config['MYSQL_DATABASE_USER'] = 'root'
            interface.config['MYSQL_DATABASE_DB'] = 'SPOTIFY_FINAL'
            interface.config['MYSQL_DATABASE_PASSWORD'] = ''
            mysql.init_app(interface)

            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.callproc('sp_createGravadora', (_nomeGravadora, _bioGravadora, _dataGravadora, _statusGravadora, _paisGravadora))
            data = cursor.fetchall()
            if len(data) == 0:
                conn.commit()
                return json.dumps({'message':'Gravadora created successfully!'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()

@interface.route('/read/')
def read():
    return render_template('read.html')

@interface.route('/update/')
def update():
    return render_template('update.html')

@interface.route('/delete/')
def delete():
    return render_template('delete.html')

if __name__ == "__main__":
    interface.run()