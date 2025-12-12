const fs = require("fs");

const data = fs.readFileSync("./input.txt", "utf-8");
const stones = data.split(" ");

const cachedOps = new Map();

const removeLeadingZeros = (string) => {
  return `${Number.parseInt(string)}`;
};

const blink = () => {
  let i = 0;
  const length = stones.length;
  while (i < length) {
    const stone = stones[i];
    if (stone === "0") {
      stones[i] = "1";
    } else {
      const cachedOp = cachedOps.get(stone);
      if (cachedOp !== undefined) {
        stones[i] = cachedOp[0];
        if (cachedOp.length === 2) {
          stones.push(cachedOp[1]);
        }
      } else {
        const len = stone.length;
        if (len % 2 === 0) {
          const part1 = stone.substring(0, len / 2);
          const part2 = removeLeadingZeros(stone.substring(len / 2));
          cachedOps.set(stone, [part1, part2]);
          stones[i] = part1;
          stones.push(part2);
        } else {
          const op = `${Number.parseInt(stone) * 2024}`;
          cachedOps.set(stone, [op]);
          stones[i] = op;
        }
      }
    }

    i += 1;
  }
};

for (let i = 0; i < 40; ++i) {
  blink();
}
console.log(`Number of stones: ${stones.length}`);
