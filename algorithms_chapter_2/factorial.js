//return a function that factorial(num) = all positive int * eachother

function factorial(num){
  var x = 1
  var i = 1
  while (i<=num){
    x = x *i
    i+=1
  }
  console.log(x)
  return(x)
}
factorial(3)
factorial(4)
