// given an array of strings remove any strings
//shorter than a certin length (str, num)
function short(arr,num){
  var i= 0
  while ( i<arr.length){
    if(arr[i].length<num){
      arr.splice(i,1);
      continue
    }
    else{
      i++
    }
  }
  console.log(arr)
}
array = ['this', 'is', 'a', 'test', 'A', 'a']
short(array,2)
