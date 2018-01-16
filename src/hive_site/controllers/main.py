#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Website
# Copyright (c) 2008-2018 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2018 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

import datetime

import colony

import hive_site

from .base import BaseController

DATE_TIME_FORMAT_VALUE = "%a, %d %b %Y %H:%M:%S +0000 (UTC)"
""" The format for the displayed date times """

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

models = colony.__import__("models")
mvc_utils = colony.__import__("mvc_utils")

class MainController(BaseController):

    @mvc_utils.serialize
    def index(self, request):
        self._template(
            request = request,
            partial_page = "general/index.html.tpl",
            area = "home",
            title = "Hive Solutions"
        )

    @mvc_utils.serialize
    def contact(self, request):
        self._template(
            request = request,
            partial_page = "general/contact.html.tpl",
            area = "about",
            title = "Hive Solutions - Contact"
        )

    @mvc_utils.serialize
    def contact_process(self, request):
        # retrieves the contact form from the request and runs the
        # proper process operation to create the contact
        contact_form = request.field("contact_form", {})
        contact_form = self._process_contact(request, contact_form)

        # in case the validation goes wrong must present the proper
        # information to the user so that he may correct it
        if not contact_form.is_valid():
            return self._template(
                request = request,
                partial_page = "general/contact.html.tpl",
                area = "about",
                title = "Hive Solutions - Contact",
                contact_form = contact_form,
                contact_form_error = REQUIRED_FIELDS_MISSING_ERROR_TEXT
            )

        # sends the email using the information present in the contact
        # form this is a synchronous operation and it's execution may
        # take a large amount of time (use it carefully)
        try: self._send_contact_form_email(request, contact_form)
        except:
            # in case the debug level is the required
            # to re-throw exception, performs the re-throw
            if request.is_debug(): raise
            return self._template(
                request = request,
                partial_page = "general/contact.html.tpl",
                area = "about",
                title = "Hive Solutions - Contact",
                contact_form = contact_form,
                contact_form_error = TECHNICAL_PROBLEMS_WHILE_SENDING_ERROR_TEXT
            )

        # sets the name attribute in the session and then redirects
        # the user to the proper thank you page (as expected)
        request.set_s("name", contact_form.name)
        self.redirect_base_path(request, "thankyou#thank-you-wrapper", quote = False)

    @mvc_utils.serialize
    def thankyou(self, request):
        name = request.get_s("name")
        self._template(
            request = request,
            partial_page = "general/thankyou.html.tpl",
            area = "about",
            title = "Hive Solutions - Thank You",
            name = name
        )

    @mvc_utils.serialize
    def products(self, request):
        self._template(
            request = request,
            partial_page = "general/products.html.tpl",
            area = "products",
            title = "Hive Solutions - Products"
        )

    @mvc_utils.serialize
    def consulting(self, request):
        self._template(
            request = request,
            partial_page = "general/consulting.html.tpl",
            area = "consulting",
            title = "Hive Solutions - Consulting"
        )

    @mvc_utils.serialize
    def saas(self, request):
        self._template(
            request = request,
            partial_page = "general/saas.html.tpl",
            area = "consulting",
            title = "Hive Solutions - SaaS"
        )

    @mvc_utils.serialize
    def cloud(self, request):
        self._template(
            request = request,
            partial_page = "general/cloud.html.tpl",
            area = "consulting",
            title = "Hive Solutions - Cloud"
        )

    @mvc_utils.serialize
    def social(self, request):
        self._template(
            request = request,
            partial_page = "general/social.html.tpl",
            area = "consulting",
            title = "Hive Solutions - Social"
        )

    @mvc_utils.serialize
    def mobile(self, request):
        self._template(
            request = request,
            partial_page = "general/mobile.html.tpl",
            area = "consulting",
            title = "Hive Solutions - Mobile"
        )

    @mvc_utils.serialize
    def labs(self, request):
        self._template(
            request = request,
            partial_page = "general/labs.html.tpl",
            area = "labs",
            title = "Hive Solutions - Labs"
        )

    @mvc_utils.serialize
    def people(self, request):
        self._template(
            request = request,
            partial_page = "general/people.html.tpl",
            area = "people",
            title = "Hive Solutions - People"
        )

    @mvc_utils.serialize
    def about(self, request):
        self._template(
            request = request,
            partial_page = "general/about.html.tpl",
            area = "about",
            title = "Hive Solutions - About"
        )

    @mvc_utils.serialize
    def language(self, request):
        locale = request.field("locale", None)
        self.set_locale_session(request, locale)
        self.redirect_back(request, "index")

    def _process_contact(self, request, contact):
        contact_form = models.ContactForm.new(map = contact)
        contact_form.validate()
        return contact_form

    def _send_contact_form_email(self, request, contact_form):
        # retrieves the client_smtp plugin
        client_smtp_plugin = self.plugin.client_smtp_plugin

        # retrieves the mime plugin
        mime_plugin = self.plugin.mime_plugin

        # retrieves the contact form attributes
        name = contact_form.name
        company = contact_form.company
        from_email = contact_form.email
        problem = contact_form.problem

        # retrieves the email attributes
        smtp_server, smtp_port, smtp_use_tls, smtp_user, smtp_password = self._get_email_attributes()

        # creates a new smtp client, using the client_smtp plugin
        smtp_client = client_smtp_plugin.create_client({})

        # opens the smtp client
        smtp_client.open({})

        # creates the parameters map
        parameters = {}

        # sets the authentication parameters
        parameters["username"] = smtp_user
        parameters["password"] = smtp_password
        parameters["tls"] = smtp_use_tls

        # creates the mime message
        mime_message = mime_plugin.create_message({})

        # encodes the received values into the default encoding
        name_encoded = name.encode("utf-8")
        company_encoded = company.encode("utf-8")
        from_email_encoded = from_email.encode("utf-8")
        problem_encoded = problem.encode("utf-8")

        # retrieves the current date time, and formats
        # it according to the "standard" format
        current_date_time = datetime.datetime.utcnow()
        current_date_time_formated = current_date_time.strftime(DATE_TIME_FORMAT_VALUE)

        # creates the time uid for identification of the message
        time_uid = current_date_time.strftime(TIMESTAMP_FORMAT_VALUE) + str(current_date_time.microsecond)

        # creates the email header values
        from_line = DEFAULT_ORIGIN_EMAIL
        to_line = DEFAULT_TARGET_EMAIL
        reply_to_line = "%s <%s>" % (name_encoded, from_email_encoded)
        subject = SUBJECT_FORMAT_VALUE % (time_uid, name_encoded, company_encoded)

        # sets the basic mime message headers
        mime_message.set_header("From", from_line)
        mime_message.set_header("To", to_line)
        mime_message.set_header("Reply-To", reply_to_line)
        mime_message.set_header("Subject", subject)
        mime_message.set_header("Date", current_date_time_formated)

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
        if not smtp_server: raise hive_site.MissingConfiguration("smtp server configuration")

        # retrieves the data from the smtp resources, defaulting
        # to the unset value in case the server is not valid
        smtp_server_data = smtp_server.data
        smtp_port_data = smtp_port and smtp_port.data or 25
        smtp_use_tls_data = smtp_use_tls and smtp_use_tls.data or False
        smtp_user_data = smtp_user and smtp_user.data or None
        smtp_password_data = smtp_password and smtp_password.data or None

        # uses the base configuration values to try to retrieve the
        # smtp attributes, defaulting to the the pre-defined resource
        # based values in case the values are not found
        smtp_server_data = colony.conf("SMTP_HOST", smtp_server_data)
        smtp_port_data = colony.conf("SMTP_PORT", smtp_port_data, cast = int)
        smtp_use_tls_data = colony.conf("SMTP_STARTTLS", smtp_use_tls_data, cast = bool)
        smtp_user_data = colony.conf("SMTP_USER", smtp_user_data)
        smtp_password_data = colony.conf("SMTP_PASSWORD", smtp_password_data)

        # returns the smtp attributes as a set of tuple values to
        # be unpacked in the calling method
        return (
            smtp_server_data,
            smtp_port_data,
            smtp_use_tls_data,
            smtp_user_data,
            smtp_password_data
        )
