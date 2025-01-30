/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function (gain) {
  let altitude = [0];
  for (let i = 0; i < gain.length; i++) {
    for (let j = i; j < altitude.length; j++) {
      altitude.push(gain[i] + altitude[j]);
      break;
    }
  }
  return Math.max(...altitude);
};