// Question: Reverse a Linked List
// Given the head of a singly linked list, write a function to reverse the list. Return the new head of the reversed list.
// Hint 1: You can solve this problem by iterating through the linked list once.
// Hint 2: You should keep track of the previous node, the current node, and the next node in the list while iterating.
// Hint 3: The new head of the reversed list will be the node at which you started iteration.

// null <= 1  2 => 3 => 4 => 5 head = 1
// 1 <= 2 <= 3 <= 4 <= 5 head = 5

// The linked list is: 1 -> 2 -> 3 -> 4 -> 5 -> null
// let head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));

// let reversed = reverseList(head);

// After reversing the list: 5 -> 4 -> 3 -> 2 -> 1 -> null
// console.log(reversed.val); // Output: 5
// console.log(reversed.next.val); // Output: 4
// console.log(reversed.next.next.val); // Output: 3
// console.log(reversed.next.next.next.val); // Output: 2
// console.log(reversed.next.next.next.next.val); // Output: 1
// console.log(reversed.next.next.next.next.next); // Output: null

// iterate over the linked list
// point the current node to the previous node without losing access to the next node
// return the new head

const reverseList = (head) => {
    
    while(currentNode.next){
        let currentNode = head //1
        let next = currentNode.next //2
        let previous = null //null

        currentNode.next = previous //null
        previous = currentNode
        currentNode = next //2
    }

    return previous
}

//Solution

// const reverseList = (head) => {
//     let currentNode = head;
//     let previousNode = null;
//     let nextNode = null;

//     while(currentNode){
//         nextNode = currentNode.next;  // Save the next node
//         currentNode.next = previousNode; // Reverse the link
//         previousNode = currentNode; // Update the previous node
//         currentNode = nextNode; // Move to the next node
//     }

//     return previousNode;
// }