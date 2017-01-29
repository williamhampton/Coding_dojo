//create a function that tests if a whole number is prime

function isprime(int){
  prime = false
  for (var i = 2; i < int-1; i++){
    if (int%i == 0){
      console.log("Not a prime number")
      break
    }
    else{
      prime = true
    }
  }
  if (prime == true){
    console.log("I am prime")
  }
}
isprime(100)
isprime(10)
isprime(5)
