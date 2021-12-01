import api_tokens
import tweepy

tweepy_client = tweepy.Client(
    bearer_token=api_tokens.BEARER_TOKEN,
    consumer_key=api_tokens.API_KEY,
    consumer_secret=api_tokens.API_KEY_SECRET,
    access_token=api_tokens.ACCESS_TOKEN,
    access_token_secret=api_tokens.ACCESS_TOKEN_SECRET
)

response = tweepy_client.get_user(username='lamonmathieu')
print(response)

response = tweepy_client.get_users_tweets(id=response.data.id, exclude='retweets,replies', max_results=10, tweet_fields='public_metrics')
print(response)