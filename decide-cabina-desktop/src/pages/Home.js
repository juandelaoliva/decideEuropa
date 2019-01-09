import React, { Component } from "react";
import Header from "../components/Header";
import { Link } from "react-router-dom";

import "../styles/Home.css";

export default class MainPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      votings: []
    };
  }

  componentDidMount() {
    fetch("http://decide-europa-cabina.herokuapp.com/voting", {
      method: "GET"
    })
      .then(res => res.json())
      .then(data => this.setState({ votings: data }));
  }

  isVotingActived({ start_date, end_date, id }) {
    var res = false;
    if (start_date === null && end_date === null) {
      res = true;
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
          <p>La votación no ha comenzado, comienda {start_date}</p>
        ) : res === "eneded" ? (
          <p>La votación ya acabó el día {end_date}</p>
        ) : (
          <p>No disponible</p>
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
