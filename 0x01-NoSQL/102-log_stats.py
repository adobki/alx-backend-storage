#!/usr/bin/env python3
""" Module tests basic/introductory MondoDB features with pymongo """
from pymongo import MongoClient


def log_stats() -> str:
    """ Pretty prints some stats about Nginx logs stored in a collection """
    # Registered HTTP methods
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    # Open MongoDB connection to query database
    with MongoClient() as client:
        # Create count_documents() query object from MongoDB collection
        # This is to make the following lines shorter and human-readable
        counter = client.logs.nginx.count_documents

        # Create dictionary to store results and compute total and status
        results = {'total': counter({}),
                   'status': counter({'method': 'GET',
                                      'path': '/status'})}

        # Get number of records for each HTTP method in methods list
        for method in methods:
            results[method] = counter({'method': method})

        # Get aggregated count of ips sorted in descending order
        count_ips = client.logs.nginx.aggregate([{'$sortByCount': '$ip'}])
        # Add first ten items to results
        results['ips'] = list(count_ips)[:10]

    # Generate output in pretty format
    output = f'{results["total"]} logs'\
             '\nMethods:'
    for method in methods:
        output += f'\n\tmethod {method}: {results[method]}'
    output += f'\n{results["status"]} status check'
    output += '\nIPs:'
    for ip in results['ips']:
        output += f'\n\t{ip.get("_id")}: {ip.get("count")}'

    # Print and return pretty output
    print(output)
    return output


if __name__ == '__main__':
    """ Tests the code in this module """
    log_stats()
