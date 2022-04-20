from flask import Flask, render_template

interface = Flask(__name__)

@interface.route('/')
def main():
    return render_template('index.html')

@interface.route('/create/')
def create():
    return render_template('create.html')

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