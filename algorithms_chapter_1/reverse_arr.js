function newarray(arr){
  newarr = []
  i = 0
  while (i< arr.length){
    newarr.unshift(arr[i]);
    i+=1;
  }
  console.log (newarr)
}
array = [1,2,3,4,5,6]
newarray(array);
