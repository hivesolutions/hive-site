// Hive Colony Framework
// Copyright (C) 2008 Hive Solutions Lda.
//
// This file is part of Hive Colony Framework.
//
// Hive Colony Framework is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Hive Colony Framework is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

// __author__    = João Magalhães <joamag@hive.pt>
// __version__   = 1.0.0
// __revision__  = $LastChangedRevision: 9229 $
// __date__      = $LastChangedDate: 2010-07-08 18:07:05 +0100 (qui, 08 Jul 2010) $
// __copyright__ = Copyright (c) 2008 Hive Solutions Lda.
// __license__   = GNU General Public License (GPL), Version 3

var Base64 = Base64 || {};

/**
 * The key string to be used in base64.
 *
 * @type String
 */
Base64._keyString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

Base64.encode = function(input, encode) {
    // the output string to be used
    var output = "";
    var character1, character2, character3;
    var encoding1, encoding2, encoding3, encoding4;
    var index = 0;

    // retrieves the encode value
    encode = encode ? encode : false;

    // encodes the input into utf
    input = encode ? input.encodeUtf() : input;

    // iterates over the input length
    while (index < input.length) {
        // retrieves the various characters
        character1 = input.charCodeAt(index++);
        character2 = input.charCodeAt(index++);
        character3 = input.charCodeAt(index++);

        // retrieves the encoding indexes
        encoding1 = character1 >> 2;
        encoding2 = ((character1 & 3) << 4) | (character2 >> 4);
        encoding3 = ((character2 & 15) << 2) | (character3 >> 6);
        encoding4 = character3 & 63;

        // in case the input is not a number
        if (isNaN(character2)) {
            encoding3 = encoding4 = 64;
        } else if (isNaN(character3)) {
            encoding4 = 64;
        }

        // creates the output
        output = output + Base64._keyString.charAt(encoding1)
                + Base64._keyString.charAt(encoding2)
                + Base64._keyString.charAt(encoding3)
                + Base64._keyString.charAt(encoding4);
    }

    // returns the output
    return output;
}

Base64.decode = function(input, decode) {
    var output = "";
    var character1, character2, character3;
    var encoding1, encoding2, encoding3, encoding4;
    var index = 0;

    // retrieves the decode value
    decode = decode ? decode : false;

    // removes all the invalid values from the input
    input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");

    // iterates over the input length
    while (index < input.length) {
        // retrieves the various encoded values
        encoding1 = Base64._keyString.indexOf(input.charAt(index++));
        encoding2 = Base64._keyString.indexOf(input.charAt(index++));
        encoding3 = Base64._keyString.indexOf(input.charAt(index++));
        encoding4 = Base64._keyString.indexOf(input.charAt(index++));

        // converts the encoded values into characters
        character1 = (encoding1 << 2) | (encoding2 >> 4);
        character2 = ((encoding2 & 15) << 4) | (encoding3 >> 2);
        character3 = ((encoding3 & 3) << 6) | encoding4;

        output = output + String.fromCharCode(character1);

        if (encoding3 != 64) {
            output = output + String.fromCharCode(character2);
        }

        if (encoding4 != 64) {
            output = output + String.fromCharCode(character3);
        }
    }

    // decodes the output from utf
    output = decode ? output.decodeUtf() : output;

    // returns the output
    return output;
}
