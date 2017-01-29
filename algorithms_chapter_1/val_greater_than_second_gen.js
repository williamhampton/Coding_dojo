function greaterThan(arr) {
	if(arr.length > 1) { //can also do arr.length < 2 and return false with no else statement.
		var newArr = [];
		for(var i = 0; i < arr.length; i++) {
			if(arr[i] > arr[1]) {
				newArr.push(arr[i]);
			}
		}
		console.log(newArr.length);
		return newArr;
	} else {
		console.log("This does not work")
	}
}

var arr2 = [0];
var arr3 = [1, 2, 3, 4, 5];
greaterThan(arr2);
greaterThan(arr3);
