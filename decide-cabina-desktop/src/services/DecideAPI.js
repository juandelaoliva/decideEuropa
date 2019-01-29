const API_URL = "https://decide-europa.herokuapp.com";

if (fetch === undefined) {
  var fetch = require("isomorphic-fetch");
}

async function getVotings() {
  return await fetch(API_URL + "/voting", {
    method: "GET",
    mode: "cors",
    headers: {
      Origin: "http://localhost:3000"
    }
  }).then(res => res.json());
}

function login(loginForm) {
  return new Promise((resolve, reject) => {
    fetch(API_URL + "/authentication/login/", {
      method: "POST",
      mode: "cors",
      body: JSON.stringify(loginForm),
      headers: {
        "Content-type": "application/json",
        Origin: "http://localhost:3000"
      }
    })
      .then(res => res.json())
      .then(data => {
        if (data.token === undefined) {
          reject(data);
        } else {
          var auth = { token: data.token };

          fetch(API_URL + "/authentication/getuser/", {
            method: "POST",
            mode: "cors",
            body: JSON.stringify(auth),
            headers: {
              "Content-type": "application/json",
              Origin: "http://localhost:3000"
            }
          })
            .then(res => res.json())
            .then(userDetails => {
              auth = { ...auth, id: userDetails.id };
              resolve(auth);
            })
            .catch(err => reject(err));
        }
      })
      .catch(err => reject(err));
  });
}

function vote(auth, votingId, cipher) {
  return new Promise((resolve, reject) => {
    fetch(API_URL + "/store/", {
      method: "POST",
      mode: "cors",
      body: JSON.stringify({
        vote: { a: cipher.alpha.toString(), b: cipher.beta.toString() },
        voting: votingId,
        voter: auth.id,
        token: auth.token
      }),
      headers: {
        "Content-type": "application/json",
        Authorization: "Token " + auth.token,
        Origin: "http://localhost:3000"
      }
    })
      .then(async res => {
        if (res.status !== 200) {
          reject("Ha habido algún problema");
        } else {
          resolve();
        }
      })
      .catch(err => this.setState({ ...this.state, err: err }));
  });
}

function getVotingDetails(votingId) {
  return new Promise((resolve, reject) => {
    fetch(API_URL + "/voting/?id=" + votingId, {
    mode: "cors",
    headers: {
      "Content-type": "application/json",
      Origin: "http://localhost:3000"
    }
  })
    .then(res => res.json())
    .then(data => resolve(data))
    .catch(err => reject(err));
  })
}

export { getVotings, login, vote, getVotingDetails };
