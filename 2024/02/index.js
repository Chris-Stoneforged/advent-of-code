const fs = require("fs");

function isReportSafe(levels) {
  const ascending = levels[0] < levels[1];

  for (const i in levels) {
    const difference = levels[i] - levels[i - 1];
    if (
      (ascending && (difference < 1 || difference > 3)) ||
      (!ascending && (difference > -1 || difference < -3))
    ) {
      return false;
    }
  }

  return true;
}

function main(filePath) {
  const data = fs.readFileSync(filePath, "utf-8");
  const lines = data.split("\n");
  let numSafeLevels = 0;

  for (const line of lines) {
    const levels = line.split(" ").map((l) => Number.parseInt(l));
    if (
      isReportSafe(levels) ||
      // --- Part 2
      levels.some((val, index, array) => {
        const copy = [...array];
        copy.splice(index, 1);
        return isReportSafe(copy);
      })
      // --- End Part 2
    ) {
      numSafeLevels += 1;
    }
  }

  console.log(`Number of safe levels: ${numSafeLevels}`);
}

main("./input.txt");
