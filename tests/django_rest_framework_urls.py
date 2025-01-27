from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class FooView(APIView):
    """Foo"""

    def get(self, request: Request) -> Response:
        return Response("foo")


class FooBarView(APIView):
    def get(self, request: Request, bar: int) -> Response:
        request._request.apiradar_consumer = "test"  # type: ignore[attr-defined]
        return Response(f"foo: {bar}")


@api_view(["POST"])
def bar(request: Request) -> Response:
    return Response("bar")


@api_view(["PUT"])
def baz(request: Request) -> Response:
    raise ValueError("baz")


urlpatterns = [
    path("foo/", FooView.as_view()),
    path("foo/<int:bar>/", FooBarView.as_view()),
    path("bar/", bar),
    path("baz/", baz),
]
