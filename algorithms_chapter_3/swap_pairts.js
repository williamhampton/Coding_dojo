// create a function that swaps the first and last values, if it is odd do not swap
//the last value, swap the second to last do this without any built in functions

function swap_pairs(arr) {
	for(var i = 0; i < arr.length -1; i += 2) {
		x = arr[i]
		arr[i] = arr[i + 1]
		arr[i + 1] = x
	}
	console.log(arr);
}


array1 = [1,2,3,4,5,6]
array2 = [1,2,3,4,5]
swap_pairs(array1)
swap_pairs(array2)
