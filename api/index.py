from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil, a1, a2, ops = None, "", "", ""
    
    if request.method == 'POST':
        try:
            ops = request.form.get('operasi')
            v1 = request.form.get('angka1')
            a1 = float(v1) if v1 else 0
            
            # Operasi Ilmiah (1 Angka)
            if ops in ['sin', 'cos', 'tan', 'akar', 'log']:
                if ops == 'sin': hasil = math.sin(math.radians(a1))
                elif ops == 'cos': hasil = math.cos(math.radians(a1))
                elif ops == 'tan': hasil = math.tan(math.radians(a1))
                elif ops == 'akar': hasil = math.sqrt(a1)
                elif ops == 'log': hasil = math.log10(a1)
            
            # Operasi Standar (2 Angka)
            else:
                v2 = request.form.get('angka2')
                a2 = float(v2) if v2 else 0
                if ops == 'tambah': hasil = a1 + a2
                elif ops == 'kurang': hasil = a1 - a2
                elif ops == 'kali': hasil = a1 * a2
                elif ops == 'bagi': hasil = a1 / a2 if a2 != 0 else "Error"
                elif ops == 'pangkat': hasil = math.pow(a1, a2)
                elif ops == 'persen': hasil = (a1 / 100) * a2

            # MENGHILANGKAN .0 (Hasil angka bulat)
            if isinstance(hasil, float):
                if hasil.is_integer():
                    hasil = int(hasil)
                else:
                    hasil = round(hasil, 8)
        except:
            hasil = "Error"
            
    return render_template('index.html', hasil=hasil, a1=a1, a2=a2, ops=ops)

if __name__ == '__main__':
    app.run(debug=True)