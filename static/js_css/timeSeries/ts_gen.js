// Plotly.d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv", function(err, rows){
//
//
//   function unpack(rows, key) {
//     return rows.map(function(row) { return row[key]; });
//   }
//
// var data = [[unpack(rows, "Date"), unpack(rows, "AAPL.High")], [unpack(rows, "Date"), unpack(rows, "AAPL.Low")]]
// console.log("INTS")
// console.log(data)
// // draw_plotly_TS(data)
// })

//////////////////////
// copied from https://gist.github.com/aerispaha/63bb83208e6728188a4ee701d2b25ad5

var gd3 = d3.select('#timeseries0')

$(window).on('resize', function(data) {
  gd3.style({
      width: '100%',
      height: $('#timeseries0').width()/1.7 + "px",
    });
  gd = gd3.node();
  Plotly.Plots.resize(gd);
});

//
//
// function draw_plotly_TS(data, id = "timeseries0", names = ["One", "Two"]){
//
//   dataArray = []
//   data.forEach(function(item, i){
//     var trace = {
//       type: "scatter",
//       mode: "lines",
//       name: names[i],
//       x: item[0],
//       y: item[1],
//       line: {color: '#17BECF'} // randome color
//     }
//     dataArray.push(trace)
//   })
//
//   var layout = {
//     autosize: true,
//     title: 'Price over time',
//     xaxis: {
//       autorange: true,
//       range: ['2015-02-17', '2017-02-16'],
//       rangeselector: {buttons: [
//           {
//             count: 1,
//             label: '1m',
//             step: 'month',
//             stepmode: 'backward'
//           },
//           {
//             count: 6,
//             label: '6m',
//             step: 'month',
//             stepmode: 'backward'
//           },
//           {step: 'all'}
//         ]},
//       rangeslider: {range: ['2015-02-17', '2017-02-16']},
//       type: 'date'
//     },
//     yaxis: {
//       autorange: true,
//       range: [86.8700008333, 138.870004167],
//       type: 'linear'
//     }
//   };
//   Plotly.newPlot(id, dataArray, layout);
// }
