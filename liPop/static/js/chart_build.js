
AXISTITLES = ["Discussion forums (SO)", "Developer activity (GH)", "Web search (Google data)"
  , "Download volumes (ditto)", "Documentation quality"]


// input: tag corresponding to div id (str), data (array of array),  titles (array)
function radarConstructor(tag, arrayOfDataArrays = [[1,1,1,1,1]], axisTitles = AXISTITLES) {

  var w = 500;
  var h = 500;
  var colorscale = d3.scale.category10();

  var dataSup = []  // builds the proper object for feeding into RadarChart
  arrayOfDataArrays.forEach(function(array, i){
    var dataSub = []
    array.forEach(function(measurement, j){
      dataSub.push({axis: axisTitles[j], value: measurement})
    })
    dataSup.push(dataSub)
  })

  //Options for the Radar chart, other than default
  var mycfg = {
    w: w,
    h: h,
    maxValue: 0.6,
    levels: 6,
    ExtraWidthX: 200,
    ExtraWidthY: 100
  }

  //Call function to draw the Radar chart
  //Will expect that data is in %'s
  RadarChart.draw("#" + tag, dataSup, mycfg);
}

function colorPalette(){
  return "#" + Math.random().toString(16).slice(2, 8) // get a list of 10 nice colors
}

// input: data (an array of arrays, an id, the latter of the form [dates, prices], names (an array), title (str))
function drawPlotlyTS(data, id = "timeseries0", names = ["One", "Two"], title = "Downloads"){

  dataArray = []
  range = []
  data.forEach(function(item, i){ // constuct Trace object to feed into Plotly.newPlot
    // get range of item[1]
    // if top of range higher that current top, raise it... same with bottom
    var trace = {
      type: "scatter",
      mode: "lines",
      name: names[i],
      x: item[0],
      y: item[1],
      line: {color: "#" + Math.random().toString(16).slice(2, 8)}
      // line: {color: colorPalette[i]}
    }
    // console.log("names[i]: ",  +names[i])
    dataArray.push(trace)
  })

  var layout = {  // constuct Layout object to feed into Plotly.newPlot
    autosize: true,
    title: title,
    xaxis: {
      autorange: true,
      range: ['2010-02-17', '2017-02-16'],
      rangeselector: {buttons: [
          {
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
          {step: 'all'}
        ]},
      rangeslider: {range: ['2015-02-17', '2017-02-16']}, // Change that to earliest inception dte
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
