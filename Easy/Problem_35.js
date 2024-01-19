// You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
// Given the string command, return the Goal Parser's interpretation of command.

// Example 1:
// Input: command = "G()(al)"
// Output: "Goal"
// Explanation: The Goal Parser interprets the command as follows:
// G -> G
// () -> o
// (al) -> al
// The final concatenated result is "Goal".

// SOLUTION:

function interpret(command) {
  let ans = "";

  let i = 0;
  while (i < command.length) {
    if (command[i] === "G") {
      ans += "G";
      i++;
    } else if (command[i] === "(" && command[i + 1] === ")") {
      ans += "o";
      i += 2;
    } else if (
      command[i] === "(" &&
      command[i + 1] === "a" &&
      command[i + 2] === "l" &&
      command[i + 3] === ")"
    ) {
      ans += "al";
      i += 4;
    } else {
      i++;
    }
  }

  return ans;
}

// Example usage:
let command = "G()(al)";
console.log(interpret(command));
