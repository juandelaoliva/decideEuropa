import React from "react";
import { Link } from "react-router-dom";
import Login from "./Login";

export default class Voting extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      votingId: this.props.match.params.id,
      userAuth: null
    };

    this.loginUser = this.loginUser.bind(this);
  }

  loginUser(token) {
    this.setState({ ...this.props, userAuth: token });
  }

  render() {
    if (this.state.userAuth === null) {
      return <Login loginUser={this.loginUser} />;
    } else {
      return (
        <div id="voting">
          Voting page number {this.props.match.params.id} -
          <Link to="/">Go to Home</Link>
        </div>
      );
    }
  }
}
