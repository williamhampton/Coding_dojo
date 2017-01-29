//create function that prints yummy each time one value = food
// if no array elements = food print I'm Hungry

function hungry(arr){
  yummy = []
  for (var i = 0; i< arr.length; i++){
    if (arr[i]=="food"){
      yummy.push("yummy")
    }
  }
  if (yummy.length == 0){
    console.log("I'm Hungry")
  }
  else {
  console.log(yummy)
  }
}
array1 = ["food","food","not food","metal"]
array2 = ["heavy", "metal", "thunder"]
hungry(array1)
hungry(array2)
