from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    joblib.dump(cif, 'Deplying_alg.pkl')
    NB_spam_model = open('Deplying_alg.pkl','rb')
    cif = joblib.load(NB_spam_model)
    
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = cif.predict(vect)
    return render_template('result.html',prediction = my_prediction)
    


     
	
	

	



if __name__ == '__main__':
	app.run(debug=True)
