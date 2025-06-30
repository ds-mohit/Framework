# from flask import Flask,render_template,request,url_for
# app=Flask(__name__)

# @app.route('/')

# def home():
#     return render_template('home.html')

# @app.route("/content")
# def content():
#     return render_template('content.html')

# @app.route('/project')
# def content():
#     return render_template('project.html')

# if __name__=='__main__':
#     app.run(debug=True)

from flask import Flask,render_template,request,url_for
import pandas as pd 
import joblib
model = joblib.load('model.pkl')

app=Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route("/content")
def content():
    return render_template('content.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            brand_name = request.form['brand_name']
            owner_name = int(request.form['owner_name'])
            age_bike = int(request.form['age_bike'])
            power_bike = int(request.form['power_bike'])
            kms_driven_bike = int(request.form['kms_driven'])

            bike_number = {'TVS': 0,
                            'Royal Enfield': 1,
                            'Triumph': 2,
                            'Yamaha': 3, 
                            'Honda': 4,
                            'Hero': 5,
                            'Bajaj': 6,
                            'Suzuki': 7,
                            'Benelli': 8,
                            'KTM': 9,
                            'Mahindra': 10,
                            'Kawasaki': 11,
                            'Ducati': 12,
                            'Hyosung': 13,
                            'Harley-Davidson': 14,
                            'Jawa': 15,
                            'BMW': 16,
                            'Indian': 17,
                            'Rajdoot': 18,
                            'LML': 19,
                            'Yezdi': 20,
                            'MV': 21,
                            'Ideal': 22}

                           
            brand_name_encoded = bike_number.get(brand_name)
            input_data = [[owner_name,
                          brand_name_encoded,
                          kms_driven_bike,
                          age_bike,
                          power_bike]]
        
            

            prediction = model.predict(input_data)
            prediction = round(prediction[0],2)
            return render_template('projects.html',prediction=prediction)

        except Exception as e:
            return f"An error occurred: {e}"
        
            
if __name__ == '__main__':
    app.run(debug=True)