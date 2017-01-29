//create fun that returns the sum all int from 0 to num except :
//if current count is evenly divisible by 3 skip
// if current count is evenly divisible by 7 add it twice
// if current count is 1/3 num return -1 instead

function messymath(num){
  var count = 0
  var i = 0
  while (count < num){
    if (count%3==0){
      count +=1
    }
    if (count%7 == 0){
      i = i + count + count
      count +=1
    }
    if (count== num/3){
      i = -1
      break
    }
    else{
      i = i+count
      count +=1
    }
  }
  console.log(i)
}
messymath(8)
messymath(4)
messymath(15)
