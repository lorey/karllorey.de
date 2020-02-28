import os
from os import listdir
from pathlib import Path
from urllib.parse import urljoin


def main():
    """
    Script to generate redirect tuples for conf.py based on the old Wordpress permalinks.
    :return:
    """
    posts_directory = "posts"
    return generate_redirects(posts_directory)


def generate_redirects(posts_directory):
    # extract the files with their absolute paths in `posts_directory`
    files = [f for f in listdir(posts_directory)]
    files_abs = [os.path.abspath(os.path.join(posts_directory, f)) for f in files]

    # generate redirect tuples (from, to)
    redirects_posts = []
    for file_path in files_abs:
        with open(file_path, "r") as file:
            # I know this is ugly, but it gets the job done

            # extract the old Wordpress permalink
            permalink = extract_permalink_from_meta(file)
            url_path_old = urljoin(permalink, "index.html")

            # create the new path
            # (doesn't need /index.html)
            base_path = "/{}".format(posts_directory)
            post_slug = Path(file_path).name.replace(".md", "")
            url_path_new = "/".join([base_path, post_slug])

            redirects_posts.append((url_path_old, url_path_new))

    with open("url_map.csv") as csv_file:
        csv_lines = csv_file.readlines()
    redirects_map_tuples = [l.split(",") for l in csv_lines]
    redirects_map_tuples = [
        (t[0].replace("http://www.karllorey.de", "") + "/index.html", t[1].strip())
        for t in redirects_map_tuples
    ]
    redirects_tags = [t for t in redirects_map_tuples if t[0].startswith("/tag")]

    return redirects_posts + redirects_tags


def extract_permalink_from_meta(file):
    lines = file.readlines()
    permalink_links = [l for l in lines if l.startswith("permalink")]
    permalink = permalink_links[0].replace("permalink: ", "").strip()
    return permalink


if __name__ == "__main__":
    print("These are your redirects from the old Wordpress posts")
    print("just copy them into the REDIRECTIONS constant in conf.py:")
    print(main())
