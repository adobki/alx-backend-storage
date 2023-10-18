#!/usr/bin/env python3
""" Module is an introduction to Redis as a DB manager and for caching """
from requests import get
from redis import Redis
from requests.exceptions import ConnectionError


def get_page(url: str) -> str:
    """ Implements a Redis client to be used for caching operations """
    # Send HTTP request to given URL ignoring connection errors
    try:
        content = get(url).text
    except ConnectionError:
        content = ''

    # Create redis client and increment URL access count
    r = Redis()
    r.incr(f'count:{url}')

    # Cache content for ten seconds
    r.set(url, content, ex=10)

    return content


# if __name__ == '__main__':
#     """ Tests the code in this module """
#     from random import randint
#     from time import sleep
#
#     db = Redis()
#     results = {}
#     urls = ['http://localhost:88',
#             'http://localhost:80',
#             'https://intranet.alxswe.com/projects/1234#task-11668',
#             'http://localhost:5555',
#             'https://slowwly.robertomurray.co.uk']
#
#     # Remove previous stats from database
#     db.flushdb()
#
#     # Make 100 calls to get_page() and print stats
#     for i in range(1, 101):
#         # Select random url from list and make call to get_page() with it
#         url = urls[randint(0, len(urls) - 1)]
#         get_page(url)
#
#         # Print statistics from database to see effect of get_page()
#         print(f'{i:2d}. {url}')
#         stats = {'count': int(db.get(f'count:{url}')),
#                  'content': len(db.get(url)),
#                  'TTL': db.ttl(url)}
#         results[url] = stats
#         for key in results.keys():
#             # Update TTL and content length for other URLs in results
#             if key != url:
#                 results[key]['TTL'] = db.ttl(key)
#                 data = db.get(key)
#                 results[key]['content'] = len(data) if data else None
#             print(f'\t{key}: {results[key]}')
#
#         # Pause for random number of seconds before sending another request
#         t = randint(0, 5)
#         print(f'Sleeping for {t} second(s) before sending next request. . .')
#         sleep(t)
