#!/usr/bin/env python3
""" Module tests basic/introductory MondoDB features with pymongo """
from typing import Collection, Iterable


def top_students(mongo_collection: Collection) -> Iterable:
    """ Returns all students sorted by average score """
    # Create aggregate() query object from MongoDB collection
    # This is to make the next line shorter and human-readable
    aggr = mongo_collection.aggregate

    # Query database and return results with sorted average score
    return aggr([{'$project': {'_id': '$_id', 'name': '$name',
                               'averageScore': {'$avg': '$topics.score'}}},
                 {'$sort': {'averageScore': -1}}])


if __name__ == '__main__':
    """ Tests the code in this module """
    from pymongo import MongoClient
    list_all = __import__('8-all').list_all
    insert_school = __import__('9-insert_school').insert_school
    with MongoClient() as client:
        students_collection = client.my_db.students
        j_students = [
            {'name': 'John', 'topics': [{'title': 'Algo', 'score': 10.3},
                                        {'title': 'C', 'score': 6.2},
                                        {'title': 'Python', 'score': 12.1}]},
            {'name': 'Bob', 'topics': [{'title': 'Algo', 'score': 5.4},
                                       {'title': 'C', 'score': 4.9},
                                       {'title': 'Python', 'score': 7.9}]},
            {'name': 'Sonia', 'topics': [{'title': 'Algo', 'score': 14.8},
                                         {'title': 'C', 'score': 8.8},
                                         {'title': 'Python', 'score': 15.7}]},
            {'name': 'Amy', 'topics': [{'title': 'Algo', 'score': 9.1},
                                       {'title': 'C', 'score': 14.2},
                                       {'title': 'Python', 'score': 4.8}]},
            {'name': 'Julia', 'topics': [{'title': 'Algo', 'score': 10.5},
                                         {'title': 'C', 'score': 10.2},
                                         {'title': 'Python', 'score': 10.1}]}]
        for j_student in j_students:
            insert_school(students_collection, **j_student)

        students = list_all(students_collection)
        for student in students:
            print(
                '[{}] {} - {}'.format(student.get('_id'), student.get('name'),
                                      student.get('topics')))

        top_students = top_students(students_collection)
        for student in top_students:
            print(
                '[{}] {} => {}'.format(student.get('_id'), student.get('name'),
                                       student.get('averageScore')))
