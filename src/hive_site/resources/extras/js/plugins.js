// Hive Solutions Website
// Copyright (C) 2010 Hive Solutions Lda.
//
// This file is part of Hive Solutions Website.
//
// Hive Solutions Website is confidential and property of Hive Solutions Lda.,
// its usage is constrained by the terms of the Hive Solutions
// Confidential Usage License.
//
// Hive Solutions Website should not be distributed under any circumstances,
// violation of this may imply legal action.
//
// If you have any questions regarding the terms of this license please
// refer to <http://www.hive.pt/licenses/>.

// __author__    = João Magalhães <joamag@hive.pt>
// __version__   = 1.0.0
// __revision__  = $LastChangedRevision$
// __date__      = $LastChangedDate$
// __copyright__ = Copyright (c) 2010 Hive Solutions Lda.
// __license__   = Hive Solutions Confidential Usage License (HSCUL)

(function($) {
    jQuery.fn.textfield = function(method, options) {
        // the default values for the menu
        var defaults = {};

        // sets the default options value
        var options = options ? options : {};

        // constructs the options
        var options = jQuery.extend(defaults, options);

        // sets the jquery matched object
        var matchedObject = this;

        /**
         * Initializer of the plugin, runs the necessary functions to initialize
         * the structures.
         */
        var initialize = function() {
            _appendHtml();
            _registerHandlers();
        };

        /**
         * Creates the necessary html for the component.
         */
        var _appendHtml = function() {
            // iterates over all the items in the matched object
            matchedObject.each(function(index, element) {
                // retrieves the element reference
                var elementReference = jQuery(element);

                // retrieves the current status
                var currentStatus = elementReference.attr("data-current_status");

                // retrieves the current error
                var currentError = elementReference.attr("data-error");

                // retrieves the original value
                var originalValue = elementReference.attr("data-original_value");

                // in case there is an error
                if (currentError != "") {
                    // adds the invalid mode class
                    elementReference.addClass("invalid");
                } else if (currentStatus != "") {
                    elementReference.attr("value", currentStatus);
                }

                // retrieves the current value
                var currentValue = elementReference.attr("value");

                // in case the current value is the original one
                if (currentValue == originalValue) {
                    // adds the lower (background) mode class
                    elementReference.addClass("lower");
                }
            });
        };

        /**
         * Registers the event handlers for the created objects.
         */
        var _registerHandlers = function() {
            // registers for the focus event
            matchedObject.focus(function(event) {
                        // retrieves the element
                        var element = jQuery(this);

                        // retrieves the current value
                        var currentValue = element.attr("value");

                        // retrieves the original value
                        var originalValue = element.attr("data-original_value");

                        // retrieves the current error
                        var currentError = element.attr("data-error");

                        // retrieves the current status
                        var currentStatus = element.attr("data-current_status");

                        // in case the current value is
                        // the original one
                        if (currentValue == originalValue) {
                            // sets the value attribute to empty
                            element.attr("value", "");

                            // removes the lower class
                            element.removeClass("lower");

                            // in case there is an error
                            if (currentError != "") {
                                // removes the invalid mode class
                                element.removeClass("invalid");
                            }
                        }

                        // adds the active class
                        element.addClass("active");
                    });

            // registers for the blur event
            matchedObject.blur(function(event) {
                        // retrieves the element
                        var element = jQuery(this);

                        // retrieves the current value
                        var currentValue = element.attr("value");

                        // retrieves the original value
                        var originalValue = element.attr("data-original_value");

                        // retrieves the current error
                        var currentError = element.attr("data-error");

                        // retrieves the current status
                        var currentStatus = element.attr("data-current_status");

                        // in case the current value is empty
                        if (currentValue == "") {
                            // sets the value attribute to the original value
                            element.attr("value", originalValue);

                            // adds the lower class
                            element.addClass("lower");

                            // in case there is an error
                            if (currentError != "") {
                                // adds the invalid mode class
                                element.addClass("invalid");
                            }
                        }

                        // removes the active class
                        element.removeClass("active");
                    });
        };

        // initializes the plugin
        initialize();

        // returns the object
        return this;
    };
})(jQuery);

(function($) {
    jQuery.fn.textarea = function(method, options) {
        // the default values for the menu
        var defaults = {};

        // sets the default options value
        var options = options ? options : {};

        // constructs the options
        var options = jQuery.extend(defaults, options);

        // sets the jquery matched object
        var matchedObject = this;

        /**
         * Initializer of the plugin, runs the necessary functions to initialize
         * the structures.
         */
        var initialize = function() {
            _appendHtml();
            _registerHandlers();
        };

        /**
         * Creates the necessary html for the component.
         */
        var _appendHtml = function() {
            // iterates over all the items in the matched object
            matchedObject.each(function(index, element) {
                // retrieves the element reference
                var elementReference = jQuery(element);

                // retrieves the current status
                var currentStatus = elementReference.attr("data-current_status");

                // retrieves the current error
                var currentError = elementReference.attr("data-error");

                // retrieves the original value
                var originalValue = elementReference.attr("data-original_value");

                // in case there is an error
                if (currentError != "") {
                    // adds the invalid mode class
                    elementReference.addClass("invalid");
                } else if (currentStatus != "") {
                    // in case the browser is webkit based the text area
                    // requires some time before it is changed
                    // otherwise the browser might crash
                    if (jQuery.browser.safari) {
                        // sets the timeout function to change the
                        // text area value
                        setTimeout(function() {
                                    elementReference.get(0).value = currentStatus;
                                    elementReference.removeClass("lower");
                                }, 10);
                    } else {
                        // sets the text area value
                        elementReference.get(0).value = currentStatus;
                    }
                }

                // retrieves the current value
                var currentValue = elementReference.get(0).value;

                // in case the current value is the original one
                if (currentValue == originalValue) {
                    // adds the lower (background) mode class
                    elementReference.addClass("lower");
                }
            });

        };

        /**
         * Registers the event handlers for the created objects.
         */
        var _registerHandlers = function() {
            // registers for the focus event
            matchedObject.focus(function(event) {
                        // retrieves the element
                        var element = jQuery(this);

                        // retrieves the current value
                        var currentValue = element.get(0).value;

                        // retrieves the original value
                        var originalValue = element.attr("data-original_value");

                        // retrieves the current error
                        var currentError = element.attr("data-error");

                        // retrieves the current status
                        var currentStatus = element.attr("data-current_status");

                        // in case the current value is
                        // the original one
                        if (currentValue == originalValue) {
                            // sets teh value reference value as empty
                            element.get(0).value = "";

                            // removes the lower class
                            element.removeClass("lower");

                            // in case there is an error
                            if (currentError != "") {
                                // removes the invalid mode class
                                element.removeClass("invalid");
                            }
                        }

                        // adds the active class
                        element.addClass("active");
                    });

            // registers for the blur event
            matchedObject.blur(function(event) {
                        // retrieves the element
                        var element = jQuery(this);

                        // retrieves the current value
                        var currentValue = element.get(0).value;

                        // retrieves the original value
                        var originalValue = element.attr("data-original_value");

                        // retrieves the current error
                        var currentError = element.attr("data-error");

                        // retrieves the current status
                        var currentStatus = element.attr("data-current_status");

                        // in case the current value is empty
                        if (currentValue == "") {
                            // sets teh value reference value as the original value
                            element.get(0).value = originalValue;

                            // adds the lower class
                            element.addClass("lower");

                            // in case there is an error
                            if (currentError != "") {
                                // adds the invalid mode class
                                element.addClass("invalid");
                            }
                        }

                        // removes the active class
                        element.removeClass("active");
                    });
        };

        // initializes the plugin
        initialize();

        // returns the object
        return this;
    };
})(jQuery);

(function($) {
    jQuery.fn.submitbutton = function(method, options) {
        // the default values for the menu
        var defaults = {};

        // sets the default options value
        var options = options ? options : {};

        // constructs the options
        var options = jQuery.extend(defaults, options);

        // sets the jquery matched object
        var matchedObject = this;

        /**
         * Initializer of the plugin, runs the necessary functions to initialize
         * the structures.
         */
        var initialize = function() {
            _appendHtml();
            _registerHandlers();
        };

        /**
         * Creates the necessary html for the component.
         */
        var _appendHtml = function() {
        };

        /**
         * Registers the event handlers for the created objects.
         */
        var _registerHandlers = function() {
            // registers for the click event
            matchedObject.click(function() {
                        // in case the form is already being sent
                        if (matchedObject.attr("sending") == "true") {
                            return;
                        }

                        // retrieves the parent form
                        var parentForm = matchedObject.parents("form");

                        // resets the text values
                        __resetTextValues(matchedObject, options, parentForm);

                        // sets the sending flag as true
                        matchedObject.attr("sending", "true");

                        // changes the label
                        matchedObject.html("Sending...");

                        // submits the parent form
                        parentForm.submit();
                    });
        };

        var __resetTextValues = function(matchedObject, options, parentForm) {
            // retreives the text fields
            var textFields = jQuery(":text", parentForm);

            // retreives the text areas
            var textAreasFields = jQuery("textarea", parentForm);

            // iterates over each of the text fields
            textFields.each(function(index, element) {
                // retrieves the value reference
                var elementReference = jQuery(element);

                // retrieves the current value
                var currentValue = elementReference.attr("value");

                // retrieves the original value
                var originalValue = elementReference.attr("data-original_value");

                // in case the current value is the original one
                if (currentValue == originalValue) {
                    // sets the element value to empty
                    // avoids sending the default (original value)
                    elementReference.attr("value", "");
                }
            });

            // iterates over each of the text areas
            textAreasFields.each(function(index, element) {
                // retrieves the value reference
                var elementReference = jQuery(element);

                // retrieves the current value
                var currentValue = elementReference.get(0).value;

                // retrieves the original value
                var originalValue = elementReference.attr("data-original_value");

                // in case the current value is the original one
                if (currentValue == originalValue) {
                    // sets the element value to empty
                    // avoids sending the default (original value)
                    elementReference.get(0).value = "";
                }
            });
        };

        // initializes the plugin
        initialize();

        // returns the object
        return this;
    };
})(jQuery);
