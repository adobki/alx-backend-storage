#!/usr/bin/env python3
""" Module tests basic/introductory MondoDB features with pymongo """
from typing import Collection


def schools_by_topic(mongo_collection: Collection,
                     topic: str) -> list:
    """ Returns the list of school having a specific topic """
    return list(mongo_collection.find({'topics': {'$in': [topic]}}))


if __name__ == '__main__':
    """ Tests the code in this module """
    from pymongo import MongoClient
    list_all = __import__('8-all').list_all
    insert_school = __import__('9-insert_school').insert_school
    with MongoClient() as client:
        school_collection = client.my_db.school
        j_schools = [
            {'name': 'Holberton school',
             'topics': ['Algo', 'C', 'Python', 'React']},
            {'name': 'UCSF', 'topics': ['Algo', 'MongoDB']},
            {'name': 'UCLA', 'topics': ['C', 'Python']},
            {'name': 'UCSD', 'topics': ['Cassandra']},
            {'name': 'Stanford', 'topics': ['C', 'React', 'Javascript']}
        ]
        for j_school in j_schools:
            insert_school(school_collection, **j_school)

        schools = schools_by_topic(school_collection, 'Python')
        for school in schools:
            print('[{}] {} {}'.format(school.get('_id'), school.get('name'),
                                      school.get('topics', '')))
