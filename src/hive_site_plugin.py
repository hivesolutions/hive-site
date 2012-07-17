#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Website
# Copyright (C) 2010-2012 Hive Solutions Lda.
#
# This file is part of Hive Solutions Website.
#
# Hive Solutions Website is confidential and property of Hive Solutions Lda.,
# its usage is constrained by the terms of the Hive Solutions
# Confidential Usage License.
#
# Hive Solutions Website should not be distributed under any circumstances,
# violation of this may imply legal action.
#
# If you have any questions regarding the terms of this license please
# refer to <http://www.hive.pt/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2010-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

import colony.base.system
import colony.base.decorators

class HiveSitePlugin(colony.base.system.Plugin):
    """
    The main class for the Hive Site Main plugin.
    """

    id = "pt.hive.cronus.plugins.hive_site"
    name = "Hive Site Main Plugin"
    short_name = "Hive Site Main"
    description = "The plugin that offers the hive web site"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.system.EAGER_LOADING_TYPE
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT
    ]
    capabilities = [
        "mvc_service"
    ]
    dependencies = [
        colony.base.system.PluginDependency("pt.hive.colony.plugins.mvc.utils", "1.x.x"),
        colony.base.system.PluginDependency("pt.hive.colony.plugins.resources.manager", "1.x.x"),
        colony.base.system.PluginDependency("pt.hive.colony.plugins.client.smtp", "1.x.x"),
        colony.base.system.PluginDependency("pt.hive.colony.plugins.format.mime", "1.x.x")
    ]
    main_modules = [
        "hive_site.exceptions",
        "hive_site.system"
    ]

    hive_site = None
    """ The hive site """

    mvc_utils_plugin = None
    """ The mvc utils plugin """

    resources_manager_plugin = None
    """ The resources manager plugin """

    client_smtp_plugin = None
    """ The client_smtp plugin """

    format_mime_plugin = None
    """ The format mime plugin """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import hive_site.system
        self.hive_site = hive_site.system.HiveSite(self)

    def end_load_plugin(self):
        colony.base.system.Plugin.end_load_plugin(self)
        self.hive_site.load_components()

    def unload_plugin(self):
        colony.base.system.Plugin.unload_plugin(self)
        self.hive_site.unload_components()

    @colony.base.decorators.inject_dependencies
    def dependency_injected(self, plugin):
        colony.base.system.Plugin.dependency_injected(self, plugin)

    def get_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as patterns,
        to the web mvc service. The tuple should relate the route with the handler
        method/function.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as patterns,
        to the web mvc service.
        """

        return self.hive_site.get_patterns()

    def get_communication_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as communication patterns,
        to the web mvc service. The tuple should relate the route with a tuple
        containing the data handler, the connection changed handler and the name
        of the connection.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as communication patterns,
        to the web mvc service.
        """

        return self.hive_site.get_communication_patterns()

    def get_resource_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as resource patterns,
        to the web mvc service. The tuple should relate the route with the base
        file system path to be used.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as resource patterns,
        to the web mvc service.
        """

        return self.hive_site.get_resource_patterns()

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.mvc.utils")
    def set_mvc_utils_plugin(self, mvc_utils_plugin):
        self.mvc_utils_plugin = mvc_utils_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.resources.manager")
    def set_resources_manager_plugin(self, resources_manager_plugin):
        self.resources_manager_plugin = resources_manager_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.client.smtp")
    def set_client_smtp_plugin(self, client_smtp_plugin):
        self.client_smtp_plugin = client_smtp_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.format.mime")
    def set_format_mime_plugin(self, format_mime_plugin):
        self.format_mime_plugin = format_mime_plugin
