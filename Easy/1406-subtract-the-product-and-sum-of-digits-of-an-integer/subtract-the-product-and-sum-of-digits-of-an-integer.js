/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function (n) {
  let str = n.toString();
  let product = 1;
  let sum = 0;
  for (const i of str) {
    product *= parseInt(i);
    sum += parseInt(i);
  }
  return product - sum;
};
