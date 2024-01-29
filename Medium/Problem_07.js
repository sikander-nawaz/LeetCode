// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example 1:
// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.

// SOLUTION:

var addTwoNumbers = function (l1, l2) {
  let result = new ListNode(0, undefined);
  let currentNode = result;
  let carriedOverValue = 0;
  do {
    let currentSum = carriedOverValue;

    if (l1) {
      if (l1.val > 0) {
        currentSum += l1.val;
      }
      l1 = l1.next;
    }
    if (l2) {
      if (l2.val > 0) {
        currentSum += l2.val;
      }
      l2 = l2.next;
    }

    if (currentSum >= 10) {
      carriedOverValue = Math.floor(currentSum / 10);
      currentSum -= 10;
    } else {
      carriedOverValue = 0;
    }

    currentNode.val += currentSum;
    if (l1 || l2) {
      currentNode.next = new ListNode(0, undefined);
      currentNode = currentNode.next;
    } else if (carriedOverValue > 0) {
      currentNode.next = new ListNode(carriedOverValue, undefined);
      currentNode = currentNode.next;
    }
  } while (l1 || l2);

  return result;
};

let l1 = [2, 4, 3];
let l2 = [5, 6, 4];
console.log(addTwoNumbers(l1, l2));
