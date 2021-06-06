from instapy import InstaPy

session = InstaPy(username = 'your username', password = 'your password')
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)
session.set_do_follow(True, percentage = 100)
session.like_by_tags(['gaming','python'], amount = 3)
session.set_dont_like(['steam'])

session.end()