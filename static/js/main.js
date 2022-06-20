var xValues = ["JULY", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN", "FEB", "MAR", "APR", "MAY", "JUNE"];
            var yValues = [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15, 7];

            new Chart("myChart", {
                type: "line",
                data: {
                    labels: xValues,
                    datasets: [{
                        fill: false,
                        lineTension: 1,
                        backgroundColor: "rgba(0,0,255,1.0)",
                        borderColor: "rgba(0,0,255,0.1)",
                        data: yValues
                    }]
                },
                options: {
                    legend: { display: false },
                    scales: {
                        yAxes: [{ ticks: { min: 6, max: 16 } }],
                    }
                }
            });