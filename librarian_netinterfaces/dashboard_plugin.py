"""
plugin.py: Network interfaces plugin

Display all available network interfaces on device.

Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

from bottle_utils.i18n import lazy_gettext as _

from librarian.presentation.dashboard.dashboard import DashboardPlugin

from .lsnet import get_network_interfaces
from .forms import WifiForm


class NetInterfacesDashboardPlugin(DashboardPlugin):
    # Translators, used as dashboard section title
    heading = _('Network Interfaces')
    name = 'netinterfaces'

    def get_template(self):
        return 'dashboard/' + self.name

    def get_context(self):
        form_cls = WifiForm.get_form_class()
        form = form_cls.from_conf_file()
        return dict(interfaces=get_network_interfaces(), form=form)
