;(function (define) {
    'use strict';

    define([
        'js/learner_dashboard/views/program_list_view',
        'js/learner_dashboard/views/sidebar_view'
    ],
    function (ProgramListView, SidebarView) {
        return function (options) {
            var listView = new ProgramListView({
                el: '.program-cards-container',
                context: options
            });
            
            var rightPanelView = new SidebarView({
                el: '.sidebar',
                context: options
            });
        };
    });
}).call(this, define || RequireJS.define);
