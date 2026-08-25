class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list) # (count, tweetId)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.posts[userId].append((self.count, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # n = number of posts in feed
        # f = following
        # Brute force: Go through n most recent posts of each person the user follows including himself + min heap = f * nlogn
        # Alternative: Queue up the most recent post of each person the user follows and insert the next post of the top = flogf
        # X min heap because you want to evict the least recent of the n most recent. heap will be LR to MR from top to bottom
        # max heap because you want to keep pulling from the user with the most recent post
        heap = [] # (count, userId, index, tweetId)
        feed = []
        following = self.follows[userId]
        following.add(userId)
        for followee in following:
            posts = self.posts[followee]
            if posts:
                count = posts[-1][0]
                index = len(posts) - 1
                tweetId = posts[-1][1]
                heapq.heappush(heap, (-count, followee, index, tweetId))
        while len(feed) < 10 and heap:
            count, user, i, tweetId = heapq.heappop(heap)
            feed.append(tweetId)
            if i > 0:
                posts = self.posts[user]
                count = posts[i-1][0]
                index = i-1
                tweetId = posts[i-1][1]
                heapq.heappush(heap, (-count, user, index, tweetId))
        return feed





    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
# Key method is getNewsFeed where we show the 10 most recent posts from the users' following posts
# Store 'follows' = all the users a particular user follows dict(set)
# Store 'posts' = all the posts of a particular user dict(list)