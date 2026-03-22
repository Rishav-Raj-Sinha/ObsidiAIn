from youtube_transcript_api import YouTubeTranscriptApi

def pull(id: str):
    ytt_api = YouTubeTranscriptApi()
    fetched = ytt_api.fetch(id)
    transcript_list = []
    for snippet in fetched:
        transcript_list.append(snippet.text)
    transcript = "/n".join(transcript_list)    
    return transcript

#pull(input())
