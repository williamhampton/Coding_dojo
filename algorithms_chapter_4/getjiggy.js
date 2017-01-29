// create a function that takes a name and removes the first letters
// and adds ' to the '[firstletter]

function jiggy(str){
  arr = str.split('')
  beg = []
  end = arr[0]
  for(var i = 1; i<arr.length; i++){
    beg[i] = arr[i]
  }
  return (beg.join('')+ ' to the '+ end)
}
console.log(jiggy('dylan'))
console.log(jiggy('will'))
