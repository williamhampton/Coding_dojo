//given array retun array of all the numbers turned negative
function negative(arr){
  newarr = []
  i = 0
  while (i< arr.length){
    newarr[i]= arr[i]-arr[i]-arr[i]
    i+=1
  }
  console.log(newarr)
}
array = [1,2,3,4,5,6,7,8]
negative(array)
