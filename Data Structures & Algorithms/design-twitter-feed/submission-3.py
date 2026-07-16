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
        
        def follower_with_later_post(a, b):
            a_time = self.posts[a][-1][1] if a and self.posts[a] else 0
            b_time = self.posts[b][-1][1] if b and self.posts[b] else 0
            return a if a_time >= b_time else b

        def get_most_recent_post_follower(userId):
            target_follower = 0
            for follower in self.follows[userId]:
                target_follower = follower_with_later_post(target_follower, follower)
            return target_follower
    
        recent_posts = deque() # move them onto here
        feed = [] # add id here before putting back into posts map
        for _ in range(10):
            target_follower = get_most_recent_post_follower(userId)
            # No more posts
            if target_follower == 0:
                break
            # Have the most recent post
            tweet_id, time = self.posts[target_follower].pop()
            recent_posts.append((target_follower, tweet_id, time))
        # Assemble feed -> forward
        for post in recent_posts:
            feed.append(post[1])
        # Put back posts <- backward
        while recent_posts:
            target_follower, tweet_id, time = recent_posts.pop()
            self.posts[target_follower].append((tweet_id, time))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# State
# posts {
#     1: [(10,1)]
#     2: [(20,2)]
# }
# followers {
#     1: (1)
# }
# time_stamp = 1 -> 2 -> 3

# 1. list of all posts (id + userId)
#     map of each person's followers (including themself)
#     getNewsFeed will go through the posts from most recent
#     and return posts where the userId matches
# con = getNewsFeed goes through ALL posts in twitter
# 2. map each person's posts {userId: [(post, timestamp)...]}
#     then we can cycle through all of their followers posts
#     and always add the highest timestamp until 10 posts
#     this will be O(10 * number of followers)
