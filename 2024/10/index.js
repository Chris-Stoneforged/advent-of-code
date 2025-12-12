const fs = require("fs");

const data = fs.readFileSync(
  "/Users/chris/Documents/advent-of-code/10/input.txt",
  "utf-8"
);
const mapArray = data
  .replaceAll("\n", "")
  .split("")
  .map((e) => Number.parseInt(e));
const mapWidth = data.indexOf("\n");
const targetHeight = 9;
const startingHeight = 0;

const getAdjacent = (index) => {
  const adjacent = [];
  // Left
  if (index % mapWidth > 0) {
    adjacent.push(index - 1);
  }
  // Right
  if (index % mapWidth < mapWidth - 1) {
    adjacent.push(index + 1);
  }
  // Up
  if (index >= mapWidth) {
    adjacent.push(index - mapWidth);
  }
  // Down
  if (index < mapArray.length - mapWidth) {
    adjacent.push(index + mapWidth);
  }
  return adjacent;
};

const traverseTrail = (currentHeight, index, ends) => {
  if (mapArray[index] === targetHeight) {
    ends.push(index);
    return;
  }

  const adjacent = getAdjacent(index);
  for (i of adjacent) {
    if (mapArray[i] == currentHeight) {
      traverseTrail(currentHeight + 1, i, ends);
    }
  }
};

const totalScore = mapArray.reduce((prev, curr, index) => {
  if (curr === startingHeight) {
    const trailEnds = [];
    traverseTrail(startingHeight + 1, index, trailEnds);
    return prev + trailEnds.length;
  }
  return prev;
}, 0);

console.log(`Total score = ${totalScore}`);
