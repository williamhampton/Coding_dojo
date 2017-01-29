function fit(arr){
  if(arr[0]> arr.length){
    console.log("Too Big!");
  }
  else if(arr[0]<arr.length){
    console.log("Too Small");
  }
  else{
    console.log("Just right!");
  }
}
var arr1 = [1,2,3];
var arr2 = [8,2];
var arr3 = [3,2,1];

fit(arr1);
fit(arr2);
fit(arr3);
