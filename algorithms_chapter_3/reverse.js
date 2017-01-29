// reverse the order of values of an array, should have the same length work within the array

function reverse(arr){
  var i = 0;
  q = (arr.length - 1);
  while(i <arr.length/2){
    x = arr[i]
    arr[i] = arr[arr.length-1-i]
    arr[q] = x
    i++
    q--
    //console.log(x)
  }
  console.log(arr)
}
array = [1,2,3,4,5,6]
reverse(array)
