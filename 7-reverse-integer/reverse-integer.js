/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let str1 = x.toString();
  let arr = str1.split("");
  //   console.log(arr);
  let reverse = arr.reverse();
  //   console.log(ans);
  let str = reverse.join("");
  //   console.log(str);
  let ans = x >= 0 ? parseInt(str) : -parseInt(str);
  if (ans < Math.pow(-2, 31) || ans > Math.pow(2, 31) - 1) {
    return 0;
  } else {
    return ans;
  }
};