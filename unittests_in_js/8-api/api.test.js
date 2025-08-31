// 8-api/api.test.js
// Integration tests for the index route using request and spawning the server

const { expect } = require("chai");
const request = require("request");
const { spawn } = require("child_process");

describe("Index page", function () {
  let server;
  let timer;
  let finished = false;

  before(function (done) {
    // Give the server a bit of time to boot
    this.timeout(7000);

    server = spawn("node", ["api.js"], {
      stdio: ["ignore", "pipe", "pipe"],
    });

    function onReady(data) {
      const msg = data.toString();
      if (msg.includes("API available on localhost port 7865")) {
        safeDone();
      }
    }

    function onErrorData(data) {
      const msg = data.toString();
      if (msg.includes("EADDRINUSE")) {
        safeDone(
          new Error(
            "Port 7865 already in use. Stop the running server and retry."
          )
        );
      }
    }

    function onExitEarly(code) {
      if (!finished) {
        safeDone(new Error(`Server exited early with code ${code}`));
      }
    }

    function safeDone(err) {
      if (finished) return;
      finished = true;
      clearTimeout(timer);
      // Detach listeners to avoid leaks and duplicate done calls
      server.stdout.off("data", onReady);
      server.stderr.off("data", onErrorData);
      server.off("exit", onExitEarly);
      done(err);
    }

    server.stdout.on("data", onReady);
    server.stderr.on("data", onErrorData);
    server.on("exit", onExitEarly);
    server.on("error", (err) => {
      safeDone(err);
    });

    // Fallback if the log message isn't seen
    timer = setTimeout(() => {
      safeDone(new Error("Server did not start in time"));
    }, 4000);
  });

  after(function (done) {
    this.timeout(5000);
    if (!server) return done();
    const onExit = () => done();
    server.on("exit", onExit);
    try {
      if (!server.killed) server.kill();
    } catch (e) {
      server.off("exit", onExit);
      done();
    }
  });

  it("Correct status code?", function (done) {
    request.get("http://localhost:7865/", (err, res) => {
      if (err) return done(err);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it("Correct result?", function (done) {
    request.get("http://localhost:7865/", (err, res, body) => {
      if (err) return done(err);
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });

  it("Other? (Content-Type header)", function (done) {
    request.get("http://localhost:7865/", (err, res) => {
      if (err) return done(err);
      expect(res.headers["content-type"]).to.match(/text\/html/);
      done();
    });
  });
});
