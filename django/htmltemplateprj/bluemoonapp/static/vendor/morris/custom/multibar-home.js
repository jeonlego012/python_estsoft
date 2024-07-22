// Displaying X Labels Diagonally (Bar Chart)
var day_data = [
	{"period": "Jan", "Delivered": 1, "Ordered": 2, "Reporeted": 3, "Arrived": 4},
	{"period": "Feb", "Delivered": 5, "Ordered": 4, "Reporeted": 3, "Arrived": 2},
	{"period": "Mar", "Delivered": 7, "Ordered": 8, "Reporeted": 9, "Arrived": 10},
	{"period": "Apr", "Delivered": 12, "Ordered": 11, "Reporeted": 10, "Arrived": 9},
	{"period": "May", "Delivered": 15, "Ordered": 16, "Reporeted": 17, "Arrived": 18},
	{"period": "Jun", "Delivered": 20, "Ordered": 19, "Reporeted": 18, "Arrived": 17},
	{"period": "Jul", "Delivered": 10, "Ordered": 9, "Reporeted": 8, "Arrived": 7},
	{"period": "Aug", "Delivered": 7, "Ordered": 8, "Reporeted": 9, "Arrived": 10},
	{"period": "Sep", "Delivered": 12, "Ordered": 11, "Reporeted": 10, "Arrived": 9},
	{"period": "Oct", "Delivered": 15, "Ordered": 16, "Reporeted": 17, "Arrived": 18},
	{"period": "Nov", "Delivered": 20, "Ordered": 19, "Reporeted": 18, "Arrived": 17},
	{"period": "Dec", "Delivered": 10, "Ordered": 9, "Reporeted": 8, "Arrived": 7},
];
Morris.Bar({
	element: 'xLabelsDiagBar',
	data: day_data,
	xkey: 'period',
	ykeys: ['Delivered', 'Ordered', 'Reporeted', 'Arrived'],
	labels: ['Delivered', 'Ordered', 'Reporeted', 'Arrived' ],
	xLabelAngle: 45,
	gridLineColor: "#e6e6e6",
	resize: true,
	gridTextColor: 'rgba(0, 0, 0, 0.9)',
	gridTextSize: '12',
	hideHover: "auto",
	resize: true,
	barColors:['#1a96e5', '#2498e2', '#36a8f1', '#51bafd'],
});