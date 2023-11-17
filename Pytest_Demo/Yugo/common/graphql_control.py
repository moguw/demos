"""
处理fragments从 graphql分离

"""

import json,os
from functools import wraps


def get_graphql_dir():
    r, _ = os.path.split(os.path.split(os.path.abspath(__file__))[0])
    return os.path.join(r, "graphql")


def read_file(path):
    with open(path, "r") as f:
        content = f.read()
    return content

def get_graphql_query(fragments_query=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            main_query_path = os.path.join(get_graphql_dir(), f"{func.__name__}.graphql")
            main_query = read_file(main_query_path)
            if fragments_query:
                for i in range(len(fragments_query)):
                    main_query += read_file(os.path.join(get_graphql_dir(), "fragments", str(fragments_query[i])))
            return func(query=main_query, *args, **kwargs)
        return wrapper
    return decorator






# def get_graphql_query(*fragments_query):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             main_query_path = os.path.join(get_graphql_dir(), f"{func.__name__}.graphql")
#             main_query = read_file(main_query_path)
#             if fragments_query:
#                 for i in range(len(fragments_query)):
#                     main_query += read_file(os.path.join(get_graphql_dir(), "fragments", str(fragments_query[i])))
#             return func(query=main_query, *args, **kwargs)
#         return wrapper
#     return decorator



# def get_graphql_query(*fragments_query):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             main_query_path = os.path.join(get_graphql_dir(),f"{func.__class__.__name__}", f"{func.__name__}.graphql")
#             main_query = read_file(main_query_path)
#             if fragments_query:
#                 for i in range(len(fragments_query)):
#                     main_query += read_file(os.path.join(get_graphql_dir(), "fragments", str(fragments_query[i])))
#             return func(query=main_query, *args, **kwargs)
#         return wrapper
#     return decorator










