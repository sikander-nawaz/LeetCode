// You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
// Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
// Return true if a and b are alike. Otherwise, return false.

// Example 1:
// Input: s = "book"
// Output: true
// Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

// SOLUTION:

var halvesAreAlike = function (s) {
  let half = s.length / 2;

  let a = s.slice(0, half);
  let b = s.slice(half);

  let countA = 0;
  for (const e of a) {
    if (
      e == "a" ||
      e == "e" ||
      e == "i" ||
      e == "o" ||
      e == "u" ||
      e == "A" ||
      e == "E" ||
      e == "I" ||
      e == "O" ||
      e == "U"
    ) {
      countA++;
    }
  }

  let countB = 0;
  for (const e of b) {
    if (
      e == "a" ||
      e == "e" ||
      e == "i" ||
      e == "o" ||
      e == "u" ||
      e == "A" ||
      e == "E" ||
      e == "I" ||
      e == "O" ||
      e == "U"
    ) {
      countB++;
    }
  }
  return countA === countB;
};

let s = "book";
console.log(halvesAreAlike(s));
