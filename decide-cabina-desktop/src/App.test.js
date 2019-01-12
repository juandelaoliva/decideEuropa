import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

import { expect } from "chai";

import Home from "./pages/Home";
import Login from "./pages/Login";

import { BrowserRouter as Router, Route } from "react-router-dom";

import { shallow } from "enzyme";


it("Renderiza la aplicación completa sin problemas", () => {
  const div = document.createElement("div");
  ReactDOM.render(<App />, div);
});

it("Renderiza la vista de listado de votaciones", () => {
  const div = document.createElement("div");

  ReactDOM.render(<Home />, div);
});

it("Debe haber un listado de votaciones con una votación", async () => {
  const wrapper = shallow(<Home />);

  wrapper.setState({
    votings: [
      {
        id: 1,
        name: "Votacion 1",
        desc: "Esta es la votación nº 1",
        question: {
          desc: "¿Qué te gusta desayunar?",
          options: [
            {
              number: 1,
              option: "Cereales"
            },
            {
              number: 2,
              option: "Huesos"
            }
          ]
        },
        start_date: "2019-01-11T19:01:25.738661Z",
        end_date: null,
        pub_key: {
          p: 8.5343042572311182030845293606311653334470008306390938154326172313932617287583e76,
          g: 4.0053406469274463345649215089733867786583483803327603459455966756938997645511e76,
          y: 7.5010115536702325739341511816279757331569390485358481347751907587938815760302e76
        },
        auths: [
          {
            name: "Web",
            url: "https://clebaltest.herokuapp.com",
            me: true
          }
        ],
        tally: null,
        postproc: null
      }
    ]
  });

  expect(wrapper.find(".voting")).to.have.lengthOf(1);
});

it("Renderiza la vista para iniciar sesión", () => {
  function loginUser(auth) {
    return "";
  }
  const div = document.createElement("div");

  ReactDOM.render(
    <Router>
      <Login loginUser={loginUser} />
    </Router>,
    div
  );
});

it("Escribir en el formulario para iniciar sesión", () => {
  function loginUser(auth) {
    return "";
  }

  const wrapper = shallow(<Login loginUser={loginUser} />);

  var inputUsername = wrapper.find({ name: "username" });
  var inputPassword = wrapper.find({ name: "password" });

  inputPassword.simulate("change", {
    target: { name: "password", value: "adminadmin" }
  });
  inputUsername.simulate("change", {
    target: { name: "username", value: "root" }
  });

  expect(wrapper.state("loginForm")["username"]).to.equal("root");
  expect(wrapper.state("loginForm")["password"]).to.equal("adminadmin");
});
