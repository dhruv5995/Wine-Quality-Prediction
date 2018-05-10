from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
	if request.method=='POST':
		result=request.form
		# import pdb; pdb.set_trace()
		val1 = float(result['var1'])
		val2 = float(result['var2'])
		val3 = float(result['var3'])
		val4 = float(result['var4'])
		val5 = float(result['var5'])
		val6 = float(result['var6'])
		val7 = float(result['var7'])
		val8 = float(result['var8'])
		val9 = float(result['var9'])
		val10 = float(result['var10'])
		val11 = float(result['var11'])
		val12 = float(result['var12'])

		inp = np.array([])
		inp = np.append(inp, [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12]).reshape(-1,1)

		with open("model_rcf.pkl", "rb") as f:
			model = pickle.load(f)

		pred = model.predict(inp)

		if pred == 0:
			prediction = "It's bad wine"
		else:
			prediction = "It's good wine"

		return render_template('home.html', prediction = prediction)

if __name__ == '__main__':
	app.run()