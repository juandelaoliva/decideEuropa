import React, { Component } from "react";
import Header from "../components/Header";
import { Link } from "react-router-dom";

import "../styles/Home.css";

import { getVotings } from "../services/DecideAPI";

export default class MainPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      votings: []
    };
  }

  componentDidMount() {
    getVotings().then(votings => this.setState({ votings }));
  }

  isVotingActived({ start_date, end_date, id }) {
    var res = false;
    if (start_date === null && end_date === null) {
      res = "no_started";
    } else if (start_date !== null) {
      start_date = new Date(start_date);
      let now = Date.now();
      if (end_date !== null) {
        end_date = new Date(end_date);
        if (now >= start_date && now <= end_date) res = true;
        else if (now < start_date) res = "no_started";
        else if (now > end_date) res = "ended";
      } else {
        if (now >= start_date) res = true;
        else res = "no_started";
      }
    }

    return res === true ? (
      <div className="btn btn-green">
        <Link to={"/voting/" + id}>Ir a la votación</Link>
      </div>
    ) : (
      <div className="btn btn-red">
        {res === "no_started" ? (
          <p style={{ margin: "0px" }}>La votación no ha comenzado aún</p>
        ) : res === "eneded" ? (
          <p style={{ margin: "0px" }}>
            La votación ya acabó el día {end_date}
          </p>
        ) : (
          <p style={{ margin: "0px" }}>No disponible</p>
        )}
      </div>
    );
  }

  render() {
    return (
      <React.Fragment>
        <Header />
        <div id="container">
          <h2>Votaciones</h2>
          <main>
            {this.state.votings.map(voting => (
              <React.Fragment key={voting.id}>
                <div className="voting">
                  <p>
                    {voting.name}: <small>{voting.desc}</small>
                  </p>
                  {this.isVotingActived(voting)}
                </div>
                <hr />
              </React.Fragment>
            ))}
          </main>
        </div>
      </React.Fragment>
    );
  }
}
