const reverseList = (head) => {
    // todo
    let currentHead = head //c
    let prev = null //b
    
    while(currentHead) {
      let next = currentHead.next //c
      currentHead.next = prev // a
      
      prev = currentHead
      currentHead = next
    }
    
    return prev
};