#!/usr/bin/env python

'''
	Diego Martins de Siqueira
	A Friendly Bot to Reddit
'''

import praw
import sys
import argparse
import re
from config_bot import *


class FriendlyBot:

	def __init__(self, subreddit, useragent, client_id, client_secret):
		self._subreddit = subreddit
		self._useragent = useragent
		self._praw		= praw.Reddit(user_agent = self._useragent)
		self._praw.set_oauth_app_info(client_id = client_id,
			client_secret = client_secret,
			redirect_uri = 'http://127.0.0.1:65010/'
			'authorize_callback')




	def read(self):
		self._subreddit = self._praw.get_subreddit(self._subreddit)

		new_posts 		= self._subreddit.get_new(limit = 5)

		if not new_posts:
			return

		for post in new_posts:
			if re.search("W4", post.title, re.IGNORECASE):
				self.reply(post)

	def reply(self,post):
            # Reply to the post
            #submission.add_comment("Nice Work!")
            print "Bot replying to : ", post.title


def main(argv):
	parser = argparse.ArgumentParser(description="A Friendly Bot who looks for posts and give it a reply from a list")
	parser.add_argument("subreddit", type=str, 
		help="SubReddit you wanna lurk")
	parser.add_argument("useragent", type=str, 
		help="User Agent to your Bot")

	args = parser.parse_args()

	try:
		fb = FriendlyBot(args.subreddit, args.useragent, REDDIT_USERNAME, REDDIT_PASS)
		fb.read()
		print 'All posts were looked.'
	except KeyboardInterrupt:
		print 'Interrupt received, stopping downloads'

	sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])