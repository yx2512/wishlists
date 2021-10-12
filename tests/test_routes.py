# Copyright 2016, 2019 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Wishlists API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
  codecov --token=$CODECOV_TOKEN

"""

import os
import logging
import unittest
from urllib.parse import quote_plus
from service import status  # HTTP Status Codes
from service.models import db
from service.routes import app, init_db
from .factories import WishlistFactory

# DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///../db/test.db')
DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgres://postgres:postgres@localhost:5432/postgres"
)

BASE_URL = "/wishlists"

######################################################################
#  T E S T   C A S E S
######################################################################
class TestWishlistsServer(unittest.TestCase):
    """ Wishlists Server Tests """

    # @classmethod
    # def setUpClass(cls):
    #     """ Run once before all tests """
    #     app.config["TESTING"] = True
    #     app.config["DEBUG"] = False
    #     app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    #     app.logger.setLevel(logging.CRITICAL)
    #     init_db()

    # @classmethod
    # def tearDownClass(cls):
    #     pass

    # def setUp(self):
    #     """ Runs before each test """
    #     db.drop_all()  # clean up the last tests
    #     db.create_all()  # create new tables
    #     self.app = app.test_client()

    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()
