from collections import defaultdict
class Twitter:
    """
    twitter = dict for {userid: [tweet ids]}

    post tweet = put it in the dict with the user id as key

    get news feed =>
    use list to order tweets in order they came (user id, tweet id)
    return ids in order of most recent to least recent until 10 cutoff point
    if no follow = return at most 10 tweet ids from their id 
    if follow = return both their and their followers
    feed = (7, 23), (7, 24), (7,25), (7,26), 
    userid8 = []
    feed  = [20,10] count = 1
    follow = dict for follower id: [followees ids]

    unfollow = remove the followee from the follower dict
    """

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        count = 0
        for (uid, tid) in self.tweets[::-1]:
            if count >= 10:
                break
            if uid == userId or uid in set(self.followers[userId]):
                feed.append(tid)
                count += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
        
