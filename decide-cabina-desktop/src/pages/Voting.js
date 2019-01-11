import React from "react";
import { Link } from "react-router-dom";
import Login from "./Login";
import Header from "../components/Header";

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

    fetch("https://decide-europa-cabina.herokuapp.com/store/", {
      method: "POST",
      body: JSON.stringify({
        voting: this.state.votingId,
        voter: this.state.answer,
        token: this.state.userAuth.token
      }),
      headers: {
        "Content-type": "application/json",
        "Authorization": "Token " + this.state.userAuth.token
      }
    })
      .then(res => res.json())
      .then(data => {
        if (JSON.stringify(data) === JSON.stringify({})) {
          this.setState({ ...this.state, err: data });
        } else {
          this.props.history.push("/");
        }
      })
      .catch(err => this.setState({ ...this.state, err: err }));
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
      fetch(
        "http://decide-europa-cabina.herokuapp.com/voting/?id=" +
          this.state.votingId
      )
        .then(res => res.json())
        .then(data => this.setState({ ...this.state, voting: data[0] }));
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
                      value={op.number}
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
            {this.state.err ? (
              <div id="err">
                Los credenciales no son válidas: {this.state.err}
              </div>
            ) : null}
          </div>
        </React.Fragment>
      );
    }
  }
}
