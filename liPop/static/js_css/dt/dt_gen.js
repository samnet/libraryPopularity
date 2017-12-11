
  var dataSet = [
    [ "plotly.js", "10", "0", ""],
    [ "chart.js", "7", "1", ""],
    [ "morris.js", "7", "0", ""],
    [ "metricsgraphics.js", "4", "1", ""]
  ];




$(document).ready(function() {
  console.log("salut")
    $('#datatable0').DataTable( {
        "paging": false,
        "searching": false,
        "info": false,
        data: dataSet,
        columns: [
            { title: "Name" },
            { title: "Prevalence" },
            { title: "Tendency" },
            { title: "Add to Comp." }
        ],
        columnDefs: [ {
           orderable: false,
           className: 'select-checkbox',
           checkboxes: {
              'selectRow': true
           },
           targets: 3
         } ],
         select: {
             style:    'multi',
             selector: 'td:first-child'
         },
         order: [[ 1, 'asc' ]]
    } );
} );
