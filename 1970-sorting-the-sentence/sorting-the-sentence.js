/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function (s) {
  s = s.split(" ");

  let arr = [];
  for (let i = 0; i < s.length; i++) {
    arr.push(s[i].split("").reverse().join(""));
  }

  let sort = arr.sort();
  let ans = [];
  for (let j = 0; j < sort.length; j++) {
    ans.push(sort[j].split("").slice(1).reverse().join(""));
  }

  return ans.join(" ");
};