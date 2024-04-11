from googleapiclient.discovery import build
import pandas as pd


def youtube_etl():
    API_KEY = "AIzaSyD2TUjjwKRmoiJ6d6CdbdK1TkxmnHjKYz0"

    CHANNEL_ID = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'  #Google Developers channel

    # Function to retrieve video data
    def get_channel_videos(channel_id, api_key):
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Get the playlist ID of the uploaded videos of the channel
        playlist_items = youtube.channels().list(part='contentDetails', id=channel_id).execute()
        playlist_id = playlist_items['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Retrieve video data from the playlist
        videos = []
        next_page_token = None

        while True:
            playlist_response = youtube.playlistItems().list(
                part='snippet',
                playlistId=playlist_id,
                maxResults=50,  # Maximum number of results per page
                pageToken=next_page_token
            ).execute()

            videos.extend(playlist_response['items'])
            next_page_token = playlist_response.get('nextPageToken')

            if not next_page_token:
                break

        return videos


    # Function to extract relevant information from video data
    def extract_video_info(videos):
        extracted_info = []

        for video in videos:
            video_id = video['snippet']['resourceId']['videoId']
            title = video['snippet']['title']
            description = video['snippet']['description']
            published_at = video['snippet']['publishedAt']
            thumbnail_url = video['snippet']['thumbnails']['default']['url']

            # Append relevant information to the list
            extracted_info.append({
                'video_id': video_id,
                'title': title,
                'description': description,
                'published_at': published_at,
                'thumbnail_url': thumbnail_url
            })

        return extracted_info

    videos = get_channel_videos(CHANNEL_ID, API_KEY)
    extracted_info = extract_video_info(videos)
    df=pd.DataFrame(extracted_info)
    print(df)
    df.to_csv("Youtubedata.csv")

