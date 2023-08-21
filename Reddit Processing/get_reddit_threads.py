import praw
import openai

# Reddit API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
user_agent = 'YOUR_USER_AGENT'

# OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Subreddit to search
subreddit_name = 'askreddit'
subreddit = reddit.subreddit(subreddit_name)

# Get a random submission from the subreddit
random_submission = random.choice(list(subreddit.new(limit=100)))

# Extract the question from the submission
question = random_submission.title

# Generate an answer using OpenAI's GPT-3
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=question,
    max_tokens=100
)
suitable_answer = response.choices[0].text.strip()

# Print the extracted question and generated suitable answer
print("Random Question:")
print(question)
print("\nGenerated Suitable Answer:")
print(suitable_answer)
