from collections import defaultdict
from typing import List

# Brute Force Approach

class Twitter:
    def __init__(self):
        # Initialize a dictionary to store user posts, where each userId maps to a list of (timestamp, tweetId) tuples
        self.post_data = defaultdict(list)
        # Initialize a dictionary to store follower relationships, where each followerId maps to a set of followeeIds
        self.follower_data = defaultdict(set)
        # Initialize a timestamp to keep track of the order of tweets
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Increment the timestamp for each new tweet
        self.timestamp += 1
        # Append the tweet (with its timestamp) to the user's list of posts
        self.post_data[userId].append((self.timestamp, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        # Initialize a list to collect tweets for the user's news feed
        tweets = []
        
        # Add the user's own tweets to the feed if they exist
        if userId in self.post_data:
            tweets.extend(self.post_data[userId])
        
        # Add tweets from users that the current user follows
        for followeeId in self.follower_data[userId]:
            tweets.extend(self.post_data[followeeId])
        
        # Sort the collected tweets by timestamp in descending order (most recent first)
        tweets.sort(reverse=True)
        
        # Return the tweetIds of the top 10 most recent tweets
        return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followeeId to the followerId's set of followees
        self.follower_data[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followeeId from the followerId's set of followees if it exists
        if followeeId in self.follower_data[followerId]:
            self.follower_data[followerId].remove(followeeId)

# Example usage
twitter = Twitter()
twitter.postTweet(1, 5)  # User 1 posts a tweet with ID 5
print(twitter.getNewsFeed(1))  # User 1's news feed should return [5]
twitter.follow(1, 2)  # User 1 follows user 2
twitter.postTweet(2, 6)  # User 2 posts a tweet with ID 6
print(twitter.getNewsFeed(1))  # User 1's news feed should return [6, 5]
twitter.unfollow(1, 2)  # User 1 unfollows user 2
print(twitter.getNewsFeed(1)) # User 1's news feed should return [5]

'''
Time Complexity:

- postTweet -> O(1) – simple append
- follow -> O(1)
- unfollow -> O(1)
- getNewsFeed:
    Gathering tweets: O(f × t), where f = number of followees and t = average number of tweets per followee
    Sorting all tweets: O(m log m) where m = total tweets collected
    Final slice for top 10: O(10) → O(1)

Space Complexity:

- postTweet -> O(1) per call
- follow -> O(1) per call (adds one edge)
- unfollow -> O(1)
- All tweets collected into a list → O(m)
'''

# Optimal Approach

import heapq

class Twitter:

    def __init__(self):
        self.post_data = defaultdict(list)
        self.follower_data = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.post_data[userId].append((self.timestamp, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        # Get tweets of the user and their followees
        users = set(self.follower_data[userId])
        users.add(userId)

        for uid in users:
            for tweet in self.post_data[uid]:
                heapq.heappush(minHeap, tweet)  # Push (timestamp, tweetId)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)  # Remove the oldest

        # Extract tweets from heap in reverse time order
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])  # Only tweetId
        return res[::-1]  # Most recent first

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_data[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_data[followerId]:
            self.follower_data[followerId].remove(followeeId)

# Example usage
twitter = Twitter()
twitter.postTweet(1, 5)  # User 1 posts a tweet with ID 5
print(twitter.getNewsFeed(1))  # User 1's news feed should return [5]
twitter.follow(1, 2)  # User 1 follows user 2
twitter.postTweet(2, 6)  # User 2 posts a tweet with ID 6
print(twitter.getNewsFeed(1))  # User 1's news feed should return [6, 5]
twitter.unfollow(1, 2)  # User 1 unfollows user 2
print(twitter.getNewsFeed(1)) # User 1's news feed should return [5]

'''
Time Complexity:

- postTweet -> O(1) – simple append
- follow -> O(1)
- unfollow -> O(1)
- getNewsFeed:
    Gathering tweets: O(f × t), where f = number of followees and t = average number of tweets per followee
    Heap operations (max 10 items): O(m log 10) = O(m), m = total tweets fetched (f × t)
    Pop all 10 tweets from heap: O(10) -> O(1)
    Reverse the list: O(10) -> O(1)

Space Complexity:

- postTweet -> O(1) per call
- follow -> O(1) per call (adds one edge)
- unfollow -> O(1)
- Min-heap size is at most 10 → O(1)
- Result list contains ≤10 tweets → O(1)
'''