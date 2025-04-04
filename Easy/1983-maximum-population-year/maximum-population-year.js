/**
 * @param {number[][]} logs
 * @return {number}
 */
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