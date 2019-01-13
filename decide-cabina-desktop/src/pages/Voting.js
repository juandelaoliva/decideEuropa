import React from "react";
import { Link } from "react-router-dom";
import Login from "./Login";
import Header from "../components/Header";

import { vote, getVotingDetails } from "../services/DecideAPI";

export default class Voting extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      votingId: this.props.match.params.id,
      voting: null,
      userAuth: null,
      answer: null,
      err: null
    };

    this.loginUser = this.loginUser.bind(this);
    this.handleOptionChange = this.handleOptionChange.bind(this);
    this.submitForm = this.submitForm.bind(this);
  }

  submitForm(event) {
    event.preventDefault();

    this.setState({ ...this.state, err: null });

    if (this.state.answer == null) {
      this.setState({ ...this.state, err: "Debe seleccionar una respuesta" });
    } else {
      var { ElGamal, BigInt } = window;
      ElGamal.BITS = 256;
      let { pub_key } = this.state.voting;
      var bigpk = {
        p: BigInt.fromJSONObject(`${pub_key.p}`),
        g: BigInt.fromJSONObject(`${pub_key.g}`),
        y: BigInt.fromJSONObject(`${pub_key.y}`)
      };
      var bigmsg = BigInt.fromJSONObject(this.state.answer);
      var cipher = ElGamal.encrypt(bigpk, bigmsg);
      vote(this.state.userAuth, this.state.votingId, cipher)
        .then(_ => this.props.history.push("/"))
        .catch(err => this.setState({ ...this.state, err }));
    }
  }

  handleOptionChange(changeEvent) {
    this.setState({
      [changeEvent.target.name]: changeEvent.target.value
    });
  }

  loginUser(auth) {
    this.setState({ ...this.state, userAuth: auth });
  }

  componentDidUpdate(_, prevState) {
    if (prevState.userAuth === null && this.state.userAuth !== null) {
      getVotingDetails(this.state.votingId).then(data => {
        this.setState({ ...this.state, voting: data[0] })
      })
    }
  }

  render() {
    if (this.state.userAuth === null) {
      return <Login loginUser={this.loginUser} />;
    } else if (this.state.voting === null) {
      return <p>Cargando...</p>;
    } else {
      let vot = this.state.voting;
      return (
        <React.Fragment>
          <Header />
          <div style={{ position: "absolute", top: "20px", left: "25px" }}>
            <Link to="/" style={{ color: "white", textDecoration: "none" }}>
              <span
                role="img"
                aria-label="Back home"
                aria-labelledby="home"
                style={{ fontSize: "25px" }}
              >
                ⬅️
              </span>
            </Link>
          </div>
          <div id="container">
            <h2>{vot.name}</h2>
            <p>{vot.desc}</p>
            <hr />
            <div id="question">
              <h3>{vot.question.desc}</h3>
              {vot.question.options.map(op => (
                <React.Fragment key={op.number}>
                  <label>
                    <input
                      type="radio"
                      name="answer"
                      value={op.option}
                      className="form-check-input"
                      onChange={this.handleOptionChange}
                    />
                    {op.option}
                  </label>
                  <br />
                </React.Fragment>
              ))}
            </div>
            <br />
            <button className="btn btn-green" onClick={this.submitForm}>
              Votar
            </button>
            {this.state.err ? <div id="err">{this.state.err}</div> : null}
          </div>
        </React.Fragment>
      );
    }
  }
}
