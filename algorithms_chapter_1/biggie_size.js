function big(arr){
  for (var i =0; i < arr.length; i++){
    if (arr[i]>0){
      arr[i] = "big";
      console.log(arr[i]);
    }
    else{
      console.log(arr[i]);
    }
  }
}
var arr1 = [0,1,-2,-34]
var arr2 = [1,-2,-4,5,2]
big(arr1);
big(arr2);
