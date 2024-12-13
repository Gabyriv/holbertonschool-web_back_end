#!/usr/bin/env python3
"""
12. Log Stats
"""


from pymongo import MongoClient


def log_stats():
    """
    Provide some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    docs_logs = collection.count_documents({})
    print(f"{docs_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": f"{method}"})
        print(f"\tmethod {method}: {method_count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()
