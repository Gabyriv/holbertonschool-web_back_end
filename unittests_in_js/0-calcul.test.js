// 0-calcul.test.js
/**
 * Test the calculateNumber function
 * You can assume that a and b are always numbers
 * Test should be around the "rounded" part
 * You have to use assert
 * You should be able to run the thest suite using npm test 0-calcul.test.js
 * Every test should pass without any warning
 */
const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe("calculateNumber", () => {
  it("should return the sum of two numbers", () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it("should return the sum of two numbers", () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it("should return the sum of two numbers", () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it("should return the sum of two numbers", () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
