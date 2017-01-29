// create a function that tests if a strin
// is a palindrome and returns what is within it
function skip(str){
  str = str.replace(/\s/g, '');
  return(str)
  }

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
  s = []
  r = 0
  var i = 0
  while(i< str.length){
    if (a[i] == str[i]){
      s[r] = str[i]
      r++
      i++
    }
    else{
      i++
    }
  }
  return s.join('')
}
string = ""
console.log(palindrome(string))
