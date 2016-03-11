;(function (define) {
    'use strict';

    define(['backbone',
            'jquery',
            'underscore',
            'gettext',
            'text!../../../templates/learner_dashboard/sidebar.underscore'
           ],
         function(
             Backbone,
             $,
             _,
             gettext,
             sidebarTpl
         ) {
            return Backbone.View.extend({
                el: '.sidebar',
                tpl: _.template(sidebarTpl),
                initialize: function(data) {
                    this.context = data.context;
                    this.render();
                },

                render: function() {
                    this.$el.html(this.tpl(this.context));
                    return this;
                }
            });
        }
    );
}).call(this, define || RequireJS.define);
