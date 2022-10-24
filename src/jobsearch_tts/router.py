#  __author__ = "Vũ Đức Cường"
#  ___date__ = 10/22/22, 4:32 PM
from io import BytesIO

from fastapi import APIRouter
from gtts.tts import gTTS
from fastapi.responses import StreamingResponse
from pytube import Search, YouTube
from pytube.exceptions import VideoUnavailable

router = APIRouter(prefix="/tts", tags=["Text To Speed"])


@router.get("/")
async def text_to_speed(r):
    mp3 = BytesIO()
    tts = gTTS(lang="vi", text="Xin chào")
    tts.write_to_fp(mp3)
    mp3.seek(0)

    return StreamingResponse(mp3, media_type="audio/mp3")


@router.get("/youtube")
async def search_youtube(q: str):
    s = Search(q)
    return dict(data=s.results)


@router.get("youtube_to_mp3")
async def youtube_to_mp3(url: str):
    try:
        yt = YouTube(url)
        return dict(
            data=yt.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )
    except VideoUnavailable:
        raise LookupError("Video is unavaialable")
