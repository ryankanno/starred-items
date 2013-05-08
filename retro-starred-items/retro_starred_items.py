#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import argparse
import os
import csv
import traceback

from libgreader import GoogleReader
from libgreader import ClientAuthMethod
from libgreader import Feed
from libgreader import ReaderUrl
from libgreader import SpecialFeed

"""
Function retrieves all starred items from a Google Reader account.
"""

LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'


# TODO: add config file (ryankanno) <Sun Feb 10 08:05:33 2013>
def init_argparser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-u', '--username', help='Google username', 
                        required=True)
    parser.add_argument('-p', '--password', help='Google password', 
                        required=True)
    parser.add_argument('-f', '--csv_file', help='Name of starred items file', 
                        default="starred_items.csv")
    parser.add_argument('-v', '--verbose', action='store_true', 
                        help='increase chattiness of script')
    return parser


def get_feed_item_contents(item):
    id = item['id'] if 'id' in item else ""
    title = item['title'] if 'title' in item else ""
    try:
        url = item['alternate'][0]['href']
    except:
        url = ""
    published = str(item['published']) if 'published' in item else ""
    return [id.encode('utf-8'),
            title.encode('utf-8'),
            url.encode('utf-8'),
            published.encode('utf-8')]


def get_reader(username, password):
    username = username.strip()
    password = password.strip()
    auth = ClientAuthMethod(username, password)
    return GoogleReader(auth)


def get_starred_feed_contents(reader, feed, continuation=None, num_items=1000):
    return reader.getFeedContent(feed,
                                 False,
                                 continuation,
                                 num_items,
                                 None,
                                 None)


def get_feed_items(feed_contents):
    return feed_contents['items'] if feed_contents and 'items' in feed_contents else []


def get_continuation_hash(feed_contents):
    return feed_contents['continuation'] if feed_contents and 'continuation' in feed_contents else None


def get_starred_items(args):
    logging.debug("Getting starred items for {0}".format(args.username))

    reader = get_reader(args.username, args.password)
    feed = SpecialFeed(reader, ReaderUrl.STARRED_LIST)

    feed_contents = get_starred_feed_contents(reader, feed)
    continuation = get_continuation_hash(feed_contents)

    with open(args.csv_file, 'wb') as csv_file:
        writer = csv.writer(csv_file)

        while continuation is not None:
            for item in get_feed_items(feed_contents):
                writer.writerow(get_feed_item_contents(item))

            feed_contents = get_starred_feed_contents(
                reader, feed, continuation)
            continuation = get_continuation_hash(feed_contents)

        # Last set of items to write (this sucks, just fyi)
        for item in get_feed_items(feed_contents):
            writer.writerow(get_feed_item_contents(item))


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = init_argparser()
    args = parser.parse_args(argv)

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format=LOG_FORMAT)

    try:
        get_starred_items(args)
    except:
        trace = traceback.format_exc()
        logging.error("OMGWTFBBQ: {0}".format(trace))
        sys.exit(1)

    # Yayyy-yah
    sys.exit(0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# vim: filetype=python
