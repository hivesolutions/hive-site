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

jQuery(document).ready(function() {
    // retrieves the browser name and converts it to lowercase
    var browserName = BrowserDetect.browser.toLowerCase();

    // retrieves the browser version
    var browserVersion = BrowserDetect.version;

    // retrieves the browser operative system and converts it to lowercase
    var browserOs = BrowserDetect.os.toLowerCase();

    // adds the browser classes to the body item
    jQuery("body").addClass(browserName);
    jQuery("body").addClass(browserName + "-" + browserVersion);
    jQuery("body").addClass(browserOs);

    // creates the text field
    jQuery(":text").textfield();

    // creates the text area
    jQuery("textarea").textarea();

    // creates the submit button
    jQuery("#send-form-button").submitbutton();

    // creates the slideshow
    jQuery("#screenshots-button").slideshow({
        screenshotsPrefix : "resources/screenshots/",
        screenshots : ["omni-screen-1.jpg", "omni-screen-2.jpg",
                "omni-screen-3.jpg", "omni-screen-4.jpg"]
    });

    // retrieves the portfolio slider contents
    var portfolioSliderContents = jQuery("#portfolio-slider-contents");

    // retrieves the portfolio slider selector
    var portfolioSliderSelector = jQuery("#portfolio-slider-selector");

    // retrieves the portfolio data parsed
    var portfolioDataParsed = jQuery("#portfolio-data").parseData();

    // retrieves the portfolio data set
    var portfolioDataSets = portfolioDataParsed != null
            ? portfolioDataParsed["set"]
            : [];

    // creates the slider
    jQuery("#portfolio-slider").slider("default", {
                "contents" : portfolioSliderContents,
                "selector" : portfolioSliderSelector,
                "sets" : portfolioDataSets
            });

    // iterates over each error
    jQuery(".form-error").each(function(index, element) {
                // retrieves the element reference
                var elementReference = jQuery(element);

                // retrieves the current status
                var currentStatus = elementReference.attr("data-current_status");

                // in case there is a status defined
                if (currentStatus != "") {
                    // shows the value
                    elementReference.addClass("visible");
                }
            });

    // registers for the click event
    jQuery("#screenshots-button").click(function() {
                jQuery.scrollTo(jQuery("#jquery-slideshow"), 800, {
                            offset : {
                                top : -50,
                                left : 0
                            }
                        });
            });

    // registers for the click event
    jQuery("#find-us-location-button").click(function(event) {
                // retrieves the map balloon
                var mapBallon = jQuery("#map-balloon");

                // in case the map balloon is visible
                if (mapBallon.is(":visible")) {
                    // fades out the map balloon
                    mapBallon.fadeOut(150);
                } else {
                    // fades in the map balloon
                    mapBallon.fadeIn(250);
                }
            });

    // registers for the mouse enter event
    jQuery("#blog-button").mouseenter(function(event) {
                jQuery("#blog-balloon").show();
            });

    // registers for the mouse leave event
    jQuery("#blog-button").mouseleave(function(event) {
                jQuery("#blog-balloon").hide();
            });

    // registers for the mouse enter event
    jQuery("#twitter-button").mouseenter(function(event) {
                jQuery("#twitter-balloon").show();
            });

    // registers for the mouse leave event
    jQuery("#twitter-button").mouseleave(function(event) {
                jQuery("#twitter-balloon").hide();
            });

    // registers for the mouse enter event
    jQuery("#facebook-button").mouseenter(function(event) {
                jQuery("#facebook-balloon").show();
            });

    // registers for the mouse leave event
    jQuery("#facebook-button").mouseleave(function(event) {
                jQuery("#facebook-balloon").hide();
            });
});
