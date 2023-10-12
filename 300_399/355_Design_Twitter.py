import heapq
from collections import defaultdict, deque
from itertools import count, islice


class Twitter:
    def __init__(self):
        self.timer = count(step=-1)
        self.tweets = defaultdict(deque)
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((next(self.timer), tweetId))

        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))

        return [t for _, t in islice(tweets, 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
