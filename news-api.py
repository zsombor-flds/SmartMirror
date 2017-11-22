def newsFeed():
    import feedparser

    news = {}
    sub_news = []

    tech = feedparser.parse('http://index.hu/tech/rss?')
    for i in range(0, 2):
        cer = tech["entries"][i]
        sub_news.append({"title": cer["title"],"summary":cer["summary"],"published":cer["published"]})

    news["tech"] = sub_news[:]


    belfold = feedparser.parse("http://index.hu/belfold/rss?")
    del sub_news[:]
    for i in range(0, 2):
        cer = belfold["entries"][i]
        sub_news.append({"title": cer["title"],"summary":cer["summary"],"published":cer["published"]})

    news["belfold"] = sub_news[:]


    kulfold = feedparser.parse("http://index.hu/kulfold/rss?")
    del sub_news[:]

    for i in range(0, 2):
        cer = kulfold["entries"][i]
        sub_news.append({"title": cer["title"],"summary":cer["summary"],"published":cer["published"]})


    news["kulfold"] = sub_news[:]
    return news


if __name__ == "__main__":
    test = newsFeed()
    print test["belfold"][0]
