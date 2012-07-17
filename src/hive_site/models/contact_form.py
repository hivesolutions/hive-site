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

import colony.libs.import_util

models = colony.libs.import_util.__import__("models")

class ContactForm(models.Model):
    """
    The class representing the logical
    contact form.
    """

    name = {
        "data_type" : "text"
    }
    """ The name of the person reporting the problem """

    company = {
        "data_type" : "text"
    }
    """ The company of the person reporting the problem """

    email = {
        "data_type" : "text"
    }
    """ The email of the person reporting the problem """

    problem = {
        "data_type" : "text"
    }
    """ The problem reported by the person """

    def __init__(self):
        """
        Constructor of the class.
        """

        self.name = None
        self.company = None
        self.email = None
        self.problem = None

    def set_validation(self):
        """
        Sets the validation structures for the current
        structure.
        """

        # adds the validation methods to the name attribute
        self.add_validation_method("name", "not_none", True)
        self.add_validation_method("name", "not_empty")

        # adds the validation methods to the company attribute
        self.add_validation_method("company", "not_none", True)
        self.add_validation_method("company", "not_empty")

        # adds the validation methods to the email attribute
        self.add_validation_method("email", "not_none", True)
        self.add_validation_method("email", "is_email")

        # adds the validation methods to the problem attribute
        self.add_validation_method("problem", "not_none", True)
        self.add_validation_method("problem", "not_empty")
