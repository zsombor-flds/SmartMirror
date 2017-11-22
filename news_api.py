def newsFeed():
    import feedparser

    news = {}
    sub_news = []

    tech = feedparser.parse('http://index.hu/tech/rss?')
    cer = tech["entries"][0]

    news["tech"] = cer

    belfold = feedparser.parse("http://index.hu/belfold/rss?")
    cer = belfold["entries"][0]

    news["belfold"] = cer

    kulfold = feedparser.parse("http://index.hu/kulfold/rss?")

    cer = kulfold["entries"][0]

    news["kulfold"] = cer
    return news


if __name__ == "__main__":
    test = newsFeed()
    print test[u"kulfold"]["title"] + "\n" + test[u"kulfold"]["description"]
