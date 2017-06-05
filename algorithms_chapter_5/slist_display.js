// create display(node) for debugging that returns a string containing all listvalues
// build what you wish console.log(mylist) did

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
  this.display = function(){
    runner = this;
    while(runner != null){
      console.log(runner.value)
      runner = runner.next
    }
  }
}
var list = new Listnode('value1')
list.next = new Listnode('value2')
list.next.next = new Listnode('value3')

list.display()
