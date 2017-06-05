//create a function that accepts a pointer to the first list node and returns
// number of nodes in the list

function Listnode(value){
  this.value = value;
  this.next = null;
  this.contains = function(val){
    runner = this
    while(runner != null){
      if(runner.value == val){
        return('true')
        return true;
      }
      else{
        runner = runner.next;
      }
    }
  }
  this.length = function(){
    var len = 0;
    runner = this
    while (runner != null){
      len++;
      runner = runner.next
    }
    return(len)
  }
}
var list = new Listnode('value1')
list.next = new Listnode('value2')
list.next.next = new Listnode('value3')

console.log(list.length())
