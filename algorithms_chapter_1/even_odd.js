//create function that accepts arr, when three odd values in a row prin "thats odd"
//when three evens in a row "even more so!"
function evenodd(arr){
  for (var i = 0; i<arr.length; i++){
    if(arr[i]%2 != 0){
      if (arr[i+1]%2 != 0){
        if (arr[i+2]%2 != 0){
          console.log("That's Odd!")
        }
      }
    }
    if(arr[i]%2 == 0){
      if (arr[i+1]%2 == 0){
        if (arr[i+2]%2 == 0){
          console.log("Even more so!")
        }
      }
    }
  }
}
var array = [1,1,1,2,2,2];
evenodd(array);
