from flask import Flask,render_template,request
import pickle
from sklearn.svm import SVC


app=Flask(__name__)

@app.route('/')
def index():
   return render_template("indexx.html")


@app.route('/predict',methods=["POST"])
def predict():
    if request.method=='POST':
       month=request.form["month"]
       week=request.form["week"]
       vtype=request.form["vtype"]
       Bouncerate=request.form["Bouncerate"]
       exitrate=request.form["exitrate"]

       data=[[int(month),int(week),int(vtype),float(Bouncerate),float(exitrate)]]
       lr=pickle.load(open("shopping.pkl","rb"))
       prediction=lr.predict(data)[0]
       
        
       


        
       
             
      


    
    return render_template("predict.html",prediction=prediction,month=month,vtype=vtype,week=week)
          
@app.route('/')
def other():
   return render_template("indexx.html")


if __name__=='__main__':
    app.run(debug=True)