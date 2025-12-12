const fs = require("fs");

const data = fs.readFileSync(
  "/Users/chris/Documents/advent-of-code/12/input.txt",
  "utf-8"
);
const mapArray = data.replaceAll("\n", "").split("");
const mapWidth = data.indexOf("\n");

const getAdjacent = (index) => {
  const adjacent = [];
  if (index % mapWidth > 0) {
    adjacent.push(index - 1);
  }
  if (index % mapWidth < mapWidth - 1) {
    adjacent.push(index + 1);
  }
  if (index >= mapWidth) {
    adjacent.push(index - mapWidth);
  }
  if (index < mapArray.length - mapWidth) {
    adjacent.push(index + mapWidth);
  }
  return adjacent;
};

class Group {
  constructor(character) {
    this.perimeter = 0;
    this.indices = [];
    this.character = character;
  }

  hasIndex = (index) => {
    return this.indices.indexOf(index) >= 0;
  };

  add = (index, adjacent) => {
    this.indices.push(index);
    this.perimeter +=
      4 - 2 * adjacent.filter((a) => this.indices.indexOf(a) >= 0).length;
  };

  cost = () => {
    return this.perimeter * this.indices.length;
  };
}

const traverseAdjacent = (index, character, group) => {
  const adjacent = getAdjacent(index).filter((a) => mapArray[a] === character);
  group.add(index, adjacent);
  for (const i of adjacent) {
    if (group.hasIndex(i)) {
      continue;
    }
    traverseAdjacent(i, character, group);
  }
};

const groups = [];
while (true) {
  const index = mapArray.findIndex(
    (a, i) => !groups.some((g) => g.hasIndex(i))
  );

  if (index < 0) {
    break;
  }

  const character = mapArray[index];
  const group = new Group(character);
  traverseAdjacent(index, character, group);
  groups.push(group);
}

const totalCost = groups.reduce((prev, curr) => {
  return prev + curr.cost();
}, 0);

console.log(`Total cost = ${totalCost}`);
