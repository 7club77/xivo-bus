# -*- coding: utf-8 -*-

# Copyright (C) 2013-2016 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from __future__ import unicode_literals

import unittest
import uuid

from ..event import AgentStatusUpdateEvent
from ..event import CallFormResultEvent
from ..event import UserStatusUpdateEvent
from ..event import EndpointStatusUpdateEvent
from hamcrest import assert_that
from hamcrest import equal_to


SOME_UUID = str(uuid.uuid4())


class TestCallFormResultEvent(unittest.TestCase):

    def test_marshal(self):
        user_id = 42
        variables = {'a': 'b'}
        event = CallFormResultEvent(user_id, variables)

        msg = event.marshal()

        assert_that(msg, equal_to({'user_id': 42,
                                   'variables': {'a': 'b'}}))

    def test_string_user_id(self):
        user_id = "42"

        event = CallFormResultEvent(user_id, {})

        assert_that(event.user_id, equal_to(42))


class TestAgentStatusUpdateEvent(unittest.TestCase):

    def test_marshal(self):
        agent_id = 42
        status = 'logged_in'

        event = AgentStatusUpdateEvent(agent_id, status)
        msg = event.marshal()

        assert_that(msg, equal_to({'agent_id': 42,
                                   'status': 'logged_in'}))

    def test_that_string_ids_are_not_leaked(self):
        agent_id = '42'
        status = 'logged_in'

        event = AgentStatusUpdateEvent(agent_id, status)
        msg = event.marshal()

        assert_that(msg, equal_to({'agent_id': 42,
                                   'status': 'logged_in'}))


class TestEndpointStatusUpdateEvent(unittest.TestCase):

    def test_marshal(self):
        endpoint_id = 42
        status = 8

        event = EndpointStatusUpdateEvent(endpoint_id, status)
        msg = event.marshal()

        assert_that(msg, equal_to({'endpoint_id': endpoint_id,
                                   'status': status}))

    def test_marshal_with_string_status(self):
        endpoint_id = 42

        event = EndpointStatusUpdateEvent(endpoint_id, '8')
        msg = event.marshal()

        assert_that(msg, equal_to({'endpoint_id': endpoint_id,
                                   'status': 8}))

    def test_that_string_endpoint_ids_are_not_leaked(self):
        endpoint_id = '42'
        status = 8

        event = EndpointStatusUpdateEvent(endpoint_id, status)

        msg = event.marshal()

        assert_that(msg, equal_to({'endpoint_id': 42,
                                   'status': status}))


class TestUserStatusUpdateEvent(unittest.TestCase):

    def test_marchal(self):
        user_uuid = SOME_UUID
        status = 'busy'

        event = UserStatusUpdateEvent(user_uuid, status)

        msg = event.marshal()

        assert_that(msg, equal_to({'user_uuid': SOME_UUID,
                                   'status': status}))

    def test_equality(self):
        user_uuid = SOME_UUID
        status = 'some_value'

        e1 = UserStatusUpdateEvent(user_uuid, status)
        e2 = UserStatusUpdateEvent(user_uuid, status)
        e3 = UserStatusUpdateEvent(user_uuid, 'other_value')
        e4 = UserStatusUpdateEvent(666, status)

        assert_that(e1 == e2, equal_to(True))
        assert_that(e1 != e2, equal_to(False))
        assert_that(e1 == e3, equal_to(False))
        assert_that(e1 == e4, equal_to(False))
        assert_that(e1 != e3, equal_to(True))
        assert_that(e1 != e4, equal_to(True))
