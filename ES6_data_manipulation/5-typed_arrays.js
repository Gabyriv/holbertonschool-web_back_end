export default function createInt8TypedArray(length, position, value) {
  const myint8 = new Int8Array(length);
  myint8[position] = value;
  const infoDataView = new DataView(myint8.buffer, 0, myint8.byteLength);

  if (position >= length) {
    throw new Error('Position outside range');
  }

  return infoDataView;
}
