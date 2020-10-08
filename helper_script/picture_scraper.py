"""
Scrapes n pictures from Google Images given a serch phrase.


Usage:
    python get_images.py --search_phrase <search phrase> --destination_folder <folder_name> --n <number of images>

Ex:
    python get_images.py --search_phrase "studio apartments" --destination_folder  data --n 10
"""

import argparse

import os
import sys
from bing_image_downloader import downloader

my_argparser = argparse.ArgumentParser(description=__doc__)

my_argparser.add_argument("--search_phrase", type=str, required=True)
my_argparser.add_argument("--download_folder", type=str, required=True)
my_argparser.add_argument("--limit", type=int, required=True)


def main(args):
    downloader.download(args.search_phrase, 
                        limit=args.limit, 
                        output_dir=args.download_folder, 
                        force_replace=False, 
                        timeout=60)

    print(f"Pictures are downloaded to {args.download_folder}")


if __name__ == "__main__":
    args = my_argparser.parse_args()
    main(args)
else:
    print(__doc__)
