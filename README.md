# A solution to a common problem

Are you tired of listening to ads on the radio or on the TV during your *precious* free time ? Are you unsatisfied with the content selection on radio and TV news programs ? What if you could choose your news sources and *automatically* generate a podcast that summarises the latest news on the topics of your choice ?

## Features

This program makes use of RSS news feeds to get access to up-to-date information on  topics of your choice, redacts a daily script with all the contents you might have read ( If you had the time), summarises the aggregated contents through LLM,  and converts the summary into a podcast-like audio that you can listen to when you find the time (for example during your daily commute, while you cook, or while you do the laundry).

Features highlight:

+ choose your own RSS news feeds;

+ define a custom policy for the aggregation of the contents. For example, you may want most recent articles or require a number of articles for each source;

+ define a target duration for the output podcast summary. For example, you could set an objective of 10 minutes for a daily news summary, or a longer duration for a weekly update;

+ *serve* the output podcast through a standard RSS service so that you can stream the summary with your favourite podcast app;

+ include source articles references in podcast shownotes with clickable links pointing to the original, source website.

## Known limitations

By design, this software cannot:

* extract meaningful, textual information by scraping a generic website. The content of the news needs to be given thought standard RSS protocol;

* spot and highlight modifications to the original news contents due to translation from local language to Engligh

* spot and highlight modifications to the original news contents due to LLM processing for summary creation.



Language limitations also come into play, for example:

+ local news most likely are not delivered in English language;

+ most of the cutting edge development of LLM technology is being done primarily in English language, therefore, depending on the popularity of your local language, a dedicated LLM may not be available;

+ translation to English may introduce errors and the contents



## Disclaimer

LLM technology may alter the meaning of the original information. If you decide to use this software, you are aware that modifications will happen and that you will hear a fake news. It is your own responsibility to check and verify what you hear on the podcast summary: the link to the original news is included in the podcast shownotes so that you can check and verify what you hear.

# Development

## Dependencies

wip

## Building blocks

wip

## Deployment

wip