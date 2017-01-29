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
function palindrome(str){
  a = reverse(str)
  if(a == str){
    return true
  }
  else{
    return false
  }
}
console.log(palindrome('ada'))
console.log(palindrome('notatpalidrome'))
console.log(palindrome('dad'))
