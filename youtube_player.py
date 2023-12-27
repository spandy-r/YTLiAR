from googleapiclient.discovery import build
import argparse
import webbrowser

def search_and_play(api_key, query):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=1
    )
    response = request.execute()

    if 'items' in response and response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        print(f"Playing: {response['items'][0]['snippet']['title']}")
        webbrowser.open(video_url)
    else:
        print("No videos found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search and play YouTube videos.")
    parser.add_argument("api_key", help="USE_YOUR_API_KEY")
    parser.add_argument("query", help="Search query for the YouTube video.")
    args = parser.parse_args()

    search_and_play(args.api_key, args.query)
