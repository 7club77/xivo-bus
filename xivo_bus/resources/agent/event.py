# -*- coding: utf-8 -*-
# Copyright 2015-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import unicode_literals
from xivo_bus.resources.common.event import TenantEvent, MultiUserEvent


class AgentCreatedEvent(TenantEvent):
    name = 'agent_created'
    routing_key_fmt = 'config.agent.created'

    def __init__(self, agent_id, tenant_uuid):
        content = {'id': int(agent_id)}
        super(AgentCreatedEvent, self).__init__(content, tenant_uuid)


class AgentDeletedEvent(TenantEvent):
    name = 'agent_deleted'
    routing_key_fmt = 'config.agent.deleted'

    def __init__(self, agent_id, tenant_uuid):
        content = {'id': int(agent_id)}
        super(AgentDeletedEvent, self).__init__(content, tenant_uuid)


class AgentEditedEvent(TenantEvent):
    name = 'agent_edited'
    routing_key_fmt = 'config.agent.edited'

    def __init__(self, agent_id, tenant_uuid):
        content = {'id': int(agent_id)}
        super(AgentEditedEvent, self).__init__(content, tenant_uuid)


class AgentPausedEvent(MultiUserEvent):
    name = 'agent_paused'
    routing_key_fmt = 'status.agent.pause'
    required_acl_fmt = 'events.statuses.agents'

    def __init__(self, agent_id, agent_number, queue, reason, tenant_uuid, user_uuids):
        content = {
            'agent_id': agent_id,
            'agent_number': agent_number,
            'paused': True,
            'paused_reason': reason or '',
            'queue': queue,
        }
        super(AgentPausedEvent, self).__init__(content, tenant_uuid, user_uuids)


class AgentUnpausedEvent(MultiUserEvent):
    name = 'agent_unpaused'
    routing_key_fmt = 'status.agent.unpause'
    required_acl_fmt = 'events.statuses.agents'

    def __init__(self, agent_id, agent_number, queue, reason, tenant_uuid, user_uuids):
        content = {
            'agent_id': agent_id,
            'agent_number': agent_number,
            'paused': False,
            'paused_reason': reason or '',
            'queue': queue,
        }
        super(AgentUnpausedEvent, self).__init__(content, tenant_uuid, user_uuids)


class AgentStatusUpdatedEvent(MultiUserEvent):
    name = 'agent_status_update'
    routing_key_fmt = 'status.agent'
    required_acl_fmt = 'events.statuses.agents'

    def __init__(self, agent_id, status, tenant_uuid, user_uuids):
        content = {'agent_id': int(agent_id), 'status': status}
        super(AgentStatusUpdatedEvent, self).__init__(content, tenant_uuid, user_uuids)
