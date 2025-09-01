import redis from "redis";

// Create a Redis client (defaults to localhost:6379)
// Using node-redis v2 API to match package.json (redis@^2.8.0)
const client = redis.createClient();

// Log when connected successfully
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

// Log when connection fails
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Set a key with a value, using callback style. redis.print prints "Reply: OK" etc.
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Get a key's value and log it to the console, using callback style
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(value);
  });
}

// Demo calls per requirements
// Expectation if key 'Holberton' exists: prints 'School'
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
