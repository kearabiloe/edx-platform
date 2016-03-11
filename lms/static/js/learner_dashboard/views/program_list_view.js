;(function (define) {
    'use strict';

    define(['backbone',
            'jquery',
            'underscore',
            'gettext',
            'js/learner_dashboard/models/program_model',
            'js/learner_dashboard/collections/program_collection',
            'js/learner_dashboard/views/program_card_view'
           ],
         function(
             Backbone,
             $,
             _,
             gettext,
             ProgramModel,
             ProgramCollection,
             ProgramCardView
         ) {
            return Backbone.View.extend({
                el: '.program-cards-container',
                initialize: function(data) {
                    var context = data.context;
                    this.collection = new ProgramCollection(context.programsData);
                    this.render()
                },

                render: function() {
                    var cardList = [];
                    this.collection.each(function(program){
                        var cardView = new ProgramCardView({model:program});
                        cardList.push(cardView.el);
                    });
                    this.$el.html(cardList);
                    return this;
                }
            });
        }
    );
}).call(this, define || RequireJS.define);
