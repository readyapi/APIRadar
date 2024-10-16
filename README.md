<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets-apiradar.khulnasoft.com/logos/logo-vertical-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="https://assets-apiradar.khulnasoft.com/logos/logo-vertical-light.png">
    <img alt="Apiradar logo" src="https://assets-apiradar.khulnasoft.com/logos/logo-vertical-light.png" width="150">
  </picture>
</p>

<p align="center"><b>API monitoring made easy.</b></p>

<p align="center"><i>Apiradar is a simple API monitoring & analytics tool with a focus on data privacy.<br>It is super easy to use for API projects in Python or Node.js and never collects sensitive data.</i></p>

<p align="center">🔗 <b><a href="https://apiradar.khulnasoft.com" target="_blank">apiradar.io</a></b></p>

![Apiradar screenshots](https://assets-apiradar.khulnasoft.com/screenshots/overview.png)

---

# Apiradar client library for Python

[![Tests](https://github.com/readyapi/apiradar/actions/workflows/tests.yaml/badge.svg?event=push)](https://github.com/readyapi/apiradar/actions)
[![Codecov](https://codecov.io/gh/readyapi/apiradar/graph/badge.svg?token=UNLYBY4Y3V)](https://codecov.io/gh/readyapi/apiradar)
[![PyPI](https://img.shields.io/pypi/v/apiradar?logo=pypi&logoColor=white&color=%23006dad)](https://pypi.org/project/apiradar/)

This client library for Apiradar currently supports the following Python web
frameworks:

- [ReadyAPI](https://docs-apiradar.khulnasoft.com/frameworks/readyapi)
- [Starlette](https://docs-apiradar.khulnasoft.com/frameworks/starlette)
- [Flask](https://docs-apiradar.khulnasoft.com/frameworks/flask)
- [Django Ninja](https://docs-apiradar.khulnasoft.com/frameworks/django-ninja)
- [Django REST Framework](https://docs-apiradar.khulnasoft.com/frameworks/django-rest-framework)
- [Litestar](https://docs-apiradar.khulnasoft.com/frameworks/litestar)

Learn more about Apiradar on our 🌎 [website](https://apiradar.khulnasoft.com) or check out
the 📚 [documentation](https://docs-apiradar.khulnasoft.com).

## Key features

- Middleware for different frameworks to capture metadata about API endpoints,
  requests and responses (no sensitive data is captured)
- Non-blocking clients that aggregate and send captured data to Apiradar in
  regular intervals

## Install

Use `pip` to install and provide your framework of choice as an extra, for
example:

```bash
pip install apiradar[readyapi]
```

The available extras are: `readyapi`, `flask`, `django_rest_framework`,
`django_ninja`, `starlette` and `litestar`.

## Usage

Our [setup guides](https://docs-apiradar.khulnasoft.com/quickstart) include all the details
you need to get started.

### ReadyAPI

This is an example of how to add the Apiradar middleware to a ReadyAPI
application. For further instructions, see our
[setup guide for ReadyAPI](https://docs-apiradar.khulnasoft.com/frameworks/readyapi).

```python
from readyapi import ReadyAPI
from apiradar.readyapi import ApiradarMiddleware

app = ReadyAPI()
app.add_middleware(
    ApiradarMiddleware,
    client_id="your-client-id",
    env="dev",  # or "prod" etc.
)
```

### Flask

This is an example of how to add the Apiradar middleware to a Flask application.
For further instructions, see our
[setup guide for Flask](https://docs-apiradar.khulnasoft.com/frameworks/flask).

```python
from flask import Flask
from apiradar.flask import ApiradarMiddleware

app = Flask(__name__)
app.wsgi_app = ApiradarMiddleware(
    app,
    client_id="your-client-id",
    env="dev",  # or "prod" etc.
)
```

### Django

This is an example of how to add the Apiradar middleware to a Django Ninja or
Django REST Framework application. For further instructions, see our
[setup guide for Django](https://docs-apiradar.khulnasoft.com/frameworks/django).

In your Django `settings.py` file:

```python
MIDDLEWARE = [
    "apiradar.django.ApiradarMiddleware",
    # Other middleware ...
]
APIRADAR_MIDDLEWARE = {
    "client_id": "your-client-id",
    "env": "dev",  # or "prod" etc.
}
```

### Litestar

This is an example of how to add the Apiradar plugin to a Litestar application.
For further instructions, see our
[setup guide for Litestar](https://docs-apiradar.khulnasoft.com/frameworks/litestar).

```python
from litestar import Litestar
from apiradar.litestar import ApiradarPlugin

app = Litestar(
    route_handlers=[...],
    plugins=[
        ApiradarPlugin(
            client_id="your-client-id",
            env="dev",  # or "prod" etc.
        ),
    ]
)
```

## Getting help

If you need help please
[create a new discussion](https://github.com/orgs/apiradar/discussions/categories/q-a)
on GitHub or
[join our Slack workspace](https://join.slack.com/t/apiradar-community/shared_invite/zt-2b3xxqhdu-9RMq2HyZbR79wtzNLoGHrg).

## License

This library is licensed under the terms of the MIT license.
