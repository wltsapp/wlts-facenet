from scrapers.reddit_scraper import RedditScraper

rs = RedditScraper()
def run_gather_threads():
  #code that goes to reddit and gets thread info
  rs.gather_threads()
  print "Gathering Threads"

def run_gather_comments():
  #code that goes to reddit and gets comment info
  print "Gathering Comments"
  rs.gather_comments()
