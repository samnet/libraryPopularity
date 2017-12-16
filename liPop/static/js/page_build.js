popularRlibs =  ["viridisLite","devtools","readr","dplyr","readxl","shiny","R6","tidyr",
"boot","Rcpp","data.table","tibble","mgcv","psych","xlsx","tidyverse","lubridate",
"stingr","colorspace","backports","XML"]

var shuffled = popularRlibs.sort(function(){return .5 - Math.random()});
var preSelection=shuffled.slice(0,1); // For some reason I don't manage to have pre selection > 1

$(document).ready(function(){

  // Populate the library (first) selection input
  optgroup0 = document.createElement("optgroup")
  optgroup0.id = "optgrp0"
  optgroup0.label = "R"
  document.getElementById('input0').appendChild(optgroup0); // append optgrp
  packList.forEach(function(item, i){
    lib = document.createElement("option")
    lib.value = item
    lib.innerHTML = item
    document.getElementById('optgrp0').appendChild(lib); // append individual tags
  })

  // Populate the task selection (second) input
  input1 = document.getElementById('input1')
  topology.forEach(function(item, i){
    console.log(item.name)
    newcluster = document.createElement("optgroup")
    newcluster.id = item.name
    newcluster.label = item.name
    input1.appendChild(newcluster)
    item.constituents.forEach(function(component, j){
      newtask = document.createElement("option")
      newtask.value = component.name
      newtask.innerHTML = component.name
      document.getElementById(item.name).appendChild(newtask);
    })
  })

  // Pre-select (restrict to well known library pairs)
  document.getElementById('input0').value = preSelection;

  // Update page content based on selection
  $("#input0").change(function(){
      currentSelection = $("#input0").val()
      if (currentSelection.length > 0) { // do nothing if change is deletion of unique selected tag
         $.ajax({
           url : '/sendMeDatJS',
           type : 'GET',
           dataType : 'json',
           data: "currentSelection="+ currentSelection, // annoying detail: if you put spaces around the equal sign it sends nuts!
           success : function(response, status) { pageGenerator(response, "#input0")},
           error : function(resultat, statut, erreur){
             console.log('/sendMeDatJS ajax call failed')
           },
           complete : function(resultat, statut){
             console.log('/sendMeDatJS ajax call completed')
           }
        });
      }
  })
  // trigger a change so the page gets populated upon launching (ow. no change)
  $("#input0").change()
})

function pageGenerator(response, inputID){

  // retrieve the libraries currently under study
  currentSelection = $(inputID).val()

  // each elements of the supSets correspond to one library
  supSetTS = []   // for the time series
  supSetRadar = []   // for the radar

  referenceRadar = [7000,2000,1,6000000,1] // HOW TO CALIBRATE IT?

  // for each of the libraries under consideration
  currentSelection.forEach(function(tag, i){
    // isolate the data received from the server
    var data = response[tag]
    // build the data used for the time series
    var dates = unpack(data.cran.downloads, 'day')
    var dailyDwld = unpack(data.cran.downloads, 'downloads')
    supSetTS.push([dates, dailyDwld])
    // build the data used for the radar
    var githubDat = data.github.length > 0 ? data.github[1] : 0; // case where no match on gihub
    var totalCranDwld = arraySum(dailyDwld)
    subSet = [data.soflw, githubDat, data.googleTrend, totalCranDwld, data.doc]
    // rounding and normalizing radar data wrt referenceRadar
    var subSet = subSet.map(function(n, j) { return Math.round(1000*n / referenceRadar[j])/1000; });
    supSetRadar.push(subSet)
  })

  // draw
  drawPlotlyTS(supSetTS, id = "timeseries0", names = currentSelection)
  radarConstructor("radarchart0", arrayOfDataArrays = supSetRadar)
}

// des missing
function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

// cumulative sum of the entries of an array
function arraySum(anArray){
  var count=0;
  for (var i=anArray.length; i--;) { // apparently faster so
    count+=anArray[i];
  }
  return(count)
}
