import React from "react";
import { Link } from "react-router-dom";
import Header from "../components/Header";

import "../styles/Login.css";

export default class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userAuth: null,
      err: null,
      loginForm: {
        username: "",
        password: ""
      }
    };

    this.handleChange = this.handleChange.bind(this);
    this.login = this.login.bind(this);
  }

  login(e) {
    e.preventDefault();

    this.setState({ ...this.state, err: null });

    fetch("https://decide-europa-cabina.herokuapp.com/authentication/login/", {
      method: "POST",
      body: JSON.stringify(this.state.loginForm),
      headers: {
        "Content-type": "application/json"
      }
    })
      .then(res => res.json())
      .then(data => {
        if (data.token === undefined) {
          this.setState({ ...this.state, err: data });
        } else {
          this.props.loginUser(data.token);
        }
      })
      .catch(err => this.setState({ ...this.state, err: err }));
  }

  handleChange(event) {
    let { name, value } = event.target;
    this.setState({ loginForm: { ...this.state.loginForm, [name]: value } });
  }

  render() {
    return (
      <React.Fragment>
        <Header />
        <div style={{ position: "absolute", top: "20px", left: "25px" }}>
          <Link to="/" style={{ color: "white", textDecoration: "none" }}>
            <span role="img" aria-label="Back home" aria-labelledby="home" style={{ fontSize: "25px" }}>
              ⬅️
            </span>
          </Link>
        </div>
        <div id="container">
          <h2>Iniciar sesión</h2>
          <main id="login">
            <form>
              <div>
                <label for="username">Nombre de usuario</label>
                <input
                  type="text"
                  name="username"
                  id="username"
                  onChange={this.handleChange}
                />
              </div>
              <div>
                <label for="password">Contraseña</label>
                <input
                  type="password"
                  name="password"
                  id="password"
                  onChange={this.handleChange}
                />
              </div>
              <button type="submit" class="btn btn-blue" onClick={this.login}>
                Iniciar sesión
              </button>
              {this.state.err ? (
                <div id="err">Los credenciales no son válidas</div>
              ) : null}
            </form>
          </main>
        </div>
      </React.Fragment>
    );
  }
}
