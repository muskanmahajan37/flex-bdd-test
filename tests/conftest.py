import os
from typing import Generator

import pytest
from starlette.testclient import TestClient

BDD_BASE_URL = os.getenv("BDD_BASE_URL")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")


