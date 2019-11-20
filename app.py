from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='/assets')

@app.route('/')
def start():
    return render_template('index.html')

# Definindo rotas
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('assets/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('assets/css', path)


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('assets/images', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('assets/fonts', path)


@app.route('/sobre/')
def about():
    print("Eulálio é feio!")
    print(1+1)
    return render_template('sobre.html')

if __name__ == '__main__':
   app.run(debug = True)