main.py
form flask import flask,render_template
app=flask(__name__)
@app.route('/')
def home();
return render_template('index.html',file="home page")
if__name__=='__main__':
app.run(host='127.0.0.1',port=8080,debug=true)

