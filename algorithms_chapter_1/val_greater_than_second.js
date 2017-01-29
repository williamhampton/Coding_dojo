function greaterThanSecond(arr) {
	var x = 0;
	for(var i = 0; i < arr.length; i++) {
		if(arr[i] > arr[1]) {
			console.log(arr[i]);
			x++;
		}
	}
	return x;
}

var array = [1,3,5,7,9,13];
greaterThanSecond(array);
