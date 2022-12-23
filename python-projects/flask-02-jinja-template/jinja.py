from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 =7000 , number2=9000)

@app.route('/mult')
def number():
  num1, num2 =1213 ,1313
  return render_template('body.html', var1=num1, var2=num2 ,sum = num1* num2)




if __name__=="__main__":
    app.run(debug=True,port=5000)

