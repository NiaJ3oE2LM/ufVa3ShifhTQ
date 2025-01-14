#! bin/env python3
# -*- coding: utf-8 -*-
import tomllib
import feedparser as FP
from newspaper import Article
from datetime import datetime
from os import path

with open("sources.toml", "rb") as f:
    sources = tomllib.load(f)


with open("modes.toml", "rb") as f:
    modes = tomllib.load(f)
    
#%% 
out_name = datetime.now().isoformat()
with open(path.join('aggregated',out_name+'.html'),'w') as out_file:
    print('<body>', file=out_file)
    #
    for mode_name, mode in modes.items():
        #
        for _, source in sources.items():
            #
            if mode_name in source['modes']:
                print(source['name'])
                raw_feed = FP.parse(source['url'])
                articles_list = raw_feed.entries
                print(len(articles_list))
                # select articles
                for i in range(mode['num_articles']):
                    # TODO implement custom policy
                    feed_article = articles_list.pop()
                    # scrape full text
                    article = Article(feed_article.link)
                    article.download()
                    article.parse()
                    # aggregate to file 
                    print("<h1>{}</h1>".format(article.title), file=out_file)
                    print(article.text, file= out_file)
                    # TODO summarize ?
                    # TODO spechify
                    
    print('</body>', file=out_file)
                  
                