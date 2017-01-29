// return an array with the numbers doubbled

function doubble(arr) {
	var newarr = [];
	var i = 0;
	while(i < arr.length) {
		newarr.push(arr[i] * 2);
		i++;
	}
	return newarr;
//  console.log(newarr)
}

var array = [1,2,3,4,5,6,7,8,9]
doubble(array)
