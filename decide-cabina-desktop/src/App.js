import React, { Component } from "react";

import "./App.css";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Voting from "./pages/Voting";
import { BrowserRouter as Router, Route } from "react-router-dom";

export default class App extends Component {
  render() {
    return (
      <Router>
        <React.Fragment>
          <Route exact path="/" component={Home} />
          <Route path="/login" component={Login} />
          <Route path="/voting" component={Voting} />
        </React.Fragment>
      </Router>
    );
  }
}
