
function rollone(){
  min = Math.ceil(1);
  max = Math.floor(7);
  return Math.floor(Math.random() * (max - min)) + min;
}


function playfives(num){
  for( var i =0; i<num; i++){
    x = rollone();
    if (x == 5){
      console.log( x + ' thats good luck!!' )
    }
    else{
      console.log(x)
    }
  }
}
playfives(3)

function playstatistics(){
  arr = []
  for (var i = 0; i< 8; i++){
    arr.push(rollone())
  }
  high = 0
  low = 7
  for (var i = 0; i < arr.length; i++){
    if (arr[i]> high){
      high = arr[i]
    }
    if (arr[i]< low){
      low = arr[i]
    }
  }
  console.log("High: "+ high+ " | Low: "+low)
}
playstatistics()

function playstatistics2(){
  arr = []
  for (var i = 0; i< 8; i++){
    arr.push(rollone())
  }
  high = 0
  low = 7
  for (var i = 0; i < arr.length; i++){
    if (arr[i]> high){
      high = arr[i]
    }
    if (arr[i]< low){
      low = arr[i]
    }
  }
  console.log("High: "+ high+ " | Low: "+low)
  total = 0
  for(var i = 0; i< arr.length; i++){
      total = total + arr[i]
  }
  console.log( "Total: "+ total)
}
playstatistics2()

function playstatistics3(x){
  arr = []
  for (var i = 0; i< x; i++){
    arr.push(rollone())
  }
  high = 0
  low = 7
  for (var i = 0; i < arr.length; i++){
    if (arr[i]> high){
      high = arr[i]
    }
    if (arr[i]< low){
      low = arr[i]
    }
  }
  console.log("High: "+ high+ " | Low: "+low)
  total = 0
  for(var i = 0; i< arr.length; i++){
      total = total + arr[i]
  }
  console.log( "Total: "+ total)
}
playstatistics3(10)

function playstatistics4(x){
  arr = []
  for (var i = 0; i< x; i++){
    arr.push(rollone())
  }
  high = 0
  low = 7
  for (var i = 0; i < arr.length; i++){
    if (arr[i]> high){
      high = arr[i]
    }
    if (arr[i]< low){
      low = arr[i]
    }
  }
  console.log("High: "+ high+ " | Low: "+low)
  total = 0
  for(var i = 0; i< arr.length; i++){
      total = total + arr[i]
  }
  q = total/x
  console.log( "Average: "+ q)
}
playstatistics4(12)
