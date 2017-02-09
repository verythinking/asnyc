from flask import Flask,redirect,render_template,flash,url_for,make_response,Response
from flask_wtf import FlaskForm
from wtforms import SubmitField
import subprocess
from threading import Thread

class SureForm(FlaskForm):
    submit = SubmitField('submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'heloolon'
app.config['DEBUG'] = True

@app.route('/',methods=['GET','POST'])
def index():
    form = SureForm()
    if form.validate_on_submit():
        return redirect(url_for("do"))
    return render_template('index.html',form=form)

@app.route('/do')
def do():
    p = subprocess.Popen('wc -l /tmp/tar.log',shell=True,stdout=subprocess.PIPE)
    line = p.stdout.read().split()[0]
    t = Thread(target=subprocess.call,kwargs=dict(args='python /tmp/3.py',shell=True,stdout=subprocess.PIPE))
    t.start()
    return render_template('do.html',line=line)

@app.route('/getlog/<int:line>')
def get_log(line):
    p = subprocess.Popen('sed -n {}p /tmp/tar.log'.format(line),shell=True,stdout=subprocess.PIPE)
    out_line = p.stdout.read().strip('\n')
    return make_response(out_line)


if __name__ == '__main__':
    app.run('192.168.128.128')