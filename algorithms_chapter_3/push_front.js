//create a function that inserts at the beginning of an arr, do this without
// built in functions

function push_front(arr, x){
  arr2 = []
  arr2[0] = x
  for (i = 0; i<arr.length; i++){
    arr2[i+1] = arr[i]
  }
  console.log(arr2)
}
array = [1,2,3,4,5,6,7]
push_front(array, 2)
