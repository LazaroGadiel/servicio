am4core.useTheme(am4themes_animated);

var chart = am4core.create("chartdiv", am4charts.XYChart);

chart.data = [{
	"mes": "Enero",
	"recaudacion": 1
}, {
	"mes": "Febrero",
	"recaudacion": 1882
}, {
	"mes": "Marzo",
	"recaudacion": 1809
}, {
	"mes": "Abril",
	"recaudacion": 1322
}, {
	"mes": "Mayo",
	"recaudacion": 1122
}, {
	"mes": "Junio",
	"recaudacion": 1114
}, {
	"mes": "Julio",
	"recaudacion": 984
}, {
	"mes": "Agosto",
	"recaudacion": 711
}, {
	"mes": "Septiembre",
	"recaudacion": 665
}, {
	"mes": "Octubre",
	"recaudacion": 665
},{
	"mes": "Noviembre",
	"recaudacion": 580
}, {
	"mes": "Diciembre",
	"recaudacion": 443
}, 
];

chart.padding(40, 40, 40, 40);

var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.renderer.grid.template.location = 0;
categoryAxis.dataFields.category = "mes";
categoryAxis.renderer.minGridDistance = 60;

var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

var series = chart.series.push(new am4charts.ColumnSeries());
series.dataFields.categoryX = "mes";
series.dataFields.valueY = "recaudacion";
series.tooltipText = "{valueY.value}"
series.columns.template.strokeOpacity = 0;

chart.cursor = new am4charts.XYCursor();

// as by default columns of the same series are of the same color, we add adapter which takes colors from chart.colors color set
series.columns.template.adapter.add("fill", function (fill, target) {
	return chart.colors.getIndex(target.dataItem.index);
});
