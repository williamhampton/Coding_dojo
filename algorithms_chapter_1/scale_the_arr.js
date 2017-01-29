// given an arr and num, multiply all numbers in arr times num and return arr

function multiply(arr,num){
  newarr= []
  for(var i = 0; i<arr.length; i++){
    newarr[i] = arr[i]*num
  }
  return newarr
  //console.log (newarr)
}
array = [1,2,3,4,5,6,7,8]
multiply(array,2)
