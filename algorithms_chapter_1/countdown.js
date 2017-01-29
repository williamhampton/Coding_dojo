function countdown(num) {
	var arr = [];
	for (var i = num; i >= 0; i--) {
		arr[arr.length] = i;
	}
	console.log(arr.length);
	return arr;
}

var x = countdown(20);
console.log(x);
