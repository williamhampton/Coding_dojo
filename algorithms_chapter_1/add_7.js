//build a function that accepts arr. have it return a new arr with
//7 added to all but the first.  do not alter original arr.

function add7(arr){
  newarr = [];
  newarr[0] = arr[0];
  var i = 1;
  while(i < arr.length) {
    newarr.push(arr[i]+7);
    i++;
  }
    console.log(newarr);
    return(newarr);
  }

var array = [1,2,3,4,5,6,7,8,9]

add7(array);
