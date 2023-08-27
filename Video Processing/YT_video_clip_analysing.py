from googleapiclient.discovery import build

# Replace with your API key
API_KEY = 'YOUR_API_KEY'

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Video ID of the YouTube video
video_id = 'YOUR_VIDEO_ID'

# Get video statistics (view count over time)
video_stats_response = youtube.videos().list(
    part='statistics',
    id=video_id
).execute()

view_count_data = video_stats_response['items'][0]['statistics']['viewCount']

# Convert view count data to a list of integers
view_count_list = [int(view_count) for view_count in view_count_data.split(',')]

# Calculate increases in view count for each interval
view_count_increases = [view_count_list[i+1] - view_count_list[i] for i in range(len(view_count_list)-1)]

# Define the length of time intervals in seconds (adjust as needed)
interval_length = 60  # 1 minute intervals

# Analyze view count increases and identify most viewed sections
most_viewed_sections = []
for i, increase in enumerate(view_count_increases):
    start_time = i * interval_length
    end_time = (i + 1) * interval_length
    most_viewed_sections.append((start_time, end_time, increase))

# Sort sections by view count increase in descending order
most_viewed_sections.sort(key=lambda x: x[2], reverse=True)

# Print the most viewed sections
print(f"Most Viewed Sections of '{video_id}':")
for section in most_viewed_sections:
    start_time = section[0]
    end_time = section[1]
    increase = section[2]
    print(f"Time: {start_time}-{end_time} seconds | Increase in Views: {increase}")
