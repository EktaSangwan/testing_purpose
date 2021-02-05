from flask import Flask,request, render_template,url_for,redirect


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/name_enter', methods=['POST'])
def name_enter():
    print(request.form)
    print(request.form['name'])
    data = {'name':request.form['name']}
    return render_template('home.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)
    