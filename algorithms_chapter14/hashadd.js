/* create a hashtable that accepts a new hashmap of key value pairs and adds them
  to the hashmap */

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
  this.addhash = function(hash){
    for( key in hash.table){
      this.add(key, hash.table[key]);
    }
  }
}

var a = new hashmap(40);
a.add('test','testing123')
a.add('color', 'red')
a.add('sky', 'blue')
var b = new hashmap(60);
b.add('newtest', 'newtesting123')
b.add('b', 'b value')
b.add('c', 'c value')
b.addhash(a)
console.log(b.table)
