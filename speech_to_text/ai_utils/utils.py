import base64
from pydub import AudioSegment
import io

def decodeSound(imgstring):
    # Decode base64 string directly into an AudioSegment object
    decoded_data = base64.b64decode(imgstring)
    audio_segment = AudioSegment.from_file(io.BytesIO(decoded_data))

    return audio_segment