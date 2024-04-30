from flask import Flask, render_template,request,jsonify
import config
from utils import AdultAutism, ToddlerAutism
import numpy as np


app = Flask(__name__)

@app.route("/")
def get_homepage():
    return render_template("homepage.html")

@app.route('/adultpredict', methods=['POST'])
def adultpredict():
    if request.method == "POST":
        data = request.json
        A1 = float(data.get('A1'))
        A2 = float(data.get('A2'))
        A3 = float(data.get('A3'))
        A4 = float(data.get('A4'))
        A5 = float(data.get('A5'))
        A6 = float(data.get('A6'))
        A7 = float(data.get('A7'))
        A8 = float(data.get('A8'))
        A9 = float(data.get('A9'))
        A10 = float(data.get('A10'))
        age = float(data.get('age'))
        jaundice = float(data.get('jaundice'))
        autism = float(data.get('autism'))
        gender = float(data.get('gender'))

        # Create an instance of the Autism class
        autism_model = AdultAutism(A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, age, gender,jaundice, autism)
        
        # Call the get_autism method on the instance
        result = autism_model.get_adultautism()
        result_list = result.tolist()
        return jsonify({'autism_prediction': result_list})
    
        
@app.route('/toddlerpredict', methods=['POST'])
def toddlerpredict():
    if request.method == "POST":
        data = request.json
        A1 = float(data.get('A1'))
        A2 = float(data.get('A2'))
        A3 = float(data.get('A3'))
        A4 = float(data.get('A4'))
        A5 = float(data.get('A5'))
        A6 = float(data.get('A6'))
        A7 = float(data.get('A7'))
        A8 = float(data.get('A8'))
        A9 = float(data.get('A9'))
        A10 = float(data.get('A10'))
        age = float(data.get('age'))
        Jaundice = float(data.get('Jaundice'))
        autism = float(data.get('autism'))
        gender = float(data.get('gender'))

        # Create an instance of the Autism class
        autism_model = ToddlerAutism(A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, age, gender,Jaundice, autism)
        
        # Call the get_autism method on the instance
        result = autism_model.get_toddlerautism()
        result_list = result.tolist()
        return jsonify({'autism_prediction': result_list})
    
        
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config.PORT_NUMBER, debug=False)




