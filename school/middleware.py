import time

from django.db import connections


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("request", request)
        start_time = time.time()
        response = self.get_response(request)
        ex_time = time.time() - start_time
        print("ex_time", ex_time)

        path = "school/request_logs.txt"

        with open(path, "a") as file:
            file.write(
                f"Path: {request.path}, Method: {request.method}, Execution Time: {ex_time} seconds\n"
            )

        connection = connections["default"]
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO school_requestlog (path, method, ex_time) VALUES (%s, %s, %s)",
                [request.path, request.method, ex_time],
            )

        return response
