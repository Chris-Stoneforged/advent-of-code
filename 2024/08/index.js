const fs = require("fs");

const writeResult = () => {
  let string = "";
  for (let i = 0; i < inputArray.length; ++i) {
    if (i % gridLength === 0) {
      string += "\n";
    }
    string += inputArray[i];
  }
  fs.writeFileSync("./result.txt", string);
};

const data = fs.readFileSync("./input.txt", "utf-8");
const gridLength = data.indexOf("\n");
const inputArray = data.replaceAll("\n", "").split("");
const gridHeight = Math.floor(data.length / gridLength);
const ignoreChar = ".";

const toCoords = (index) => {
  return [Math.floor(index / gridLength), index % gridLength];
};

const fromCoords = (x, y) => {
  return x * gridLength + y;
};

const frequencies = new Map();
for (const element of inputArray) {
  if (element === ignoreChar) {
    continue;
  }

  const array = frequencies.get(element) ?? [];
  array.push(i);
  frequencies.set(element, array);
}

const uniqueLocations = new Set();
frequencies.forEach((value, key) => {
  for (let i = 0; i < value.length; ++i) {
    uniqueLocations.add(value[i]);
    for (let j = 0; j < value.length; ++j) {
      if (j === i) {
        continue;
      }

      const [x1, y1] = toCoords(value[i]);
      const [x2, y2] = toCoords(value[j]);
      const [dx, dy] = [x2 - x1, y2 - y1];
      let [lx, ly] = [x2 + dx, y2 + dy];

      while (lx >= 0 && lx < gridHeight && ly >= 0 && ly < gridLength) {
        const locationIndex = fromCoords(lx, ly);
        uniqueLocations.add(locationIndex);
        lx += dx;
        ly += dy;
      }
    }
  }
});

writeResult();
const numUniqueLocations = uniqueLocations.size;
console.log(`Number of unique antinode locations is ${numUniqueLocations}`);
