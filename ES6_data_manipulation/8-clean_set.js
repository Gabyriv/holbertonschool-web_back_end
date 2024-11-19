export default function cleanSet(set, startString) {
  if (!set || !startString || !(set instanceof Set) || typeof startString !== 'string' || startString === '') {
    return '';
  }

  const filteredArray = Array.from(set)
    .filter((item) => typeof item === 'string' && item.startsWith(startString))
    .map((item) => item.slice(startString.length));

  return filteredArray.join('-');
}
