#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Website
# Copyright (C) 2010 Hive Solutions Lda.
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

__author__ = "João Magalhães <joamag@hive.pt> & Luís Martinho <lmartinho@hive.pt> & Tiago Silva <tsilva@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision: 421 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-11-20 15:16:53 +0000 (Qui, 20 Nov 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2010 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

EXCEPTION_VALUE = "exception"
""" The exception value """

MESSAGE_VALUE = "message"
""" The message value """

AVAILABLE_LOCALES = (
    "pt_pt",
    "en_us"
)
""" The available locales """

class ExceptionController:
    """
    The hive site exception controller
    """

    hive_site_plugin = None
    """ The hive site plugin """

    hive_site = None
    """ The hive site """

    def __init__(self, hive_site_plugin, hive_site):
        """
        Constructor of the class.

        @type hive_site_plugin: HiveSitePlugin
        @param hive_site_plugin: The hive site plugin.
        @type hive_site: HiveSite
        @param hive_site: The hive site.
        """

        self.hive_site_plugin = hive_site_plugin
        self.hive_site = hive_site

    def handle_exception(self, rest_request, parameters = {}):
        """
        Handles an exception.

        @type rest_request: RestRequest
        @param rest_request: The rest request for which the exception occurred.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # retrieves the exception parameters
        exception = parameters.get(EXCEPTION_VALUE)
        exception_message = exception.get(MESSAGE_VALUE)

        # processes the contents of the template file assigning the appropriate values to it
        template_file = self.retrieve_template_file("general.html.tpl", partial_page = "exception/exception.html.tpl", locale = locale)
        template_file.assign("exception_message", exception_message)
        self.process_set_contents(rest_request, template_file)
