var data = [4, 8, 15, 20, 30, 42];

var x = 250

var chart = d3.select(".chart");
chart.style("width",1000);
chart.style("height",1000);

var circle = chart.selectAll("circle");
var circleUpdate = circle.data(data);
var circleEnter = circleUpdate.enter().append('circle');
circleEnter.style("fill", function(d) { return getRandomColor(); });
circleEnter.style("stroke-width",3);
circleEnter.style("stroke", "black");
circleEnter.attr("cx",function(d) { return x+=80 });
circleEnter.attr("cy",function(d){ return 250; });
circleEnter.attr("r",function(d) { return d; });

x=250
var text = chart.selectAll("text");
var textUpdate = text.data(data);
var textEnter = textUpdate.enter().append('text');
textEnter.style("fill", "white");
textEnter.text( function (d) { return ""+d+""; })
textEnter.attr("x",function(d) { return x+=80; });
textEnter.attr("y",function(d){ return 250; });



function getRandomColor()
{
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}




