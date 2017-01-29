// create a function that given a string reverses the characters
// so ot is to excetera...

function reverse(str){
  i = str.length
  q = 0
  arr = []
  while(i>=0){
    arr[q] = str[i]
    i--
    q++
  }
  console.log(arr.join(''))
}
string = 'test'
reverse(string)
