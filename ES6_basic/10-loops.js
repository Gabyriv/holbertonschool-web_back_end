export default function appendToEachArrayValue(array, appendString) {
  const thisArray = [];
  for (const idx of array) {
    thisArray.push(appendString + idx);
  }

  return thisArray;
}
