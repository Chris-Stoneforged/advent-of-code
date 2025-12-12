const { time } = require("console");
const fs = require("fs");

function getInput(filePath) {
  const data = fs.readFileSync(filePath).toString("utf-8");
  const pairs = data.split("\n");
  const list1 = [];
  const list2 = [];

  for (const pair of pairs) {
    pairArray = pair.split("   ");
    list1.push(Number.parseInt(pairArray[0]));
    list2.push(Number.parseInt(pairArray[1]));
  }

  return [list1, list2];
}

function run(filePath) {
  const startTime = Date.now();
  const [list1, list2] = getInput(filePath);
  list1.sort((a, b) => a - b);
  list2.sort((a, b) => a - b);

  // Difference score
  let differenceScore = 0;
  const list2Map = new Map([]);
  for (const i in list1) {
    const list2Item = list2[i];
    differenceScore += Math.abs(list1[i] - list2Item);
    const current = list2Map.get() ?? 0;
    list2Map.set(list2Item, current + 1);
  }

  // Similarity score
  const similarityScore = list1.reduce(
    (prev, curr) => prev + (list2Map.get(curr) ?? 0) * curr
  );

  console.log(`Difference score: ${differenceScore}`);
  console.log(`Similarity score: ${similarityScore}`);
  console.log(`Took ${Date.now() - startTime} millis`);
}

run("./input.txt");
