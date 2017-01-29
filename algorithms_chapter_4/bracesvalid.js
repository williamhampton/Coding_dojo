// given a series of braces parens, and brackets, determine
// if it is valid

function valid(str){
  x = 0
  y = 0
  z = 0
  for(var i = 0; i<str.length; i++){
    if(str[i] == '('){
      x +=1
    }
    else if(str[i] == ')'){
      x-=1
    }
    if (x< 0){
      return false
    }
    if(str[i] == '{'){
      y++
    }
    else if(str[i] == '}'){
      y--
    }
    if (y< 0){
      return false
    }
    if(str[i] == '['){
      z +=1
    }
    else if(str[i] == ']'){
      z-=1
    }
    if (z< 0){
      return false
    }
  }
  if (x == 0 & y == 0 & z == 0){
    return true
  }
  else{
    return false
  }
}
string1 = "this([{}])istrue" // true
string2 = "[{]()" // false
string3 = '{()}]' // false
string4= '{}[])' // false
console.log(valid(string1))
console.log(valid(string2))
console.log(valid(string3))
console.log(valid(string4))
