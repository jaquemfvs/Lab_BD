from youtool import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from pymongo import MongoClient
from datetime import datetime
from itertools import islice
import re

#MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["youtube_data"]
collection = db["videos"]

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None

def format_datetime(dt):
    if isinstance(dt, datetime):
        return dt.isoformat()
    return dt

def get_video_data(video_id, yt=None):
    print(f"Coletando dados do vídeo: {video_id}")

    try:
        info = next(yt.videos_infos([video_id]))
    except Exception as e:
        print(f"Falha ao buscar info do vídeo: {e}")
        return None

    video_data = {
        "video_id": video_id,
        "title": info.get("title"),
        "description": info.get("description"),
        "statistics": {
            "views": info.get("views"),
            "likes": info.get("likes"),
            "dislikes": info.get("dislikes", 0),
        },
        "comments": [],
        "transcript": [],
        "livechat": [],
    }

    print("Coletando comentários")
    try:
        comments_generator = yt.video_comments(video_id)
        comments_list = list(islice(comments_generator, 100))
        if not comments_list:
            raise StopIteration
        comments_sorted = sorted(comments_list, key=lambda c: c.get("like_count", 0))
        video_data["comments"] = comments_sorted
    except StopIteration:
        print("[WARNING] Nenhum comentário encontrado para esse vídeo.")
    except Exception as e:
        print(f"Erro ao coletar comentários: {e}")

    print("Coletando transcrição...")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["pt", "en"])
        full_transcript = " ".join([item["text"] for item in transcript])
        video_data["transcript"] = full_transcript

    except (TranscriptsDisabled, NoTranscriptFound):
        print("Sem transcrição disponível.")
    except Exception as e:
        print(f"[ERRO] Transcrição falhou: {e}")

    print("Coletando mensagens de live chat")
    try:
        for chat in yt.video_livechat(video_id):
            chat_data = {
                "author": chat.get("author_name"),
                "message": chat.get("message"),
                "timestamp": format_datetime(chat.get("timestamp")),
            }
            if "money_amount" in chat:
                chat_data["superchat"] = {
                    "amount": chat.get("money_amount"),
                    "currency": chat.get("money_currency")
                }
            video_data["livechat"].append(chat_data)
    except Exception as e:
        print(f"Live chat indisponível: {e}")

    return video_data

def save_to_mongodb(video_data):
    if video_data:
        collection.update_one(
            {"video_id": video_data["video_id"]},
            {"$set": video_data},
            upsert=True
        )
        print("Dados salvos no MongoDB.")
    else:
        print("Nenhum dado para salvar.")

if __name__ == "__main__":

    api_key = "API_KEY"  # Substitua pela sua chave de API
    url = input("Cole a URL do vídeo: ").strip()

    video_id = extract_video_id(url)
    if not video_id:
        print("[ERRO] URL inválida")
        exit(1)

    yt = YouTube([api_key], disable_ipv6=True)

    data = get_video_data(video_id, yt=yt)
    save_to_mongodb(data)
    print("Coleta concluída!")