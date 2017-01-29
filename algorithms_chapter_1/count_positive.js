//given an arr of numbers,create a function to replace last value with number of
//positive value and returns it.

function countpos(arr){
  arr[arr.length-1]= Math.abs(Math.random());
  console.log(arr);
  return(arr);
}
var arr = [1,2,3,4,5,6,7,8,9];
countpos(arr);
