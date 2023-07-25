from flask import Flask

app = Flask('main')

@app.route('/')
def main():
    return 'Hello'


if __name__ == "__main__":
    app.run(debug=True)