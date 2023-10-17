#!/usr/bin/env python3
""" Module tests basic/introductory MondoDB features with pymongo """
from typing import Collection


def insert_school(mongo_collection: Collection,
                  **kwargs) -> str:
    """ Inserts a new document in a collection based on kwargs """
    return mongo_collection.insert_one(kwargs).inserted_id


if __name__ == '__main__':
    """ Tests the code in this module """
    from pymongo import MongoClient
    list_all = __import__('8-all').list_all
    with MongoClient() as client:
        school_collection = client.my_db.school
        new_school_id = insert_school(school_collection, name='UCSF',
                                      address='505 Parnassus Ave')
        print('New school created: {}'.format(new_school_id))

        schools = list_all(school_collection)
        for school in schools:
            print('[{}] {} {}'.format(school.get('_id'), school.get('name'),
                                      school.get('address', '')))
