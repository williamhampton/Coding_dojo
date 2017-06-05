//create an average node to return the average value

function Listnode(value){
  this.value = value;
  this.next = null;
  runner = this;
  this.new = function(val){
    while (runner.next != null){
      runner = runner.next
    }
    runner.next = new Listnode(val)

  }
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
  this.max = function(){
    runner = this;
    var x = runner.value
    while(runner != null){
        if (runner.value > x){
          x = runner.value
          runner = runner.next
        }
        else{
          runner = runner.next
        }
    }
    return(x)
  }
  this.min = function(){
    runner = this;
    var x = runner.value
    while(runner != null){
        if (runner.value < x){
          x = runner.value
          runner = runner.next
        }
        else{
          runner = runner.next
        }
    }
    return(x)
  }
  this.average = function(){
    runner = this
    x = 0
    y = 0
    while (runner != null){
      x += runner.value
      y += 1
      runner = runner.next
    }
    runner = new Listnode(x/y)
    return runner.value
  }
}
var list = new Listnode(1);
list.next = new Listnode(4);
list.next.next = new Listnode(7);
list.next.next.next = new Listnode(111);
list.next.next.next.next = new Listnode(2);
console.log(list.average())

var test = new Listnode(1);
test.new(2)
test.new(3)
test.new(4)
test.display()
