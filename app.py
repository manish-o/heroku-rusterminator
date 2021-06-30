from flask import Flask, render_template, request

from keras.models import load_model

from keras.preprocessing import image
import cv2
import numpy as np

app = Flask(__name__)
dic = {0:'rusted', 1:'not rusted'}




model = load_model('deploy.h5')










def predict_label(img_path):
    img = image.load_img(img_path, target_size=(32, 32))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images)
    if classes[0] < 0.5:
        return "rusted"
    else:
        return "not rusted"
# routes

@app.route("/", methods=['GET', 'POST'])

def main():

	return render_template("index.html")


@app.route("/about")

def about_page():

	return "This Rusterminator, an industrial rust detector"


@app.route("/submit", methods = ['GET', 'POST'])

def get_output():

	if request.method == 'POST':

		img = request.files['my_image']


		img_path = "static/" + img.filename	
		img.save(img_path)


		p = predict_label(img_path)


	return render_template("index.html", prediction = p, img_path = img_path)



if __name__ =='__main__':

	#app.debug = True

	app.run(debug = True)