queue()

   .defer(d3.json, "/chart-data/")
   .await(makeGraphs);

function makeGraphs(error, data) {
   console.log(data);
   //Clean  data

      data.forEach(function(d) {
      d.feature_name = d.feature_name;
      d.price = +d.price;
  });


   //Create a Crossfilter instance
   var ndx = crossfilter(data);

   //Define Dimensions
   var featureDim = ndx.dimension(function (d) {
       return d["feature_name"];
   });

   var featuredate = ndx.dimension(function (d) {
       return d["date"];
   });


//   //Calculate metrics
        var totalfeature = featureDim.group().reduceSum(function (d) {
       return d["price"];
   });
   var all = ndx.groupAll();
   var total = ndx.groupAll().reduceSum(function (d) {
       return d["price"];
   });

   //Define values (to be used in charts)
   //Charts
    selectField = dc.selectMenu('#menu-select')
       .dimension(featureDim)
       .group(totalfeature);

    var featureTypeChart = dc.rowChart("#feature-row-chart");
    var totalchart = dc.numberDisplay("#total-chart");

   featureTypeChart
       .width(300)
       .height(250)
       .dimension(featureDim)
       .group(totalfeature)
       .xAxis().ticks(4);



   totalchart
       .formatNumber(d3.format("d"))
       .valueAccessor(function (d) {
           return d;
       })
       .group(total)
       .formatNumber(d3.format(".3s"));




   dc.renderAll();


}