//insert  a value into an array at a given point without using any built in
//methods

function insert_at(arr,x, loc){
  arr2 = []
  for (var i = 0; i< arr.length; i++){
    if (i == loc){
      arr2[i] = x
      for (var q = loc; q<arr.length; q++){
        arr2[q+1] = arr[q]
      }
      return arr2
    }
    else {
      arr2[i] = arr[i]
    }
  }
  return arr2
}
array = [1,2,3,4,5,6]
console.log(insert_at(array, 10,2))
