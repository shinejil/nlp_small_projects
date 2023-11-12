from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin


import speechToText
from ai_utils.utils import decodeSound
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index2.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['sound']

    # Decode the sound directly into an AudioSegment object
    decoded_sound = decodeSound(image)

    # Export the decoded sound to a temporary WAV file
    #temp_wav_file = "temp_audio.wav"
    decoded_sound.export("audio123.wav", format="wav")

    # Perform speech-to-text processing on the WAV file
    result = speechToText.speech2Text("audio123.wav")

    # Optionally, you can remove the temporary WAV file
    #os.remove(temp_wav_file)

    return jsonify({"Result": str(result)})


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=5000, debug=True)