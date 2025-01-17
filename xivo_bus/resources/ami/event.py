# -*- coding: utf-8 -*-
# Copyright 2013-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import unicode_literals
from xivo_bus.resources.common.event import ServiceEvent


class AMIEvent(ServiceEvent):
    service = 'amid'
    name = '{ami_event}'
    routing_key_fmt = 'ami.{name}'

    def __init__(self, ami_event, variables):
        self.name = type(self).name.format(ami_event=ami_event)
        super(AMIEvent, self).__init__(variables)
