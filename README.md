# Migrating my Wordpress site to Jekyll

This repository contains my attempt to migrate [my old wordpress site](http://karllorey.de) to Jekyll.

## What I did
1) Install [Jekyll Exporter](https://wordpress.org/plugins/jekyll-exporter/) to export data (yielded mostly clean markdown files whereas [Jekyll's functionality](http://import.jekyllrb.com/docs/wordpress/) exported messy HTML.
2) Fix overly-escaped titles: The titles were escaped twice and had to be reverted
3) Clean up images: Images were exported in various sizes which is IMHO not necessary.
4) Fix the captions and thumbnails: Captions and thumbnails were not exported correctly as there is no similar functionality in markdown.
5) Add YouTube videos and similar embedded content (was not exported at all)
6) (Optional) Convert snippets to gists
