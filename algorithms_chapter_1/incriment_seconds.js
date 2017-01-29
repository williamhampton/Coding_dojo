// given an arr of numbers add 1 to every second element specificially
// those whose index is odd [1] [3] [5]...

function incriment(arr){
  for (var i =0; i<arr.length; i++){
    if(i%2 !=0){
      arr[i]= arr[i]+1
    }
  }
  console.log(arr);
  return(arr);
}
var array = [1,2,3,4,5,6,7,8,9]
incriment(array);
