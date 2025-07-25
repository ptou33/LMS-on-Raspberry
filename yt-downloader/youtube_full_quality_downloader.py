import yt_dlp
import sys

def download_youtube_full_and_audio(url):
    # Subtitles: include English, Italian, Chinese (Simplified + Traditional)
    subtitle_languages = ['en', 'it', 'zh', 'zh-Hans', 'zh-Hant', 'auto']

    # 1. Full-quality video+audio
    video_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',
        'outtmpl': '%(title)s.%(ext)s',
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': subtitle_languages,
        'writeinfojson': False,
        'writethumbnail': True,
        'embedthumbnail': True,
        'addmetadata': True,
        'embedsubtitles': True,
        'postprocessors': [
            {'key': 'FFmpegMetadata'},
            {'key': 'EmbedThumbnail'},
        ],
        'noplaylist': True,
        'quiet': False,
        'progress_hooks': [lambda d: print(f"[VIDEO] [{d['status']}] {d.get('filename', '')}")]
    }

    # 2. Best-quality audio-only download (no re-encoding)
    audio_opts = {
        #'format': 'bestaudio/best',
        'format': 'bestaudio[ext=m4a]/bestaudio[ext=opus]/bestaudio',
        'outtmpl': '%(title)s_audio.%(ext)s',
        'writeinfojson': False,
        'writethumbnail': True,
        'embedthumbnail': True,
        'addmetadata': True,
        'postprocessors': [
            {'key': 'FFmpegMetadata'},
            {'key': 'EmbedThumbnail'},
        ],
        'noplaylist': True,
        'quiet': False,
        'progress_hooks': [lambda d: print(f"[AUDIO] [{d['status']}] {d.get('filename', '')}")]
    }

    with yt_dlp.YoutubeDL(video_opts) as ydl:
        ydl.download([url])

    with yt_dlp.YoutubeDL(audio_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube_full_quality_downloader.py <youtube_url>")
        sys.exit(1)
    download_youtube_full_and_audio(sys.argv[1])
