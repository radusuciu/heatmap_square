Vue.use(VueResource);

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello world!',
        userData: '',
        heatmapData: ''
    },
    methods: {
        generate: function() {
            this.$http.post('/heatmap', { data: this.userData }).then(function(response) {
                this.heatmapData = response.body;
            });
        }
    }
});
