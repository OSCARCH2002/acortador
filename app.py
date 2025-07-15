from flask import Flask, request, redirect, render_template, url_for, send_file
import string
import random
import io
import qrcode

app = Flask(__name__)

url_map = {}

# Generar un código corto aleatorio
def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(chars, k=length))
        if code not in url_map:
            return code

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        code = generate_short_code()
        url_map[code] = original_url
        # Redirige usando PRG
        return redirect(url_for('index', code=code))
    # GET: muestra solo si hay code en query string
    code = request.args.get('code')
    short_url = qr_url = None
    if code and code in url_map:
        short_url = request.host_url + code
        qr_url = url_for('qr_code', code=code)
    return render_template('index.html', short_url=short_url, qr_url=qr_url)

@app.route('/<code>')
def redirect_short_url(code):
    original_url = url_map.get(code)
    if original_url:
        return redirect(original_url)
    return 'Enlace no encontrado', 404

@app.route('/qr/<code>')
def qr_code(code):
    short_url = request.host_url + code
    img = qrcode.make(short_url)
    buf = io.BytesIO()
    img.save(buf, 'PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True) 