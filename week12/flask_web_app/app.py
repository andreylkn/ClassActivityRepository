from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/page_2/<name>')
def print_hellow(name):
    return f"<p>Hello {name}, world!</p>"

customers =  [
                {'name': 'Andrew', 'email': 'andrew@gmail.com', 'note': 'w erwe rwasdas  asd er' },
                {'name': 'David', 'email': 'devid@gmail.com', 'note': 'adsfafasfas a asfa sf a'}
            ]
@app.route('/info', methods=['GET', 'POST'])
def form_data_processing():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        note = request.form.get('note')
        customers.append({'name': name, 'email': email, 'note': note})
        return render_template("index.html", customers=customers)

@app.route('/')
def home():
    return render_template('index.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)
