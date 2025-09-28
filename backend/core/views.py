from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

@api_view(["GET"])
def health(_):
    ok = True
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1;"); c.fetchone()
    except Exception:
        ok = False
    return Response(
        {"status": "ok" if ok else "degraded",
         "dependencies": {"postgres": "ok" if ok else "error"}},
        status=200 if ok else 503
    )



# Create your views here.
