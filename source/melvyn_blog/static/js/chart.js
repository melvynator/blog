$(function () {

    $(document).ready(function () {

        // Build the chart
        $('#skillDev').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie',
                backgroundColor:'rgba(255, 255, 255, 0.0)'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            title:{
                text:'Developpement',
                floating: true,
                y: 70,
                style: {
                   color: '#6a6969',
                   font: '400 20px/12px "Bree Serif", Georgia, serif'
                }
            },
            credits: {
                enabled: false
            },
            exporting: {
              enabled: false
            },
            plotOptions: {
                pie: {
                    size:100,
                    allowPointSelect: false,
                    cursor: 'pointer',
                    dataLabels: {
                      style: {
                        textShadow: false,
                        color: '#6a6969'
                      },
                      distance: 0,
                      enabled: true
                    },
                }
            },
            series: [{
                name: 'Use of the language',
                colorByPoint: true,
                data: [{
                    name: 'Python',
                    y: 55
                }, {
                    name: 'Java',
                    y: 40
                }, {
                    name: 'Others',
                    y: 5
                }]
            }]
        });
        $('#skillBdd').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie',
                backgroundColor:'rgba(255, 255, 255, 0.0)'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            title:{
                text:'Data base',
                floating: true,
                y: 70,
                style: {
                   color: '#6a6969',
                   font: '400 20px/12px "Bree Serif", Georgia, serif'
                }
            },
            credits: {
                enabled: false
            },
            exporting: {
              enabled: false
            },
            plotOptions: {
                pie: {
                    size:100,
                    allowPointSelect: false,
                    cursor: 'pointer',
                    dataLabels: {
                      style: {
                        textShadow: false,
                        color: '#6a6969'
                      },
                      distance: 0,
                        enabled: true
                    },
                }
            },
            series: [{
                name: 'Use of data base',
                colorByPoint: true,
                data: [{
                    name: 'Cassandra',
                    y: 50
                }, {
                    name: 'HBase',
                    y: 30
                }, {
                    name: 'MongoDB',
                    y: 15
                }, {
                    name: 'Mysql',
                    y: 5
                }]
            }]
        });
        $('#skillSE').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie',
                backgroundColor:'rgba(255, 255, 255, 0.0)'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            title:{
                text:'Search engine',
                floating: true,
                y: 70,
                style: {
                   color: '#6a6969',
                   font: '400 20px/12px "Bree Serif", Georgia, serif'
                }
            },
            credits: {
                enabled: false
            },
            exporting: {
              enabled: false
            },
            plotOptions: {
                pie: {
                    size:100,
                    allowPointSelect: false,
                    cursor: 'pointer',
                    dataLabels: {
                      style: {
                        textShadow: false,
                        color: '#6a6969'
                      },
                      distance: 0,
                      enabled: true
                    },
                }
            },
            series: [{
                name: 'Use of the search engine',
                colorByPoint: true,
                data: [{
                    name: 'ElasticSearch',
                    y: 60
                }, {
                    name: 'SolR',
                    y: 40
                }]
            }]
        });
    });
});
