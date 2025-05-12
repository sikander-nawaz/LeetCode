/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number} m
 * @param {number} n
 * @param {ListNode} head
 * @return {number[][]}
 */
var spiralMatrix = function(m, n, head) {
    const matrix = Array.from({ length: m }, () => Array(n).fill(-1));  
    let current = head;  
    let left = 0, right = n - 1, top = 0, bottom = m - 1;  

    while (left <= right && top <= bottom) {  
        // Traverse from left to right  
        for (let i = left; i <= right; i++) {  
            if (current) {  
                matrix[top][i] = current.val;  
                current = current.next;  
            }  
        }  
        top++;  

        // Traverse from top to bottom  
        for (let i = top; i <= bottom; i++) {  
            if (current) {  
                matrix[i][right] = current.val;  
                current = current.next;  
            }  
        }  
        right--;  

        if (top <= bottom) {  
            // Traverse from right to left  
            for (let i = right; i >= left; i--) {  
                if (current) {  
                    matrix[bottom][i] = current.val;  
                    current = current.next;  
                }  
            }  
            bottom--;  
        }  

        if (left <= right) {  
            // Traverse from bottom to top  
            for (let i = bottom; i >= top; i--) {  
                if (current) {  
                    matrix[i][left] = current.val;  
                    current = current.next;  
                }  
            }  
            left++;  
        }  
    }  

    return matrix; 
};