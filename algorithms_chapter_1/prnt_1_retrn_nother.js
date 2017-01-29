//print second to last in array, return first odd value

function printreturn(arr){
  for(var i = 0; i<arr.length; i++){
    console.log(arr[arr.length-2]);
    if (arr[i]%2 != 0){
      return(arr[i]);
      break;
    }
  }
}
var array= [1,2,3,4,5,6,7,8,9]
printreturn(array);
