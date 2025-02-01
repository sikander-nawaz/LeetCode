/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function (num, k) {
    let number = BigInt(num.join("")) + BigInt(k);
    return Array.from(String(number), Number);
};
