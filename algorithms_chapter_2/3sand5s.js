// create function that adds values from 100 to 4000000 inclusive if that value
//is divisible by three or five but not both

function threefive(){
  var x = 0
  var i = 100
  while (i<=4000000){
    if (i%5==0 & i%3 == 0){
      i+=1
    }
    if (i%5==0){
      x += i
      i +=1
    }
    if (i%3==0){
      x += i
      i+=1
    }
    else{
      i+=1
    }
  }
  console.log(x)
}
threefive()
