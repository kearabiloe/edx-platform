define([
        'edx-ui-toolkit/js/utils/string-utils',
        'edx-ui-toolkit/js/utils/html-utils',
        'domReady!',
        'jquery',
        'backbone',
        'underscore',
        'gettext'
    ],
    function(StringUtils, HtmlUtils) {
        'use strict';

        // Install utility classes in the edX namespace to make them
        // available to code that doesn't use RequireJS,
        // e.g. XModules and XBlocks.
        this.edx = this.edx || {};
        this.edx.StringUtils = StringUtils;
        this.edx.HtmlUtils = HtmlUtils;
    });
