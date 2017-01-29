// create a function that removes a value from an array at a given index

function remove_at(arr, x){
  arr2 = []
  for (var i = 0; i<arr.length; i++){
    if (i == x){
      for (var q = x; q<arr.length-1; q++){
        arr2[q] = arr[q+1]
      }
      break
    }
    else {
      arr2[i] = arr[i]
    }
  }
  console.log(arr2)
}
array = [1,3,24,5,6]
remove_at(array, 2)
remove_at(array, 1)
