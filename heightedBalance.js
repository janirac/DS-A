// Given a binary tree, determine if it is height-balanced. 
// A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

// Test Case 1: Balanced binary tree
// const root1 = new TreeNode(1);
// root1.left = new TreeNode(2);
// root1.right = new TreeNode(2);
// root1.left.left = new TreeNode(3);
// root1.left.right = new TreeNode(3);
// root1.right.left = new TreeNode(3);
// root1.right.right = new TreeNode(3);

        root1 = 1 depth = 0
        /   \
    root2= 2  root3 = 2 depth = 1
// console.log(isBalanced(root1));  // Expected output: true

//traverse through the tree using BFS method
//check if the current nodes left and right values are nomore than 1 of the current node
//return true if none of the nodes are more than 1 and return false else wise

const heightBalance = (root1) => {
    let stack = [root1] //[root2, root3]

    while(stack.length > 0) {
        let currentNode = stack.pop //root1
        if(currentNode.val + 1 === currentNode.left.val){
            stack.push(currentNode.left)
        } else {
            return false
        }

        if(currentNode.val + 1 === currentNode.right.val){
            stack.push(currentNode.right)
        } else {
            return false
        }
    }

    return true 
}

