export default function singupUser(firstName, lastName) {
  return Promise.resolve({
    firstName,
    lastName,
  });
}
