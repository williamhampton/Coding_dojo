// givend an array, offset the array by given number, so [1,2,3],1 becomes [3,1,2]

function rotate(arr, x){
  arr2 = []
  var i = 0
  var q = arr.length-1-x
  while(q<arr.length){
    arr2[i] = arr[q]
    i++
    q++
  }
  while (i<arr.length){
    arr2[i] = arr[i-x-1]
    i++
  }
  console.log(arr2)
  return arr2
}
array = [1,2,3,4,5]
rotate(array,1)
