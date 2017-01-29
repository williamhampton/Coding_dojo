// create a function that returns the longest common suffix
// of the words in an array
function reverse(str){
  i = str.length
  q = 0
  arr = []
  while(i>=0){
    arr[q] = str[i]
    i--
    q++
  }
  return(arr.join(''))
}
function suffix(arr){
  arr = reverse(arr)
  i = 0
  s = 0
  arr1 = []
  while(s<arr.length){
    if (arr[s][i] == arr[arr.length-1][i]){
      arr1[i]= arr[s][i]
      s++
      if (s = arr.length){
        s = 0
        i +=1
      }
    }
    else{
      return('test')

    }
    if (s = arr[s].length-1){
      return(arr1.join(''))
    }
  }
  return(arr1.join(''))
}
array = ['ba','ba','ba','ba']
console.log(suffix(array))
