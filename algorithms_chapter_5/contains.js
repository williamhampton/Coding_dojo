// Given a pointer to a listnode and a value return whether
// value is found in any node in the list

function contains(val){
  runner = this.value
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
function removefront(runner){
  runner.value = runner.next.value;
  runner.next = runner.next.next

  console.log(runner)
}
list.contains('value2')
