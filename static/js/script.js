 $(document).ready(function(){
    var data = 0;
//
//   //   // using d3.csv
    d3.csv("/datacsv", function(data){
      console.log("I try")
      console.log(data);
      console.log("cs: " + typeof(data))
    });
    // using ajax
    console.log("ready2go")

    function init(result){
        $("#div1").html(result);
        data = JSON.parse(result);
        console.log("Resultat: " +  data.secret)
        console.log("Type: "+ typeof(data))
        var w = 500;
        var h = 500;

        var colorscale = d3.scale.category10();

        //Legend titles
        var LegendOptions = ['Smartphone','Tablet'];

        //Data
        var d = [
          [
          {axis:"Email",value:0.59},
          {axis:"Social Networks",value:data.secret/1000},
          {axis:"Internet Banking",value:0.42}
          ],[
          {axis:"Email",value:0.48},
          {axis:"Social Networks",value:0.41},
          {axis:"Internet Banking",value:0.27},
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
        RadarChart.draw("#chart", d, mycfg);

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
        console.log("after: " + data)
    }

    $.ajax({ url: '/signUpUser',
      success: init
    })



    console.log("later");
    console.log("data: " + data);


});
