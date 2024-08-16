import feedparser
from newspaper import Article

def extract_articles_from_rss(feed_urls):
    articles_info = []

    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            article_info = {}
            try:
                article = Article(entry.link)
                article.download()
                article.parse()

                article_info['title'] = article.title
                article_info['author'] = article.authors
                article_info['publish_date'] = article.publish_date
                article_info['content'] = article.text
                article_info['url'] = entry.link

                articles_info.append(article_info)
            except Exception as e:
                print(f"Failed to process article: {entry.link}")
                print(e)

    return articles_info

# List of RSS feed URLs to test, including the provided URL
rss_feed_urls = [
    'http://rss.cnn.com/rss/edition.rss',
    'http://feeds.bbci.co.uk/news/rss.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'https://timesofindia.indiatimes.com/rss.cms'
]

# Extract articles information
articles = extract_articles_from_rss(rss_feed_urls)

# Print the extracted information
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Author: {article['author']}")
    print(f"Publish Date: {article['publish_date']}")
    print(f"Content: {article['content'][:200]}...")  # Printing only the first 200 characters
    print(f"URL: {article['url']}\n")
