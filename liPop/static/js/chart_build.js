// All the graphics are constructed in this file


//////////////////////////////// SPIDER CHART //////////////////////////////////
AXISTITLES = ["Discussion\n forums (SO)", "Developer\n activity (GH)", "Web search\n (Google data)", "Download\n volumes", "Documentation \n quality"]


function radarConstructor(tag, arrayOfDataArrays = [[1, 1, 1, 1, 1]], axisTitles = AXISTITLES) {

  var marksCanvas = document.getElementById(tag);

  var dataset = []
  arrayOfDataArrays.forEach(function(array, i) {
    dataset.push({
      backgroundColor: hexToRgb(COLORPAL[i], .3),
      pointBorderColor: hexToRgb(COLORPAL[i], .4),
      pointRadius: 4,
      pointBorderWidth: 3, //
      pointBackgroundColor: hexToRgb(COLORPAL[i], .35),
      data: array,
      pointHoverRadius: 6, //
    })
  })
  var marksData = {
    labels: AXISTITLES,
    datasets: dataset,
  };

  // Options
  Chart.defaults.global.defaultFontFamily = "Lato";
  Chart.defaults.global.defaultFontSize = 12;
  var chartOptions = {
    // scale: {
    //   ticks: {
    //     beginAtZero: true, //
    //     min: 0, //
    //     max: 1, //
    //     stepSize: .2 //
    //   },
    //   pointLabels: {
    //     fontSize: 10 //
    //   }
    // },
    legend: {
      display: false,
    }
  }

  // Drawing it
  var radarChart = new Chart(marksCanvas, {
    type: 'radar',
    options: chartOptions,
    data: marksData
  });
}

// Todo:
// - info additionel hovering (links)
// - https://stackoverflow.com/questions/26521352/create-dynamic-chart-with-chart-js


///////////////////////////// SPIDER CHART (OLD) ///////////////////////////////

// AXISTITLES = ["Discussion forums (SO)", "Developer activity (GH)", "Web search (Google data)"
//   , "Download volumes (ditto)", "Documentation quality"]

// input: tag corresponding to div id (str), data (array of array),  titles (array)
// function radarConstructor(tag, arrayOfDataArrays = [[1,1,1,1,1]], axisTitles = AXISTITLES) {
//
//   var w = 500;
//   var h = 500;
//   // var colorscale = d3.scale.category10();
//   // console.log(colorscale)
//   var dataSup = []  // builds the proper object for feeding into RadarChart
//   arrayOfDataArrays.forEach(function(array, i){
//     var dataSub = []
//     array.forEach(function(measurement, j){
//       dataSub.push({axis: axisTitles[j], value: measurement})
//     })
//     dataSup.push(dataSub)
//   })
//
//   // clumsy color generating function...
//   i = 0 // clumsy...
//   couleur = function(){
//     out = COLORPAL[i]
//     i++
//     return(out)
//   }
//   var colorscale = d3.scale.linear()
//     .domain([0, 10])
//     .range(['yellow', 'red']);
//   //Options for the Radar chart, other than default
//   var mycfg = {
//     w: w,
//     h: h,
//     maxValue: 0.6,
//     levels: 6,
//     ExtraWidthX: 200,
//     ExtraWidthY: 100
//     , color: couleur
//   }
//
//   //Call function to draw the Radar chart
//   //Will expect that data is in %'s
//   RadarChart.draw("#" + tag, dataSup, mycfg);
// }

//////////////////////////////// LINE CHART ////////////////////////////////////

// input: data (an array of arrays, an id, the latter of the form [dates, prices], names (an array), title (str))
function drawPlotlyTS(data, id = "timeseries0", names = ["One", "Two"], title = "Downloads") {

  dataArray = []
  range = []
  data.forEach(function(item, i) { // constuct Trace object to feed into Plotly.newPlot
    // get range of item[1]
    // if top of range higher that current top, raise it... same with bottom
    var trace = {
      type: "scatter",
      mode: "lines",
      name: names[i],
      x: item[0],
      y: item[1],
      line: {
        color: COLORPAL[i]
      }
    }
    // console.log("names[i]: ",  +names[i])
    dataArray.push(trace)
  })

  var layout = { // constuct Layout object to feed into Plotly.newPlot
    legend: {
      x: 0.2,
      y: 0.5
    },
    autosize: true,
    title: title,
    xaxis: {
      autorange: true,
      range: ['2010-02-17', '2017-02-16'],
      rangeselector: {
        buttons: [{
            count: 1,
            label: '1m',
            step: 'month',
            stepmode: 'backward'
          },
          {
            count: 6,
            label: '6m',
            step: 'month',
            stepmode: 'backward'
          },
          {
            step: 'all'
          }
        ]
      },
      rangeslider: {
        range: ['2015-02-17', '2017-02-16']
      }, // Change that to earliest inception dte
      type: 'date'
    },
    yaxis: {
      autorange: true,
      range: [86.8700008333, 138.870004167], // must make this adaptive...
      type: 'linear'
    }
  };
  Plotly.newPlot(id, dataArray, layout);
}

// FOLLOWING IS RELATED TO RADAR
// $(document).ready(function(){

// ////////////////////////////////////////////
// /////////// Initiate legend ////////////////
// ////////////////////////////////////////////
//
// var svg = d3.select('#body')
//   .selectAll('svg')
//   .append('svg')
//   .attr("width", w+300)
//   .attr("height", h)
//
// //Create the title for the legend
// var text = svg.append("text")
//   .attr("class", "title")
//   .attr('transform', 'translate(90,0)')
//   .attr("x", w - 70)
//   .attr("y", 10)
//   .attr("font-size", "12px")
//   .attr("fill", "#404040")
//   .text("What % of owners use a specific service in a week");
//
// //Initiate Legend
// var legend = svg.append("g")
//   .attr("class", "legend")
//   .attr("height", 100)
//   .attr("width", 200)
//   .attr('transform', 'translate(90,20)')
//   ;
//   //Create colour squares
// legend.selectAll('rect')
//   .data(LegendOptions)
//   .enter()
//   .append("rect")
//   .attr("x", w - 65)
//   .attr("y", function(d, i){ return i * 20;})
//   .attr("width", 10)
//   .attr("height", 10)
//   .style("fill", function(d, i){ return colorscale(i);})
//   ;
// //Create text next to squares
// legend.selectAll('text')
//   .data(LegendOptions)
//   .enter()
//   .append("text")
//   .attr("x", w - 52)
//   .attr("y", function(d, i){ return i * 20 + 9;})
//   .attr("font-size", "11px")
//   .attr("fill", "#737373")
//   .text(function(d) { return d; })
//   ;
// //
// // });
/// });

//////////////// HELPERS //////

function hexToRgb(hex, alpha = 1) {
  // Expand shorthand form (e.g. "03F") to full form (e.g. "0033FF")
  var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
  hex = hex.replace(shorthandRegex, function(m, r, g, b) {
    return r + r + g + g + b + b;
  });

  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  out = {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  };
  return ("rgba(" + out.r + "," + out.g + "," + out.b + "," + alpha + ")")

}
