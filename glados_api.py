from fastapi import FastAPI
from fastapi.responses import FileResponse



'''
glados model setup
'''
import glados_class
glados_tts = glados_class.GladosBot()



glados_tta_api = FastAPI()
audio_output_file = "output.wav"
@glados_tta_api.get("/")
async def root():
    return {"message":"Hello World"}


@glados_tta_api.get("/glados/{text}")
async def generate_glados_speech(text):
    global glados_tts
    return FileResponse(glados_tts.get_voice())


