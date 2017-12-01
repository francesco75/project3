queue()
   .defer(d3.json, "data")
   .await(makeGraphs);

function makeGraphs(error, data) {

   //Clean projectsJson data

   var dateFormat = d3.time.format("%Y-%m-%d %H:%M:%S");
   data.forEach(function (d) {
       d["date"] = dateFormat.parse(d["date"]);
       d["date"].setDate(1);
       d["price"] = d["price"];
   });


   //Create a Crossfilter instance
   var ndx = crossfilter(data);

   //Define Dimensions
   var dateDim = ndx.dimension(function (d) {
       return d["date"];
   });
   var totalPrice = ndx.dimension(function (d) {
       return d["price"];
   });



   //Calculate metrics
   var numProjectsByDate = totalPrice.group();





   //Define values (to be used in charts)
   var minDate = dateDim.bottom(1)[0]["date"];
   var maxDate = dateDim.top(1)[0]["date"];

   //Charts
   var timeChart = dc.lineChart("#time-chart");







 timeChart
       .width(800)
       .height(200)
       .margins({top: 10, right: 50, bottom: 30, left: 50})
       .dimension(dateDim)
       .group(numProjectsByDate)
       .transitionDuration(500)
       .x(d3.time.scale().domain([minDate, maxDate]))
       .elasticY(true)
       .xAxisLabel("Monthly")
       .yAxis().ticks(4);



   dc.renderAll();
}