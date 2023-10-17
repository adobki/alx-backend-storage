#!/usr/bin/env python3
""" Module tests basic/introductory MondoDB features with pymongo """
from typing import Iterable, Collection


def update_topics(mongo_collection: Collection,
                  name: str, topics: Iterable[str]) -> None:
    """ Changes all topics of a school document based on the name """
    mongo_collection.update_many({'name': name},
                                 {'$set': {'topics': topics}})


if __name__ == '__main__':
    """ Tests the code in this module """
    from pymongo import MongoClient
    list_all = __import__('8-all').list_all
    with MongoClient() as client:
        school_collection = client.my_db.school
        update_topics(school_collection, 'Holberton school',
                      ['Sys admin', 'AI', 'Algorithm'])

        schools = list_all(school_collection)
        for school in schools:
            print('[{}] {} {}'.format(school.get('_id'), school.get('name'),
                                      school.get('topics', '')))

        print()
        update_topics(school_collection, 'Holberton school', ['iOS'])
        schools = list_all(school_collection)
        for school in schools:
            print('[{}] {} {}'.format(school.get('_id'), school.get('name'),
                                      school.get('topics', '')))
