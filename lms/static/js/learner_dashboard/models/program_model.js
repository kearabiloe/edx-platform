/**
 * Model for Course Programs.
 */
(function (define) {
    'use strict';
    define(['backbone'], function (Backbone) {
        var Program = Backbone.Model.extend({
            initialize: function(data) {
                this.set({
                    'name': data.name,
                    'category': data.category,
                    'subtitle': data.subtitle,
                    'organizations': data.organizations,
                    'marketingUrl': data.marketing_url
                });
            }
        });
        return Program;
    });
}).call(this, define || RequireJS.define);
