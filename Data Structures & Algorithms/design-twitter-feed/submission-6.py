class Twitter:

    def __init__(self):
        self.posts = defaultdict(list) # {userId: [(post, timestamp), ...]}
        self.follows = defaultdict(set) # {userId: set(userId, ...)}
        self.time_stamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((tweetId, self.time_stamp))
        self.time_stamp +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        max_heap = []
        feed = []
        for follower in self.follows[userId]:
            posts = self.posts[follower]
            if posts:
                idx = len(posts) - 1
                tweet_id, time = posts[idx]
                heapq.heappush(max_heap, (-time, tweet_id, follower, idx))
        while max_heap and len(feed) < 10:
            neg_time, tweet_id, follower, idx = heapq.heappop(max_heap)
            feed.append(tweet_id)
            if idx:
                tweet_id, time = self.posts[follower][idx-1]
                heapq.heappush(max_heap, (-time, tweet_id, follower, idx-1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)