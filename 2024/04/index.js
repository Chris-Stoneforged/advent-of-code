const fs = require("fs");

const data = fs.readFileSync(
  "/Users/chris/Documents/advent-of-code/04/input.txt",
  "utf-8"
);
numColumns = data.indexOf("\n");
const array = data.replaceAll("\n", "").split("");

// Helpers for getting index in a given direction
const getLeft = (index) => (index % numColumns === 0 ? -1 : index - 1);
const getRight = (index) =>
  index % numColumns === numColumns - 1 ? -1 : index + 1;
const getTop = (index) => (index <= numColumns ? -1 : index - numColumns);
const getBottom = (index) =>
  index >= array.length - numColumns ? -1 : index + numColumns;
const getTopLeft = (index) =>
  index <= numColumns || index % numColumns === 0 ? -1 : index - numColumns - 1;
const getBottomLeft = (index) =>
  index >= array.length - numColumns || index % numColumns === 0
    ? -1
    : index + numColumns - 1;
const getTopRight = (index) =>
  index <= numColumns || index % numColumns === numColumns - 1
    ? -1
    : index - numColumns + 1;
const getBottomRight = (index) =>
  index >= array.length - numColumns || index % numColumns === numColumns - 1
    ? -1
    : index + numColumns + 1;

const operations = [
  getLeft,
  getRight,
  getTop,
  getBottom,
  getTopLeft,
  getTopRight,
  getBottomLeft,
  getBottomRight,
];
const sequentialLetters = ["X", "M", "A", "S"];

const checkRecursive = (index, letterIndex, operation) => {
  const newIndex = operation(index);
  if (array[newIndex] === sequentialLetters[letterIndex]) {
    if (letterIndex === sequentialLetters.length - 1) {
      return true;
    }
    return checkRecursive(newIndex, letterIndex + 1, operation);
  }
  return false;
};

const ncluded = [];

const part1 = () => {
  let totalXmasFound = 0;
  for (let i = 0; i < array.length; ++i) {
    if (array[i] === sequentialLetters[0]) {
      for (operation of operations) {
        if (checkRecursive(i, 1, operation)) {
          totalXmasFound += 1;
        }
      }
    }
  }
  return totalXmasFound;
};
console.log(`Total XMAS: ${part1()}`);

const part2 = () => {
  let totalXmasFound = 0;
  for (let i = 0; i < array.length; ++i) {
    if (array[i] === "A") {
      const topLeft = array[getTopLeft(i)];
      const topRight = array[getTopRight(i)];
      const bottomLeft = array[getBottomLeft(i)];
      const bottomRight = array[getBottomRight(i)];

      if (
        ((topLeft === "M" && bottomRight === "S") ||
          (topLeft === "S" && bottomRight === "M")) &&
        ((topRight === "M" && bottomLeft === "S") ||
          (topRight === "S" && bottomLeft === "M"))
      ) {
        totalXmasFound += 1;
      }
    }
  }
  return totalXmasFound;
};

console.log(`Total X-MAS: ${part2()}`);
