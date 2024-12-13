#!/usr/bin/env python3
"""
12. Log Stats
"""


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    logs = client.logs.nginx

    docs_logs = logs.count_documents({})
    print(f"{docs_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = logs.count_documents({"method": f"{method}"})
        print(f"\tmethod {method}: {method_count}")

    status_check = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
