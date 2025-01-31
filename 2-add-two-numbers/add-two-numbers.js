/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
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