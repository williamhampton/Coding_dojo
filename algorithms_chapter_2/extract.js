// given a function with 2 parameters, both numbers, that the second one
//returns the mumear value of that digit

function extractDigit(num,digitNum){
  numstring = num.toString();
  console.log(numstring.substring(digitNum,digitNum+1))
}
extractDigit(123241,2)
extractDigit(231452314,4)
