//passed arr containing strings. replace each string with a number- the
//length of the string at previous array index- and return arr.

function prevlen(arr){
    var newarr = [];
  	var i = 0;
  	while(i < arr.length-1) {
  		newarr.push(arr[i+1].length);
  		i++;
  	}
    newarr[newarr.length]= arr[arr.length-1].length
  	return newarr;
    //console.log(newarr);
  }
var array = [ "hello", "howdy", 'yehaw', "country music"];
prevlen(array);
