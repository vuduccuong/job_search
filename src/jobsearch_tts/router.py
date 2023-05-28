#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/22/22, 4:32 PM
from io import BytesIO

from fastapi import APIRouter
from gtts.tts import gTTS
from fastapi.responses import StreamingResponse
from pytube import Search, YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError
from starlette.background import BackgroundTasks

from jobsearch_tts.exceptions import YoutubeException

router = APIRouter(prefix="/tts", tags=["Text To Speed"])


@router.get("/")
async def text_to_speed(input: str):
    mp3 = BytesIO()
    tts = gTTS(lang="vi", text=input)
    tts.write_to_fp(mp3)
    mp3.seek(0)

    return StreamingResponse(mp3, media_type="audio/mp3")


@router.get("/youtube")
async def search_youtube(q: str):
    s = Search(q)
    res = []
    for d in s.results:
        data_dict = {
            "title": d._title,
            "thumbnail_url": d.thumbnail_url,
            "video_id": d.video_id,
            "watch_url": d.watch_url,
        }
        res.append(data_dict)

    return dict(data=res)


@router.get("youtube_to_mp3")
async def youtube_to_mp3(url: str, background_task: BackgroundTasks):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()

        def audio_generator():
            audio_data = BytesIO()
            stream.stream_to_buffer(audio_data)
            audio_data.seek(0)
            while True:
                chunk = audio_data.read(4096)
                if not chunk:
                    break
                yield chunk

        return StreamingResponse(audio_generator(), media_type="audio/mp4")
    except RegexMatchError:
        raise YoutubeException.search_exception(message="Url incorrect")
    except VideoUnavailable:
        raise YoutubeException.search_exception(message="Video is unavaialable")
