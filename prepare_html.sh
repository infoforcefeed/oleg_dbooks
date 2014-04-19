#!/usr/bin/env bash

grep 'tweet-text' scraped/*.html | sed 's/.*<p class="/<p class="/g' > prepared.html
