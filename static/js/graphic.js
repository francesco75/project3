queue()

   .defer(d3.json, "/chart-vote/")
   .await(makeGraphs);

function makeGraphs(error, databug) {
   console.log(databug);
   //Clean  data


   //Create a Crossfilter instance
   var ndx = crossfilter(databug);


   //Define Dimensions
   var typeDim = ndx.dimension(function (d) {
       return d["ticket_type"];
   });
   var typeName = ndx.dimension(function (d) {
       return d["ticket_name"];
   });

   var typeDate = ndx.dimension(function (d) {
       return d["ticket_date"];
   });




   //Calculate metrics
   var totalType = typeDim.group().reduceSum(function (d) {
       return d["ticket_type"];
   });
   var totalName = typeName.group().reduceSum(function (d) {
       return d["ticket"];
   });

    var totalDate = typeDate.group().reduceSum(function (d) {
       return d["ticket"];
   });



   //Define values (to be used in charts)
   //Charts
   selectField = dc.selectMenu('#menu-vote')
       .dimension(typeDate)
       .group(totalDate);

    var bugTypeChart = dc.pieChart("#bug-pie-chart");
    var bugfeatureChart = dc.rowChart("#bug-feature-chart");
    var timerowChart = dc.rowChart("#time-row-chart");

   bugTypeChart
       .height(220)
       .radius(90)
       .innerRadius(40)
       .transitionDuration(1500)
       .dimension(typeDim)
       .group(typeDim.group());



   bugfeatureChart
       .width(300)
       .height(250)
       .dimension(typeName)
       .group(totalName)
       .xAxis().ticks(4);

   timerowChart
      .width(300)
      .height(250)
      .dimension(typeDate)
      .group(totalDate)
      .xAxis().ticks(4);



      dc.renderAll();


}