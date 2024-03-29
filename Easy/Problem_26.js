// Given a valid (IPv4) IP address, return a defanged version of that IP address.
// A defanged IP address replaces every period "." with "[.]".

// Example 1:
// Input: address = "1.1.1.1"
// Output: "1[.]1[.]1[.]1"

// SOLUTION:

var defangIPaddr = function (address) {
  return address.split(".").join("[.]");
};

let address = "1.1.1.1";

console.log(defangIPaddr(address));
