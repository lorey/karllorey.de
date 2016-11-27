# Migrating my Wordpress site to Jekyll

This repository contains my attempt to migrate [my old wordpress site](http://karllorey.de) to Jekyll.

## Steps necessary to migrate from Wordpress to Jekyll (like I did)
The following steps are necessary to reproduce the result:

1. Install [Jekyll Exporter](https://wordpress.org/plugins/jekyll-exporter/) to export data (yielded mostly clean markdown files whereas [Jekyll's functionality](http://import.jekyllrb.com/docs/wordpress/) exported messy HTML.
2. Fix overly-escaped titles: The titles were escaped twice and had to be reverted
3. Clean up images: Images were exported in various sizes which is IMHO not necessary.
4. Fix the captions and thumbnails: Captions and thumbnails were not exported correctly as there is no similar functionality in markdown.
5. Add YouTube videos and similar embedded content (was not exported at all)
6. (Optional) Convert snippets to gists

## Tasks I'm planning to do while I'm at it
In addition to the steps above, I would like to implement the following changes:

- Remove most of the pages
- Remove posts that became irrelevant over time
- Redirect removed pages to meaningful replacements

### Replace a page with a post
To replace a page with a post, I propose the following steps:

1. Create a post with the contents of the page
2. Adapt the Front Matter
3. Redirect the page's old URL to the new post
