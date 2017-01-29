//create a function that returns every number in an array above zero in order
//from lowest to highest

function skyline(arr){
  arr2 = []
  arr3 = []
  var i = 0
  var q = 0
  while(i<arr.length){
    if (arr[i]>0){
      arr2[q]= arr[i]
      q++
      i++
    }
    else{
      i++
      continue
    }
  }
  //console.log(arr2)
  function addlow(array){
    arr0 = [];
    i = 0
    while(i<array.length){
      s = 0
      t = i + s
      while (t<array.length){
        if (array[i] > array[t]){
          x = array[i]
          array[i] = array[t]
          array[t] = x
          i++
          s++

        }
        else{
          t++
        }

      }
    i++
    }
    console.log(array)
  }
    addlow(arr2)
}
array = [1,23,-1,-70,127,3]
skyline(array)
arrayx = [-1,3,1,-10,4,7,-9]
skyline(arrayx)
