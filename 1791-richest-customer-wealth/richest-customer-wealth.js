/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function (accounts) {
  let maximum = [];
  for (let index = 0; index < accounts.length; index++) {
    let plus = accounts[index].reduce((a, b) => a + b);
    maximum.push(plus);
  }
  return Math.max(...maximum);
};