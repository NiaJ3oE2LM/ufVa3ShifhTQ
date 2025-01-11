![Generic badge](https://img.shields.io/badge/Contributions-welcomed-GREEN.svg) ![Generic badge](https://img.shields.io/badge/Status-WIP-yellow.svg) ![](https://img.shields.io/badge/Language-Python-blue.svg) ![] ![] ![](https://img.shields.io/badge/Configuration-TOML-lightblue.svg)

# A solution to a common problem

Are you tired of listening to ads on the radio or on the TV during your *precious* free time ? Are you unsatisfied with the content selection on radio and TV news programs ? What if you could choose your news sources and *automatically* generate a podcast that summarises the latest news on the topics of your choice ?

## Features

This program makes use of [RSS](https://en.wikipedia.org/wiki/RSS) news feeds to get access to up-to-date information on  topics of your choice, aggregates a daily script with all the contents you might have read ( If you had the time), summarises the aggregated contents through [LLM](https://en.wikipedia.org/wiki/Large_language_model),  and converts the summary into a podcast-like audio that you can listen to when you find the time (for example during your daily commute, while you cook, or while you do the laundry).

Features highlight:

+ choose your own RSS news feeds;

+ define a custom policy for the aggregation of the contents. For example, you may want most recent articles or require a number of articles for each source;

+ define a target duration for the output podcast summary. For example, you could set an objective of 10 minutes for a daily news summary, or a longer duration for a weekly update;

+ *serve* the output podcast through a standard RSS service so that you can stream the summary with your favourite podcast app;

+ include source articles references in podcast shownotes with clickable links pointing to the original, source website.

## Known limitations

By design, this software cannot:

* extract meaningful, textual information by scraping a generic website. The content of the news needs to be given thought standard RSS protocol;

* spot and highlight modifications to the original news contents due to translation from local language to English

* spot and highlight modifications to the original news contents due to LLM processing for summary creation.

Language limitations also come into play, for example:

+ local news most likely are not delivered in English language;

+ most of the cutting edge development of LLM technology is being done primarily in English language, therefore, depending on the popularity of your local language, a dedicated LLM may not be available;

+ translation to English may introduce errors and the contents

Open issues under discussion:

* if the same news is published under similar text on different RSS sources, then the LLM will have a hard time distinguish the two and will likely include the 

## Disclaimer

LLM technology may alter the meaning of the original information. If you decide to use this software, you are aware that modifications will happen and that you will hear a fake news. It is your own responsibility to check and verify what you hear on the podcast summary: the link to the original news is included in the podcast shownotes with this purpose in mind.

# Development

Once the list of source RSS has been defined, a list of articles to aggregate can be created based on the following **collection modes** ![](https://img.shields.io/badge/Testing-Required-orange.svg) :

* select the last N articles based only on news time-stamp, regardless of the source

* select the last N articles from each RSS source

Consider news full-text when available or short text description otherwise. Contents that are not in plain English should be translated through LLM.

Once the content of each news is available in plain English, the following **summary modes** can be used: ![](https://img.shields.io/badge/Testing-Required-orange.svg)

* aggregate then summarise. The length of the summary should be compatible with target podcast duration. This method will pose serious limitations in the ability to link precise statements to original sources but could have potential benefits in  eliminating redundant information (for example, same news reported by different sources)

* summarise then aggregate. Limit the length of each summary so that it is compatible with target podcast duration. Possibly compare summaries to spot similar news and include only once. The output audio may lack continuity in the formulation of the sentences but, this method allows precise link to source website.

When the summary and shownotes have been produces, the body of the summary can be read into a podcast though [TTS](https://en.wikipedia.org/wiki/Speech_synthesis) technology.

## Dependencies and building blocks

An RSS downloader: should allow to access title and full-content

Set language associated to source manually. Provide a LLM for translation of each non-English language.

Content aggregation

LLM summary, use external service ?

text-to-speech 

shownotes generation

output RSS service 

# Deployment

wip

# Future

Group sources by topic so that summaries can also be generated by topic. For example, you may want to  listen to general news on the morning commute and to Finance news on the evening commute.