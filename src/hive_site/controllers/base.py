#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Website
# Copyright (c) 2008-2017 Hive Solutions Lda.
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

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2017 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

import colony

AVAILABLE_LOCALES = (
    "pt_pt",
    "pt",
    "en_us",
    "en"
)
""" The available locales for the current infra-structure
not that the default fallback will apply in case none of
these locales matched the requested one """

ALIAS_LOCALES = dict(
    pt = "pt_pt",
    en = "en_us"
)
""" The alias locales map this defines the mapping to be
done in case a general locale is fond meaning that each
of the keys in this map refers a more specific defined locale """

controllers = colony.__import__("controllers")

class BaseController(controllers.Controller):

    def __init__(self, plugin, system):
        controllers.Controller.__init__(self, plugin, system)

    def validate(self, request, parameters, validation_parameters):
        return self.system.require_permissions(request, validation_parameters)

    def template_file(self, template = "general.html.tpl", *args, **kwargs):
        request = kwargs.get("request", None)
        locale = self.get_locale(
            request,
            available_locales = AVAILABLE_LOCALES,
            alias_locales = ALIAS_LOCALES
        )
        return self.retrieve_template_file(
            file_path = template,
            locale = locale,
            *args,
            **kwargs
        )

    def _template(self, assign_session = True, *args, **kwargs):
        return self.template(assign_session = assign_session, *args, **kwargs)
