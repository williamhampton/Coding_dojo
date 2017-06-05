//return the value at the head of the list, if none return none

function Listnode(value){
  this.value = value;
  this.next = null;
  this.contains = function(val){
    runner = this
    while(runner != null){
      if(runner.value == val){
        console.log('true')
        return true;
      }
      else{
        runner = runner.next;
      }
    }
  }
}

var list = new Listnode('value1')
list.next = new Listnode('value2')
list.next.next = new Listnode('value3')

console.log(list.value)
