function doubble(){
  arr = []
  function rolling(){
    min = Math.ceil(1);
    max = Math.floor(21);
    return Math.floor(Math.random() * (max - min)) + min;
  }
  function array(num){
    for (var i = 0; i < arr.length; i++){
      return arr[i]
    }
  }
  for (var i = 0; i != array(); i++){
    arr.push(rolling())

  }
  total = 0
  for (var i =0; i< arr.length; i++){
    total = total+ arr[i]
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
  console.log(total)
  console.log(arr)
  console.log('High: '+high+" | Low: "+ low)
}
doubble()
