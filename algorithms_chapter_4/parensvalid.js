// create a function that given an input str returns a boolean
// wether the parentheses in str are valid

function parens(str){
  x = 0
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
  }
  if (x == 0){
    return true
  }
  else{
    return false
  }
}
string1 = '()()' //true
string2 = ')())' //false
string3 = '())' //false
console.log(parens(string1))
console.log(parens(string2))
console.log(parens(string3))
