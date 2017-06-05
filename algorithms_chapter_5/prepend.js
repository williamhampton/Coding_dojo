// create a function that inserts a value, at a given point
// if that point does not exist then add it at the end


function Listnode(value){
  this.value = value;
  this.next = null;
  this.new = function(val){
    runner = this;
    while (runner.next != null){
      runner = runner.next
    }
    runner.next = new Listnode(val)
    runner = this;
  }
  this.removefront = function(){
    runner = this.next
    var newlist = new Listnode(runner)
    while (runner != null){
      runner = runner.next
      newlist.new(runner)
    }
    return(newlist)
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
    return false
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
  this.back = function(){
    runner = this;
    while (runner.next != null){
      runner = runner.next
    }
    return runner.value
  }
  this.minfront = function(){
    runner = this
    runner2 = this
    var x = runner.value
    while (runner != null){
      if (runner.value<x){
        x = runner.value
        runner = runner.next
      }
      else {
        runner = runner.next
      }
    }
    var newlist = new Listnode(x)
    while(runner2 != null){
      if (runner2.value == x){
        runner2 = runner2.next
      }
      else{
        newlist.new(runner2.value)
        runner2 = runner2.next
      }
    }
    newlist.display()

    return newlist
  }
  this.maxback = function(){
    runner = this
    runner2 = this
    var x = runner.value
    while (runner != null){
      if (runner.value>x){
        x = runner.value
        runner = runner.next
      }
      else {
        runner = runner.next
      }
    }
    var newlist = new Listnode()
    runner3 = this
    if (runner3.value == x){
      runner3 = runner3.next
      var newlist = new Listnode(runner3.value)
    }
    else{
      var newlist = new Listnode(runner3.value)
      }

    while(runner2 != null){
      if (runner2.value == x){
        runner2 = runner2.next
      }
      if(runner2.value == runner3.value){
        runner2 = runner2.next
      }
      else{
        newlist.new(runner2.value)
        runner2 = runner2.next
      }
    }
    newlist.new(x)
    newlist.display()
    return(newlist)
  }
}
  function prep(runner,val,before){
    if(runner.contains(before) == false){
      runner.new(val)
      runner.display()
      return runner
    }
      if(runner.value != before){
        var listoflists = new Listnode(runner.value)
        runner = runner.next
        while(runner.value != before){
          listoflists.new(runner.value)
          runner = runner.next
        }
        listoflists.new(val)
        while(runner != null){
          listoflists.new(runner.value)
          runner = runner.next
        }
        listoflists.display()
        return (listoflists)
      }
      if(runner.value == before){
        var listoflists = new Listnode(val)
        while(runner != null){
          listoflists.new(runner.value)
          runner = runner.next
        }
        listoflists.display()
        return (listoflists)
      }
      else{
        console.log('this is odd')
        return(false)
      }
    }

var list = new Listnode(1);
list.next = new Listnode(4);
list.next.next = new Listnode(7);
list.next.next.next = new Listnode(111);
list.next.next.next.next = new Listnode(2);

var list2 = new Listnode(7);
list2.new(2)
list2.new(3)
list2.new(4)

//prep(list2,7000000, 100)
//prep(list2,9000000,7)
prep(list,8000000,7)
list.display()
