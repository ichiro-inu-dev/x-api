import os
import asyncio
import datetime
from typing import List, Dict
from dotenv import load_dotenv
import tweepy

load_dotenv()  # Load environment variables from .env file

class TwitterFeed:
    def __init__(self, twitter_accounts: List[str]):
        self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
        print(f"bearer_token: {self.bearer_token}")
        self.twitter_accounts = twitter_accounts
        print(f"twitter_accounts: {self.twitter_accounts}")
        self.client = None

    async def initialize_client(self):
        """Initialize Tweepy client with OAuth2 Bearer Token."""
        await self.refresh_token()

    async def refresh_token(self):
        """Refresh the OAuth2 Bearer Token if expired."""
        try:
            self.client = tweepy.Client(bearer_token=self.bearer_token)
        except Exception as e:
            print(f"Failed to refresh token: {e}")

    async def fetch_tweets(self, username: str, tweet_count: int = 10) -> List[Dict]:
        """Fetch the last `tweet_count` tweets for a given username."""
        try:
            user = self.client.get_user(username=username)
            if user.data is None:
                print(f"User {username} not found.")
                return []
            
            tweets = self.client.get_users_tweets(user_id=user.data.id, max_results=tweet_count)
            return [{"id": tweet.id, "text": tweet.text} for tweet in tweets.data] if tweets.data else []
        except tweepy.TweepyException as e:
            print(f"Error fetching tweets for {username}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while fetching tweets for {username}: {e}")
        return []

    async def periodic_fetch(self, interval: int = 300):
        """Fetch the last 10 tweets for each account in TWITTER_ACCOUNTS every `interval` seconds."""
        while True:
            for account in self.twitter_accounts:
                tweets = await self.fetch_tweets(account)
                print(f"Fetched {len(tweets)} tweets for {account}")
            await asyncio.sleep(interval)

    async def run(self):
        """Initialize client and start periodic fetching of tweets."""
        await self.initialize_client()
        await self.periodic_fetch()

# Global error handling
def handle_global_error(loop, context):
    print(f"Global error occurred: {context['message']}")

# Example usage
if __name__ == "__main__":
    # List of Twitter accounts to monitor
    TWITTER_ACCOUNTS = [
        'OpenAI',
        'DeepMind',
        'sama',
        'bitcoin'
        ]

    twitter_feed = TwitterFeed(twitter_accounts=TWITTER_ACCOUNTS)

    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handle_global_error)
    try:
        loop.run_until_complete(twitter_feed.run())
    finally:
        loop.close()