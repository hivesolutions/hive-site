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

__author__ = "João Magalhães <joamag@hive.pt> & Luís Martinho <lmartinho@hive.pt> & Tiago Silva <tsilva@hive.pt>"
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

import datetime

import colony.libs.import_util

import hive_site.exceptions

DEFAULT_ENCODING = "utf-8"
""" The default encoding value """

USERNAME_VALUE = "username"
""" The username value """

PASSWORD_VALUE = "password"
""" The password value """

TLS_VALUE = "tls"
""" The tls value """

FROM_VALUE = "From"
""" The from value """

TO_VALUE = "To"
""" The to value """

REPLY_TO_VALUE = "Reply-to"
""" The reply to value """

SUBJECT_VALUE = "Subject"
""" The subject value """

DATE_VALUE = "Date"
""" The date value """

DATE_TIME_FORMAT_VALUE = "%a, %d %b %Y %H:%M:%S +0000 (UTC)"
""" The format for the displayed date times """

REPLY_TO_LINE_FORMAT_VALUE = "%s <%s>"
""" The format to the reply to line """

SUBJECT_FORMAT_VALUE = "[%s] %s (%s) is getting in touch with us"
""" The format to the subject """

TIMESTAMP_FORMAT_VALUE = "%Y%m%d%H%M%S"
""" The timestamp format value """

DEFAULT_TARGET_EMAIL = "hello@hive.pt"
""" The default target email """

DEFAULT_ORIGIN_EMAIL = "hello@hive.pt"
""" The default origin email """

REQUIRED_FIELDS_MISSING_ERROR_TEXT = "Required fields missing"
""" The required fields missing error text """

TECHNICAL_PROBLEMS_WHILE_SENDING_ERROR_TEXT = "Technical problems while sending the form"
""" The technical problems while sending error text """

AVAILABLE_LOCALES = (
    "pt_pt",
    "en_us"
)
""" The available locales """

models = colony.libs.import_util.__import__("models")
mvc_utils = colony.libs.import_util.__import__("mvc_utils")
controllers = colony.libs.import_util.__import__("controllers")

class MainController(controllers.Controller):
    """
    The hive site controller.
    """

    @mvc_utils.serialize
    def handle_hive_index(self, rest_request, parameters = {}):
        """
        Handles the given hive index rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive index rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/index.html.tpl",
            locale = locale
        )
        template_file.assign("area", "home")
        template_file.assign("title", "Hive Solutions")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_contact(self, rest_request, parameters = {}):
        """
        Handles the given hive contact rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive contact rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/contact.html.tpl",
            locale = locale
        )
        template_file.assign("area", "about")
        template_file.assign("title", "Hive Solutions - Contact")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_contact_process(self, rest_request, parameters = {}):
        """
        Handles the given hive contact process rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive contact process rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the contact form from the rest request
        contact_form = self.get_field(rest_request, "contact_form", {})

        # processes the contact form
        contact_form_model = self._process_contact(rest_request, contact_form)

        # in case the validation goes wrong
        if not contact_form_model.is_valid():
            # retrieves the current locale
            locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

            # processes the contents of the template file assigning the
            # appropriate values to it
            template_file = self.retrieve_template_file(
                "general.html.tpl",
                partial_page = "general/contact.html.tpl",
                locale = locale
            )
            template_file.assign("area", "about")
            template_file.assign("contact_form_model", contact_form_model)
            template_file.assign("contact_form_error", REQUIRED_FIELDS_MISSING_ERROR_TEXT)
            template_file.assign("title", "Hive Solutions - Contact")
            self.process_set_contents(rest_request, template_file)

            # returns immediately
            return

        try:
            # sends the email with the defined arguments
            self._send_contact_form_email(rest_request, contact_form_model)
        except:
            # in case the debug level is the required
            # to re-throw exception
            if rest_request.is_debug():
                # re-raises the exception
                raise

            # retrieves the current locale
            locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

            # processes the contents of the template file assigning the
            # appropriate values to it
            template_file = self.retrieve_template_file(
                "general.html.tpl",
                partial_page = "general/contact.html.tpl",
                locale = locale
            )
            template_file.assign("area", "about")
            template_file.assign("title", "Hive Solutions - Contact")
            template_file.assign("contact_form_model", contact_form_model)
            template_file.assign("contact_form_error", TECHNICAL_PROBLEMS_WHILE_SENDING_ERROR_TEXT)
            self.process_set_contents(rest_request, template_file)

            # returns immediately
            return

        # sets the name attribute in the session
        self.set_session_attribute(rest_request, "name", contact_form_model.name)

        # redirects to the thank you page
        self.redirect_base_path(rest_request, "thankyou#thank-you-wrapper", quote = False)

    @mvc_utils.serialize
    def handle_hive_thankyou(self, rest_request, parameters = {}):
        """
        Handles the given hive thankyou rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive thankyou rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # retrieves the name from the parameters
        name = self.get_session_attribute(rest_request, "name")

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/thankyou.html.tpl",
            locale = locale
        )
        template_file.assign("area", "about")
        template_file.assign("title", "Hive Solutions - Thank You")
        template_file.assign("name", name)
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_products(self, rest_request, parameters = {}):
        """
        Handles the given hive products rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive products rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/products.html.tpl",
            locale = locale
        )
        template_file.assign("area", "products")
        template_file.assign("title", "Hive Solutions - Products")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_consulting(self, rest_request, parameters = {}):
        """
        Handles the given hive consulting rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive consulting rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/consulting.html.tpl",
            locale = locale
        )
        template_file.assign("area", "consulting")
        template_file.assign("title", "Hive Solutions - Consulting")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_saas(self, rest_request, parameters = {}):
        """
        Handles the given hive saas rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive saas rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/saas.html.tpl",
            locale = locale
        )
        template_file.assign("area", "consulting")
        template_file.assign("title", "Hive Solutions - SaaS")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_cloud(self, rest_request, parameters = {}):
        """
        Handles the given hive cloud rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive cloud rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/cloud.html.tpl",
            locale = locale
        )
        template_file.assign("area", "consulting")
        template_file.assign("title", "Hive Solutions - Cloud")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_social(self, rest_request, parameters = {}):
        """
        Handles the given hive social rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive social rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/social.html.tpl",
            locale = locale
        )
        template_file.assign("area", "consulting")
        template_file.assign("title", "Hive Solutions - Social")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_mobile(self, rest_request, parameters = {}):
        """
        Handles the given hive mobile rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive mobile rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/mobile.html.tpl",
            locale = locale
        )
        template_file.assign("area", "consulting")
        template_file.assign("title", "Hive Solutions - Mobile")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_labs(self, rest_request, parameters = {}):
        """
        Handles the given hive labs rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive labs rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/labs.html.tpl",
            locale = locale
        )
        template_file.assign("area", "labs")
        template_file.assign("title", "Hive Solutions - Labs")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_people(self, rest_request, parameters = {}):
        """
        Handles the given hive people rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive people rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/people.html.tpl",
            locale = locale
        )
        template_file.assign("area", "people")
        template_file.assign("title", "Hive Solutions - People")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_about(self, rest_request, parameters = {}):
        """
        Handles the given hive about rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive about rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/about.html.tpl",
            locale = locale
        )
        template_file.assign("area", "about")
        template_file.assign("title", "Hive Solutions - About")
        self.process_set_contents(rest_request, template_file)

    @mvc_utils.serialize
    def handle_hive_language(self, rest_request, parameters = {}):
        """
        Handles the given hive language rest request.

        @type rest_request: RestRequest
        @param rest_request: The hive language rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the locale from the rest request
        locale = self.get_field(rest_request, "locale", None)

        # sets the locale in session
        self.set_locale_session(rest_request, locale)

        # redirects the rest request "back"
        self.redirect_back(rest_request, "index")

    def _process_contact(self, rest_request, contact):
        # creates the contact model
        contact_form_model = models.ContactForm.new(contact)

        # validates the model retrieving the result of the validation
        _model_valid = contact_form_model.validate()

        # returns the contact form model
        return contact_form_model

    def _send_contact_form_email(self, rest_request, contact_form_model):
        # retrieves the client_smtp plugin
        client_smtp_plugin = self.plugin.client_smtp_plugin

        # retrieves the format mime plugin
        format_mime_plugin = self.plugin.format_mime_plugin

        # retrieves the contact form attributes
        name = contact_form_model.name
        company = contact_form_model.company
        from_email = contact_form_model.email
        problem = contact_form_model.problem

        # retrieves the email attributes
        smtp_server, smtp_port, smtp_use_tls, smtp_user, smtp_password = self._get_email_attributes()

        # creates a new smtp client, using the client_smtp plugin
        smtp_client = client_smtp_plugin.create_client({})

        # opens the smtp client
        smtp_client.open({})

        # creates the parameters map
        parameters = {}

        # sets the authentication parameters
        parameters[USERNAME_VALUE] = smtp_user
        parameters[PASSWORD_VALUE] = smtp_password
        parameters[TLS_VALUE] = smtp_use_tls

        # creates the mime message
        mime_message = format_mime_plugin.create_message({})

        # encodes the received values into the default encoding
        name_encoded = name.encode(DEFAULT_ENCODING)
        company_encoded = company.encode(DEFAULT_ENCODING)
        from_email_encoded = from_email.encode(DEFAULT_ENCODING)
        problem_encoded = problem.encode(DEFAULT_ENCODING)

        # retrieves the current date time, and formats
        # it according to the "standard" format
        current_date_time = datetime.datetime.utcnow()
        current_date_time_formated = current_date_time.strftime(DATE_TIME_FORMAT_VALUE)

        # creates the time uid for identification of the message
        time_uid = current_date_time.strftime(TIMESTAMP_FORMAT_VALUE) + str(current_date_time.microsecond)

        # creates the email header values
        from_line = DEFAULT_ORIGIN_EMAIL
        to_line = DEFAULT_TARGET_EMAIL
        reply_to_line = REPLY_TO_LINE_FORMAT_VALUE % (name_encoded, from_email_encoded)
        subject = SUBJECT_FORMAT_VALUE % (time_uid, name_encoded, company_encoded)

        # sets the basic mime message headers
        mime_message.set_header(FROM_VALUE, from_line)
        mime_message.set_header(TO_VALUE, to_line)
        mime_message.set_header(REPLY_TO_VALUE, reply_to_line)
        mime_message.set_header(SUBJECT_VALUE, subject)
        mime_message.set_header(DATE_VALUE, current_date_time_formated)

        # writes the contents to the mime message and then retrieves
        # the complete mime message value to be used as the payload
        mime_message.write(problem_encoded)
        mime_message_value = mime_message.get_value()

        try:
            # send the email using the defined values, including the
            # constructed mime message contents
            smtp_client.send_mail(
                smtp_server,
                smtp_port,
                from_line,
                [to_line],
                mime_message_value,
                parameters
            )
        finally:
            # closes the smtp client
            smtp_client.close({})

    def _get_email_attributes(self):
        # retrieves the resources manager plugin
        resources_manager_plugin = self.plugin.resources_manager_plugin

        # retrieves the various smtp resource values that should
        # have been set in the current configuration
        smtp_server = resources_manager_plugin.get_resource("system.mail.smtp_server")
        smtp_port = resources_manager_plugin.get_resource("system.mail.smtp_port")
        smtp_use_tls = resources_manager_plugin.get_resource("system.mail.smtp_use_tls")
        smtp_user = resources_manager_plugin.get_resource("system.mail.smtp_user")
        smtp_password = resources_manager_plugin.get_resource("system.mail.smtp_password")

        # verifies that the smtp server configuration is correctly defined
        # otherwise raises an exception indicating the problem
        if not smtp_server: raise hive_site.exceptions.MissingConfiguration("smtp server configuration")

        # retrieves the data from the smtp resources, defaulting
        # to the unset value in case the server is not valid
        smtp_server_data = smtp_server.data
        smtp_port_data = smtp_port and smtp_port.data or 25
        smtp_use_tls_data = smtp_use_tls and smtp_use_tls.data or False
        smtp_user_data = smtp_user and smtp_user.data or None
        smtp_password_data = smtp_password and smtp_password.data or None

        # returns the smtp attributes as a set of tuple values to
        # be unpacked in the calling method
        return (
            smtp_server_data,
            smtp_port_data,
            smtp_use_tls_data,
            smtp_user_data,
            smtp_password_data
        )
