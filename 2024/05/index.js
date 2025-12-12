const fs = require("fs");

const rulePairs = [];
const updates = [];

const data = fs.readFileSync("./input.txt", "utf-8");
const lines = data.split("\n");

for (const line of lines) {
  if (line.includes("|")) {
    rulePairs.push(line.split("|").map((s) => Number.parseInt(s)));
  } else if (line.includes(",")) {
    updates.push(line.split(",").map((s) => Number.parseInt(s)));
  }
}

// Part 1
const isRulePairMet = (update, rulePair) => {
  if (!update.includes(rulePair[0]) || !update.includes(rulePair[1])) {
    // both members of pair have to be included
    return true;
  }

  if (update.lastIndexOf(rulePair[1]) < update.indexOf(rulePair[0])) {
    return false;
  }

  return true;
};

const totalCorrect = updates.reduce((prev, curr) => {
  if (rulePairs.every((pair) => isRulePairMet(curr, pair))) {
    const middleNumber = curr[Math.floor(curr.length / 2)];
    return prev + middleNumber;
  }
  return prev;
}, 0);

console.log(`Total of middle numbers of correct updates is ${totalCorrect}`);

// Part 2
const orderUpdate = (update) => {
  update.sort((a, b) => {
    if (rulePairs.some((rp) => rp[0] === a && rp[1] === b)) {
      return -1;
    }
    if (rulePairs.some((rp) => rp[0] === b && rp[1] === a)) {
      return 1;
    }
    return 0;
  });

  if (rulePairs.every((pair) => isRulePairMet(update, pair))) {
    console.log("Ordering worked");
  } else {
    console.log("Ordering failed");
  }

  return update;
};

const totalIncorrect = updates.reduce((prev, curr) => {
  if (rulePairs.every((pair) => isRulePairMet(curr, pair))) {
    return prev;
  }

  // Order pair and add the middle number
  const orderedUpdate = orderUpdate(curr);
  const middleNumber = orderedUpdate[Math.floor(orderedUpdate.length / 2)];
  return prev + middleNumber;
}, 0);

console.log(
  `Total of middle numbers of incorrect updates is ${totalIncorrect}`
);
