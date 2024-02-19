from flask import Flask,request,jsonify,render_template
import json
import logging


obj=Flask(__name__)


@obj.route('/')
def welcome():
    return "Welcome to Flask"

'''
@obj.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="multiply":
        result=int(number1)*int(number2)
    elif operation=="division":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return "the operation is {} and the result is {}".format(operation,result)
'''


@obj.route('/cal', methods=["GET"])
def math_operator():
    data = request.json
    operation = data["operation"]
    number1 = float(data["number1"])
    number2 = float(data["number2"])
    
    if operation == "add":
        result = number1 + number2
    elif operation == "multiply":
        result = number1 * number2
    elif operation == "divide":
        result = number1 / number2
    else:
        result = number1 - number2
    
    return f'operation: {operation}, result: {result}'
    



@obj.route('/calculate', methods=['POST','GET'])
def calculate():
    if(request.method == "GET"):
        return render_template('calculator.html')
    else:
        number1 = float(request.form['number1'])
        number2 = float(request.form['number2'])
        operation = request.form['operation']
        if operation == 'add':
            result = number1 + number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            result = number1 / number2
        else:
            result = 'Invalid operation'
        return render_template('calculator.html', result=result)





        
    


print(__name__)

if __name__ == '__main__':
    logging.basicConfig(filename="myapp.log", level=logging.INFO)

    obj.run()