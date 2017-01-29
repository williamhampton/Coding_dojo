//print low and return high of an array.


function printlow(arr){
  for (var i = 0; i <arr.length; i++){
    var x = arr[0];
    var c = arr[0];
    if (arr[i]< x){
      x = arr[i];
    }
    if (arr[i]>c){
      c = arr[i];
    }
  }
  console.log(x);
///  console.log(c)
  return(c);
}
arr= [1,2,3,5,7];
printlow(arr);
