// given a string return wether all contained letters are in alphabetical order

function alphabet(str){
  arr = str.split('')
  for (var i = 0; i<arr.length-1; i++){
    x = true
    if(arr[i]<arr[i+1]){
      x = true
    }
    else{
      return false
    }
  }
  if (x == true){
    return true
  }
}

string = 'abcdefghijk'
string1 = 'abcdefghijklmn'
string2 = 'qbcdefghijk'
console.log(alphabet(string))
console.log(alphabet(string1))
console.log(alphabet(string2))
