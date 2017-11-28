
  var dataSet = [
    [ "plotly.js", "10", "0", "check"],
    [ "chart.js", "7", "1", "check"],
    [ "morris.js", "7", "0", "check"],
    [ "metricsgraphics.js", "4", "1", "check"]
  ];

$(document).ready(function() {
  console.log("salut")
    $('#datatable0').DataTable( {
        data: dataSet,
        columns: [
            { title: "Name" },
            { title: "Prevalence" },
            { title: "Tendency" },
            { title: "Add to Comp." }
        ]
    } );
} );
