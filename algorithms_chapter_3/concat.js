//replicate javascripts concat function that merges two arrays together

function concat_rep(array1,array2){
  array3 = [];
  var i = 0;
  var q = 0;
  while(i<array1.length){
    array3[i] = array1[i]
    i++
  }
  while(q<array2.length){
    array3[i] = array2[q]
    i++
    q++
  }
  console.log(array3)
}
arraya = [1,2,3,45,6]
arrayb = ["true", "false", 5,3]
concat_rep(arraya,arrayb)
