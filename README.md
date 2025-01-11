# A solution to a common problem

Are you tired of listening to ads on the radio or on the TV in your precious free time ? Are you unsatisfied with the content selection on radio and TV news programs ? What if you could choose you news sources and automatically generate a podcast that summarises the latest news on the topics of your choice ?

## Features

This program makes use of RSS news feeds to get access to up-to-date information on  topics of your choice, redacts a daily script with all the contents you might have read ( If you had the time), summarises the aggregated contents through LLM and converts the summary into a podcast-like audio that you can listen when you find the time (for example during your daily commute, while you cook, or while you do the laundry).

Features highlight:

+ choose your own RSS news feeds

+ define a custom policy for the aggregation of the contents. For example, you may want most recent articles or enforce a number of articles by source;

+ define a target length for the output podcast summary. For example, you could set an objective of 10 minutes for a daily news summary, or a longer duration for a weekly update;

+ *serve* the output podcast through a standard RSS service so that you can play the summary with your favourite podcast app;

## Limitations

By design, this software cannot:

* extract meaningful, textual information by scraping a generic website. The content of the news needs to be given thought standard RSS protocol;



Language limitations also come into play. For example:

+ local news most likely are not delivered in English language

+ most of the cutting edge development of LLM technology is being done primarily in English language

+ depending on the popularity of your local language, a dedicated LLM may not be available.



# Development

## Dependencies

wip

## Building blocks

wip

## Deployment

wip