from instagrapi import Client
from fastapi import FastAPI

app = FastAPI()

@app.get("/media/user_medias/")
def get_user_medias(user_id: int, amount: int = 10):
    try:
        cl = Client()
        response = cl.user_medias_gql(user_id, amount)
        return {"status": True, "data": response}
    except Exception as e:
        return {"status": False, "data": e.message}

@app.get("/media/info/")
def get_media_info(media_id: int):
    try:
        cl = Client()
        response = cl.media_info_gql(media_id)
        return {"status": True, "data": response}
    except Exception as e:
        return {"status": False, "data": e.message}
