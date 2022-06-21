var xValues = []
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
// console.log([{%for data in chart_data%} months['{{data.yearmonth}}' -1],{%endfor%}]);
// var chart_data = "{{chart_data}}"
// json_data = JSON.parse(chart_data)
// chart_data = JSON.parse(chart_data)
console.log(chart_data)
console.log(typeof chart_data)
// for (var i=0; i<chart_data.length; i += 1) {
//     console.log(months[chart_data[i]]);
//     xValues.push(months[chart_data[i].yearmonth -1]);
// }
// {% for data in chart_data %}
// xValues.push(months['{{data.yearmonth}}' -1)
// {%endfor%}
console.log(chart_data.labels, chart_data.data)
            var yValues = [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15, 7];

            new Chart("myChart", {
                type: "line",
                data: {
                    labels: chart_data.labels,
                    datasets: [{
                        fill: false,
                        lineTension: 1,
                        backgroundColor: "rgba(0,0,255,1.0)",
                        borderColor: "rgba(0,0,255,0.1)",
                        data: chart_data.data
                    }]
                },
                options: {
                    legend: { display: false },
                    scales: {
                        yAxes: [{ ticks: { min: 6, max: 16 } }],
                    }
                }
            });