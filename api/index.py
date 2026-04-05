import os
from flask import Flask, render_template, request

# Baris ini sangat penting agar Vercel bisa menemukan folder templates
app = Flask(__name__, template_folder='../templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = ""
    a1 = ""
    a2 = ""
    ops = ""
    
    if request.method == 'POST':
        try:
            a1 = request.form.get('a1', '')
            a2 = request.form.get('a2', '')
            ops = request.form.get('ops', '')
            
            if a1 and a2 and ops:
                num1 = float(a1)
                num2 = float(a2)
                
                if ops == '+':
                    hasil = num1 + num2
                elif ops == '-':
                    hasil = num1 - num2
                elif ops == '*':
                    hasil = num1 * num2
                elif ops == '/':
                    if num2 != 0:
                        hasil = num1 / num2
                    else:
                        hasil = "Error (Bagi 0)"
                
                # Membulatkan hasil jika angka desimal terlalu panjang
                if isinstance(hasil, float):
                    if hasil.is_integer():
                        hasil = int(hasil)
                    else:
                        hasil = round(hasil, 8)
        except Exception:
            hasil = "Error"
            
    return render_template('index.html', hasil=hasil, a1=a1, a2=a2, ops=ops)

# Baris ini penting untuk menjalankan Flask secara lokal (Testing)
if __name__ == '__main__':
    app.run(debug=True)
