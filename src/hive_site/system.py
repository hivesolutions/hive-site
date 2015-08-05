#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Website
# Copyright (c) 2008-2015 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

import colony

class HiveSite(colony.System):
    """
    The hive site class.
    """

    def load_components(self):
        """
        Loads the main components models, controllers, etc.
        This load should occur only after the dependencies are loaded.
        """

        # retrieves the mvc utils plugin
        mvc_utils_plugin = self.plugin.mvc_utils_plugin

        # creates the models classes then creates the controllers
        # this operation should properly load and start the components
        mvc_utils_plugin.assign_models_controllers(self, self.plugin)

    def unload_components(self):
        """
        Unloads the main components models, controllers, etc.
        This load should occur the earliest possible in the unloading process.
        """

        # retrieves the mvc utils plugin
        mvc_utils_plugin = self.plugin.mvc_utils_plugin

        # destroys the models and then destroy the controllers,
        # unregistering them from the internal structures as expected
        mvc_utils_plugin.unassign_models_controllers(self)

    def get_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as patterns,
        to the mvc service. The tuple should relate the route with the handler
        method/function.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as patterns,
        to the mvc service.
        """

        return (
            (r"hive_site/?", self.main_controller.index, "get"),
            (r"hive_site/index", self.main_controller.index, "get"),
            (r"hive_site/contact", self.main_controller.contact, "get"),
            (r"hive_site/contact", self.main_controller.contact_process, "post"),
            (r"hive_site/thankyou", self.main_controller.thankyou, "get"),
            (r"hive_site/products", self.main_controller.products, "get"),
            (r"hive_site/consulting", self.main_controller.consulting, "get"),
            (r"hive_site/saas", self.main_controller.saas, "get"),
            (r"hive_site/cloud", self.main_controller.cloud, "get"),
            (r"hive_site/social", self.main_controller.social, "get"),
            (r"hive_site/mobile", self.main_controller.mobile, "get"),
            (r"hive_site/labs", self.main_controller.labs, "get"),
            (r"hive_site/people", self.main_controller.people, "get"),
            (r"hive_site/about", self.main_controller.about, "get"),
            (r"hive_site/language", self.main_controller.language, "get")
        )

    def get_resource_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as resource patterns,
        to the mvc service. The tuple should relate the route with the base
        file system path to be used.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as resource patterns,
        to the mvc service.
        """

        # retrieves the plugin manager and uses it to retrieve
        # the colony site plugin path
        plugin_manager = self.plugin.manager
        plugin_path = plugin_manager.get_plugin_path_by_id(self.plugin.id)

        return (
            (r"hive_site/resources/.+", (plugin_path + "/hive_site/resources/extras", "hive_site/resources")),
        )
