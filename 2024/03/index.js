const fs = require("fs");

function main(filePath) {
  const data = fs.readFileSync(filePath, "utf-8");
  const matches = data.match(/(mul\((\d{1,3}),\d{1,3}\)|don't|do)/g);
  let enabled = true;
  total = matches.reduce((prev, curr) => {
    if (curr === "don't") {
      enabled = false;
    } else if (curr === "do") {
      enabled = true;
    } else if (enabled) {
      const subMatches = curr.match(/\d{1,3}/g);
      const num1 = Number.parseInt(subMatches[0]);
      const num2 = Number.parseInt(subMatches[1]);
      return prev + num1 * num2;
    }
    return prev;
  }, 0);
  console.log(total);
}

main("./input.txt");
