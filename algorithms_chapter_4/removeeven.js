// create a function to remove even length strings form an
//arr ie: it would remove 'to', 'four', but not 'but', 'i'

function removeeven(arr){
  var i = 0
  while (i<arr.length){
    if(arr[i].length%2 == 0){
      arr.splice(i,1);
      continue
    }
    else{
      i++
    }
  }
  console.log(arr)
}
array = ['this', 'is', 'a', 'test', 'for', 'array']
removeeven(array);
