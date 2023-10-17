#!/usr/bin/env python3
""" Module tests basic/introductory MondoDB features with pymongo """
from typing import Collection


def list_all(mongo_collection: Collection) -> list:
    """ Lists all the documents in a collection """
    return list(mongo_collection.find())


if __name__ == '__main__':
    """ Tests the code in this module """
    from pymongo import MongoClient
    with MongoClient() as client:
        school_collection = client.my_db.school
        schools = list_all(school_collection)
        for school in schools:
            print('[{}] {}'.format(school.get('_id'), school.get('name')))
