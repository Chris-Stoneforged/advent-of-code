const fs = require("fs");

const toCoords = (index) => {
  return [Math.floor(index / gridWidth), index % gridWidth];
};

const fromCoords = (x, y) => {
  return x * gridWidth + y;
};

const incrementDirectionIndex = (index) => {
  return index + 1 === directionVectors.length ? 0 : index + 1;
};

const writeResult = () => {
  let resultString = "";
  for (let i = 0; i < gridArray.length; ++i) {
    if (i % gridWidth === 0 && i > 0) {
      resultString += "\n";
    }
    resultString += gridArray[i];
  }
  fs.appendFileSync("./result.txt", `\n\n${resultString}`);
};

fs.writeFileSync("./result.txt", "");
const data = fs.readFileSync("./input.txt", "utf-8");
let gridArray = data.replaceAll("\n", "").split("");
const gridWidth = data.indexOf("\n");
const gridHeight = Math.floor(data.length / gridWidth);
const objChar = "#";
const visitedChar = "X";
const paradoxChar = "0";
const directionVectors = [
  [-1, 0], // Up
  [0, 1], // Right
  [1, 0], // Down
  [0, -1], // Left
];

let paradoxLocations = 0;
let totalMoves = 0;
let directionIndex = 0;
let [x, y] = toCoords(gridArray.indexOf("^"));

while (x >= 0 && x < gridHeight && y >= 0 && y < gridWidth) {
  const [dx, dy] = directionVectors[directionIndex];
  const nextX = x + dx;
  const nextY = y + dy;
  const newIndex = fromCoords(nextX, nextY);

  switch (gridArray[newIndex]) {
    case objChar:
      directionIndex = incrementDirectionIndex(directionIndex);
      continue;
    case visitedChar:
      break;
    default:
      totalMoves += 1;
      gridArray[newIndex] = visitedChar;
      break;
  }

  x = nextX;
  y = nextY;
}

console.log(
  `Total Moves = ${totalMoves}, Paradox locations = ${paradoxLocations}`
);
