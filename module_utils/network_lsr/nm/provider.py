# SPDX-License-Identifier: BSD-3-Clause

import logging

# Relative import is not support by ansible 2.8 yet
# pylint: disable=import-error, no-name-in-module
from ansible.module_utils.network_lsr.nm.active_connection import (  # noqa:E501
    deactivate_active_connection,
)
from ansible.module_utils.network_lsr.nm.client import get_client  # noqa:E501

# pylint: enable=import-error, no-name-in-module


class NetworkManagerProvider:
    def deactivate_connection(self, connection_name, timeout, check_mode):
        """
        Return True if changed.
        """
        nm_client = get_client()
        changed = False
        for nm_ac in nm_client.get_active_connections():
            nm_profile = nm_ac.get_connection()
            if nm_profile and nm_profile.get_id() == connection_name:
                changed |= deactivate_active_connection(nm_ac, timeout, check_mode)
        if not changed:
            logging.info("No active connection for {0}".format(connection_name))

        return changed
