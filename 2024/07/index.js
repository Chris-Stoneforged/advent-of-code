const fs = require("fs");

const data = fs.readFileSync("./input.txt", "utf-8");
const lines = data.split("\n");

const concat = (a, b) => {
  return Number.parseInt(`${a}${b}`);
};

const evaluate = (iteration, numbers, total, target) => {
  const current = numbers[iteration];
  if (current === undefined) {
    return total === target;
  }

  return (
    evaluate(iteration + 1, numbers, total + current, target) ||
    evaluate(iteration + 1, numbers, total * current, target) ||
    evaluate(iteration + 1, numbers, concat(total, current), target)
  );
};

const sumAll = lines.reduce((prev, curr) => {
  const split = curr.split(": ");
  const total = Number.parseInt(split[0]);
  const numbers = split[1].split(" ").map((n) => Number.parseInt(n));

  return evaluate(1, numbers, numbers[0], total) ? prev + total : prev;
}, 0);

console.log(`Total = ${sumAll}`);
