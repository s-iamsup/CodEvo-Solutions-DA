from newspaper import Article
import feedparser

def extract_news_info(feed_url):
    # Parse RSS feed
    feed = feedparser.parse(feed_url)

    # Extract article URLs
    article_urls = [entry.link for entry in feed.entries]

    # Download and parse articles
    for url in article_urls:
        article = Article(url)
        article.download()
        article.parse()

        # Extract relevant information
        title = article.title
        author = article.authors
        publish_date = article.publish_date
        content = article.text

if __name__ == "__main__":
    rss_feed_urls = [
        'http://rss.cnn.com/rss/edition.rss',
    'http://feeds.bbci.co.uk/news/rss.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    ]

    for feed_url in rss_feed_urls:
        extract_news_info(feed_url)
