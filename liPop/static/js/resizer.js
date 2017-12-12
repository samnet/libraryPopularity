// This script handles the responsive sizing of the plotly time series. It was 
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
