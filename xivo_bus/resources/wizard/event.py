# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
#
# SPDX-License-Identifier: GPL-3.0+


class CreateWizardEvent(object):
    name = 'wizard_created'
    routing_key = 'config.wizard.created'

    def marshal(self):
        return {}

    @classmethod
    def unmarshal(cls, msg):
        return cls()

    def __eq__(self, other):
        return (self.name == other.name and
                self.routing_key == other.routing_key)

    def __ne__(self, other):
        return not self == other
