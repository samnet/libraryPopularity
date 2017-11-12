$(document).ready(function(){
      var w = 500;
      var h = 500;

      var colorscale = d3.scale.category10();
      console.log("radar_gen 1")

      //Legend titles
      var LegendOptions = ['Smartphone','Tablet'];
      console.log("radar_gen 2")
      //Data
      var d = [
        [
        {axis:"Discussion forums (SO)",value:0.59},
        {axis:"Developer activity (GH)",value:.34},
        {axis:"Web search (Google data)",value:0.42},
        {axis:"Download volumes (ditto)",value:.34},
        {axis:"Documentation quality",value:.84}
        ],[
        {axis:"Discussion forums (SO)",value:0.39},
        {axis:"Developer activity (GH)",value:.32},
        {axis:"Web search (Google data)",value:0.12},
        {axis:"Download volumes (ditto)",value:.38},
        {axis:"Documentation quality",value:.24}
        ]
      ];

      //Options for the Radar chart, other than default
      var mycfg = {
        w: w,
        h: h,
        maxValue: 0.6,
        levels: 6,
        ExtraWidthX: 300
      }

      //Call function to draw the Radar chart
      //Will expect that data is in %'s
      RadarChart.draw("#radarchart0", d, mycfg);

      ////////////////////////////////////////////
      /////////// Initiate legend ////////////////
      ////////////////////////////////////////////

      var svg = d3.select('#body')
        .selectAll('svg')
        .append('svg')
        .attr("width", w+300)
        .attr("height", h)

      //Create the title for the legend
      var text = svg.append("text")
        .attr("class", "title")
        .attr('transform', 'translate(90,0)')
        .attr("x", w - 70)
        .attr("y", 10)
        .attr("font-size", "12px")
        .attr("fill", "#404040")
        .text("What % of owners use a specific service in a week");

      //Initiate Legend
      var legend = svg.append("g")
        .attr("class", "legend")
        .attr("height", 100)
        .attr("width", 200)
        .attr('transform', 'translate(90,20)')
        ;
        //Create colour squares
      legend.selectAll('rect')
        .data(LegendOptions)
        .enter()
        .append("rect")
        .attr("x", w - 65)
        .attr("y", function(d, i){ return i * 20;})
        .attr("width", 10)
        .attr("height", 10)
        .style("fill", function(d, i){ return colorscale(i);})
        ;
      //Create text next to squares
      legend.selectAll('text')
        .data(LegendOptions)
        .enter()
        .append("text")
        .attr("x", w - 52)
        .attr("y", function(d, i){ return i * 20 + 9;})
        .attr("font-size", "11px")
        .attr("fill", "#737373")
        .text(function(d) { return d; })
        ;
      //
      // });
      console.log("Radar_gen: finished.")
});
