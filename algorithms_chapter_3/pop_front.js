//create a function that removes and returns the value at the beginning of the array

function pop_front(arr){
  arr2 = []
  for (var i = 0; i<arr.length - 1; i++){
    arr2[i] = arr[i+1]
  }
  return arr[0]
}
array = [1,2,3,4,5]
console.log(pop_front(array))
