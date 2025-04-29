# conftest.py

import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="prod", help="Environment to run tests against")
