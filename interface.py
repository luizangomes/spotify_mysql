from flask import Flask, render_template

interface = Flask(__name__)

@interface.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    interface.run()