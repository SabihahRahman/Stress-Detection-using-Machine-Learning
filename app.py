from flask import Flask, render_template, Response
import test
from test import VideoCamera
app = Flask(__name__, template_folder='C:/Users/sabi/Desktop/Naveena_Stress/code/templates')
@app.route('/')
def index():
    # Main page
    return render_template('index.html')
def gen(test):
    """Video streaming generator function."""
    while True:
        frame= test.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
@app.route("/predict" , methods=['GET','POST'])
def predict():  
    import test_face
    print("done")
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    #app.run(debug=False,threaded=False)
    app.debug=True
    app.run(host='0.0.0.0', port= 5000)