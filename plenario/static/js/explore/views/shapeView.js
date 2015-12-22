var app = app || {};

    app.ShapeView = Backbone.View.extend({

        el: $('#shapes-list'),
        //template:

        initialize: function() {
            this.collection = new app.Shapes();
            this.collection.fetch({reset:true});
            if (resp) {
                this.resp = resp;
                this.query = this.resp.query;
                this.collection = this.setIntersection();
            }
            this.listenTo(this.collection, 'reset', this.render);
            //this.listenTo(this.collection, 'update', function(){console.log("update");this.render;});
        },

        render: function(){
            console.log("calling rendering");
            console.log(this.collection.toJSON());
            template = template_cache('shapesList', {shapes: this.collection.toJSON()});
            this.$el.html(template);
        },

        setIntersection: function(){
            var self = this;
            if (self.resp) {
                $.when(self.getIntersection()).then(
                    function(resp) {
                        var data = {
                            "meta": {"status": "ok", "message": ""},
                            "objects": [{
                                "dataset_name": "chicago_pedestrian_streets",
                                "num_geoms": 2
                            }, {
                                "dataset_name": "chicago_city_limits",
                                "num_geoms": 1
                            }, {
                                "dataset_name": "chicago_tif_districts",
                                "num_geoms": 2
                            }, {
                                "dataset_name": "chicago_wards",
                                "num_geoms": 9
                            }, {"dataset_name": "chicago_major_streets", "num_geoms": 28}]
                        };
                        data.objects.forEach(function (intersect) {
                            self.collection.get(intersect.dataset_name).set(intersect);
                        });
                        console.log(self.collection);//right
                        return self.collection;
                });
                return self.collection;
            }
            //return self.collection;
        },

        getIntersection: function(){
            var self = this;
            var q = this.getGeoJson();
            return $.ajax({
                url: '/v1/api/shapes/intersections/'+ q,
               // url: "http://plenar.io/v1/api/shapes/intersections/{'type':'Feature','properties':{},'geometry':{'type':'Polygon','coordinates':[[[-87.67248630523682,41.86454328565965],[-87.67248630523682,41.872117384500754],[-87.6549768447876,41.872117384500754],[-87.6549768447876,41.86454328565965],[-87.67248630523682,41.86454328565965]]]}}",
                //crossOrigin: true,
                //xhrFields: {withCredentials:true},
                dataType: 'json',
            });
        },
        getGeoJson: function() {
            var self = this;
            return self.query.location_geom__within;
        },
        //downLoad: function() {
        //    var self = this;
        //    self.collection.forEach(function(dataset){
        //        dataset.set("")
        //
        //    })
        //
        //}

    });