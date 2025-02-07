import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([uploadPhoto, createUser]) => {
      console.log(`${uploadPhoto.body} ${createUser.firstName} ${createUser.lastName}`);
    }).catch(() => {
      console.log('Signup system offline');
    });
}
