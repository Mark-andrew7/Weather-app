import logo from "./logo.svg";
import "./App.css";
import Header from "./components/Header";
import Hero from "./components/Hero";
import Features from "./components/Features";
import About from "./components/About";
import CallToAction from "./components/CallToAction";
import Contact from "./components/Contact";
import Footer from "./components/Footer";
//import logo from "./images/logo.png";

function App() {
  return (
    <div className="App">
      <Header />
      <Hero />
      <Features />
      <About />
      <CallToAction />
      <Contact />
      <Footer />
    </div>
  );
}

export default App;
