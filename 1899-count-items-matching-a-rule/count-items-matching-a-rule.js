/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function (items, ruleKey, ruleValue) {
  let count = 0;

  let indexOfItems = ruleKey == "type" ? 0 : ruleKey == "color" ? 1 : 2;

  for (const key of items) {
    if (key[indexOfItems] == ruleValue) {
      count++;
    }
  }

  return count;
};