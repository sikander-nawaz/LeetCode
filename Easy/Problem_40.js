// You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
// The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
// Return the earliest year with the maximum population.

// Example 1:
// Input: logs = [[1993,1999],[2000,2010]]
// Output: 1993
// Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

// SOLUTION:

function maximumPopulation(logs) {
  let yearsCount = Array(2051).fill(0);

  for (let [birth, death] of logs) {
    yearsCount[birth - 1950]++;
    yearsCount[death - 1950]--;
  }

  let maxPopulation = 0;
  let currentPopulation = 0;
  let earliestYear = 0;

  for (let i = 0; i < yearsCount.length; i++) {
    currentPopulation += yearsCount[i];

    if (currentPopulation > maxPopulation) {
      maxPopulation = currentPopulation;
      earliestYear = i + 1950;
    }
  }

  return earliestYear;
}

// Example usage:
let logs = [
  [1993, 1999],
  [2000, 2010],
];

let result = maximumPopulation(logs);
console.log(result);
