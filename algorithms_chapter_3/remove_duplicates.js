// given an array, remove duplicate values, arr is already in order so
// all doubbles will be grouped together

function remove_duplicates(arr){
  var location = 1
  for (var i = 0; i< arr.length; i++){
    if(arr[i] !== arr[i+1]){
      arr[location] = arr[i+1]
      location++;
    }
  }
  arr.length = location -1;
  console.log(arr)
}
array = [1,2,3,3,4,4,5,5,6]
remove_duplicates(array)
