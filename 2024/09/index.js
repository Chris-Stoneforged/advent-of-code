const fs = require("fs");
const { format } = require("path");

const data = "2333133121414131402"; //fs.readFileSync("./input.txt", "utf-8");

const array = data.split("").map((d) => Number.parseInt(d));
let totalChecksum = 0;
let left = 1;
let index = array[0];
let reverseIndex = array.reduce((prev, curr) => prev + curr) - 1;
console.log(reverseIndex);
let right = array.length % 2 === 0 ? array.length - 2 : array.length - 1;
let filePosition = () => {
  return right / 2;
};
let leftFilePosition = () => {
  return (left + 1) / 2;
};

/// Part 1
// while (left < right) {
//   const l = array[left];
//   const r = array[right];
//   const fp = filePosition();

//   if (l === r) {
//     for (let i = 0; i < l; ++i) {
//       totalChecksum += fp * index;
//       index += 1;
//     }
//     array[left] = 0;
//     array[right] = 0;
//     const lfp = (left + 1) / 2;
//     for (let i = 0; i < array[left + 1]; ++i) {
//       totalChecksum += index * lfp;
//       index += 1;
//     }
//     left += 2;
//     right -= 2;
//   } else if (l < r) {
//     for (let i = 0; i < l; ++i) {
//       totalChecksum += fp * index;
//       index += 1;
//     }
//     array[right] -= l;
//     array[left] = 0;
//     const lfp = (left + 1) / 2;
//     for (let i = 0; i < array[left + 1]; ++i) {
//       totalChecksum += index * lfp;
//       index += 1;
//     }
//     left += 2;
//   } else {
//     for (let i = 0; i < r; ++i) {
//       totalChecksum += fp * index;
//       index += 1;
//     }
//     array[left] -= r;
//     array[right] = 0;
//     right -= 2;
//   }
// }

let string = "";
for (let i = 0; i < array[0]; ++i) {
  string += "0";
}

const getLeftSpace = () => {
  let l = 1;
  while (l < right) {
    if (array[l] >= array[right]) {
      return l;
    }
    l += 2;
  }
  return -1;
};

/// Part 2
while (right >= 0) {
  const r = array[right];
  left = getLeftSpace();
  const l = array[left];
  const fp = filePosition();
  const lfp = leftFilePosition();

  if (l >= 0) {
    for (let i = 0; i < r; ++i) {
      totalChecksum += fp * index;
      index += 1;
      reverseIndex -= 1;
      string += `${fp}`;
    }
    const diff = l - r;
    for (let i = 0; i < diff; ++i) {
      string += ".";
    }
    index += diff;
    array[left] -= r;
    array[right] = 0;
  } else {
    for (let i = 0; i < r; ++i) {
      totalChecksum += fp * reverseIndex;
      reverseIndex -= 1;
    }
    for (let i = 0; i < l; ++i) {
      string += ".";
    }
  }
  reverseIndex -= array[right - 1];
  right -= 2;
}

console.log(`Total checksum = ${totalChecksum}`);
console.log(string);
