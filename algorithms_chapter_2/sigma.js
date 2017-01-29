// create a function that returns the sum of all positve int of
//a number ex sigma(3) = 6

function sigma(num){
  var x = 0
  var i = 1
  while (i<=num){
    x +=i
    i+=1
  }
  console.log(x)
  //return(x)
}
sigma(10)
sigma(3)
