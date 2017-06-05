/* create a hash table that has basic functions like add, isempty, findkey,remove*/


function hashmap(capacity){
  this.capacity = capacity;
  this.table = []
  this.add = function(key, val){
    this.table[key] = val;
  }
  this.empty = function(){
    if (this.table = []){
      return true;
    }
    else{
      return false;
    }
  }
  this.findkey = function(key){
    if(this.table[key]){
      return this.table[key];
    }
    else{
      return null;
    }
  }
  this.remove = function(key){
    if(this.findkey(key)){
      delete this.table[key];
    }
  }
}

var a = new hashmap(40);
console.log(a.empty())
a.add('test','testing123')
a.add('color', 'red')
a.add('sky', 'blue')
console.log(a.table)
console.log(a.findkey('test'))
a.remove('sky')
console.log(a.table)
