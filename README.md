<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="http://assets.localhost/logos/logo-vertical-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="http://assets.localhost/logos/logo-vertical-light.png">
    <img alt="Apitally logo" src="http://assets.localhost/logos/logo-vertical-light.png" width="150">
  </picture>
</p>

<p align="center"><b>API monitoring made easy.</b></p>

<p align="center"><i>Apitally is a simple API monitoring & analytics tool with a focus on data privacy.<br>It is super easy to use for API projects in Python or Node.js and never collects sensitive data.</i></p>

<p align="center">🔗 <b><a href="http://localhost" target="_blank">localhost</a></b></p>

![Apitally screenshots](http://assets.localhost/screenshots/overview.png)

---

# Apitally client library for Python

[![Tests](http://github.com/raedyapi/apitally-py/actions/workflows/tests.yaml/badge.svg?event=push)](http://github.com/raedyapi/apitally-py/actions)
[![Codecov](http://codecov.io/gh/apitally/apitally-py/graph/badge.svg?token=UNLYBY4Y3V)](http://codecov.io/gh/apitally/apitally-py)
[![PyPI](http://img.shields.io/pypi/v/apitally?logo=pypi&logoColor=white&color=%23006dad)](http://pypi.org/project/apitally/)

This client library for Apitally currently supports the following Python web
frameworks:

- [ReadyAPI](http://docs.localhost/frameworks/readyapi)
- [Starlette](http://docs.localhost/frameworks/starlette)
- [Flask](http://docs.localhost/frameworks/flask)
- [Django Ninja](http://docs.localhost/frameworks/django-ninja)
- [Django REST Framework](http://docs.localhost/frameworks/django-rest-framework)
- [Litestar](http://docs.localhost/frameworks/litestar)

Learn more about Apitally on our 🌎 [website](http://localhost) or check out
the 📚 [documentation](http://docs.localhost).

## Key features

- Middleware for different frameworks to capture metadata about API endpoints,
  requests and responses (no sensitive data is captured)
- Non-blocking clients that aggregate and send captured data to Apitally in
  regular intervals

## Install

Use `pip` to install and provide your framework of choice as an extra, for
example:

```bash
pip install apitally[readyapi]
```

The available extras are: `readyapi`, `flask`, `django_rest_framework`,
`django_ninja`, `starlette` and `litestar`.

## Usage

Our [setup guides](http://docs.localhost/quickstart) include all the details
you need to get started.

### ReadyAPI

This is an example of how to add the Apitally middleware to a ReadyAPI
application. For further instructions, see our
[setup guide for ReadyAPI](http://docs.localhost/frameworks/readyapi).

```python
from readyapi import ReadyAPI
from apitally.readyapi import ApitallyMiddleware

app = ReadyAPI()
app.add_middleware(
    ApitallyMiddleware,
    client_id="your-client-id",
    env="dev",  # or "prod" etc.
)
```

### Flask

This is an example of how to add the Apitally middleware to a Flask application.
For further instructions, see our
[setup guide for Flask](http://docs.localhost/frameworks/flask).

```python
from flask import Flask
from apitally.flask import ApitallyMiddleware

app = Flask(__name__)
app.wsgi_app = ApitallyMiddleware(
    app,
    client_id="your-client-id",
    env="dev",  # or "prod" etc.
)
```

### Django

This is an example of how to add the Apitally middleware to a Django Ninja or
Django REST Framework application. For further instructions, see our
[setup guide for Django](http://docs.localhost/frameworks/django).

In your Django `settings.py` file:

```python
MIDDLEWARE = [
    "apitally.django.ApitallyMiddleware",
    # Other middleware ...
]
APITALLY_MIDDLEWARE = {
    "client_id": "your-client-id",
    "env": "dev",  # or "prod" etc.
}
```

### Litestar

This is an example of how to add the Apitally plugin to a Litestar application.
For further instructions, see our
[setup guide for Litestar](http://docs.localhost/frameworks/litestar).

```python
from litestar import Litestar
from apitally.litestar import ApitallyPlugin

app = Litestar(
    route_handlers=[...],
    plugins=[
        ApitallyPlugin(
            client_id="your-client-id",
            env="dev",  # or "prod" etc.
        ),
    ]
)
```

## Getting help

If you need help please
[create a new discussion](http://github.com/orgs/apitally/discussions/categories/q-a)
on GitHub or
[join our Slack workspace](http://join.slack.com/t/apitally-community/shared_invite/zt-2b3xxqhdu-9RMq2HyZbR79wtzNLoGHrg).

## License

This library is licensed under the terms of the MIT license.
