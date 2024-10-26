### Errors encountered

#### An unexpected error occurred while fetching tweets for OpenAI: Client.get_users_tweets() missing 1 required positional argument: 'id'
#### Fix: update the function call parameter list 
```
self.client.get_users_tweets(id=twitter_account['id'], max_results=tweet_count)
```

#### Error fetching tweets for Bitcoin: 403 Forbidden
##### When authenticating requests to the Twitter API v2 endpoints, you must use keys and tokens from a Twitter developer App that is attached to a Project. You can create a project via the developer portal.
#### Fix: upgrade to Basic API subscription.  Free tier does not allow fetching tweets. 
#### Reference: https://developer.x.com/en/docs/x-api/getting-started/about-x-api