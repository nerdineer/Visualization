var data = [4, 8, 15, 20, 30, 42];

var x = 40

var chart = d3.select(".chart");
chart.style("width",720);
chart.style("height",120)

var circle = chart.selectAll("circle");
var circleUpdate = circle.data(data);
var circleEnter = circleUpdate.enter().append('circle');
circleEnter.style("color", "white");
circleEnter.style("fill", "steelblue");
circleEnter.attr("cx",function(d) { return x+=80; });
circleEnter.attr("cy",60);
circleEnter.attr("r",function(d) { return d; });



