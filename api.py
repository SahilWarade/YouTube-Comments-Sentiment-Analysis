from googleapiclient.discovery import build
import subprocess

def create_comments(vid_id):
#This key works till 95000 comments , after that change api key or need to take 300$ subscription of google ypoutube api v3
    API_KEY = "AIzaSyAI_pp6cVpDKzJqkWzlldgU94I_cgvPCYM" 
    VIDEO_ID = vid_id

    youtube = build("youtube", "v3", developerKey=API_KEY)

    # Retrieve video comments
    comments = []

    # Initialize nextPageToken for pagination
    next_page_token = None

    while True:
        # Make request to fetch comments
        comments_request = youtube.commentThreads().list(
            part="snippet",
            videoId=VIDEO_ID,
            textFormat="plainText",
            pageToken=next_page_token
        )
        comments_response = comments_request.execute()

        # Extract comments from response
        for item in comments_response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        # Check if there are more pages of comments
        next_page_token = comments_response.get("nextPageToken")

        # Break the loop if no more pages
        if not next_page_token:
            break

    # Save comments to a file
    output_file = "output_file.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        for comment in comments:
            file.write(comment + '\n')

    print(f"Comments saved to '{output_file}' successfully!")

    return f"{output_file}"

    # Execute another Python file at the end
    # second_file_path = "emotion.py"
    # subprocess.run(["python3", second_file_path])
