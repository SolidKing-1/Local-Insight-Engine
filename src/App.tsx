import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Competitors from "./pages/Competitors";
import Insights from "./pages/Insights"; // added
import NavBar from "./components/NavBar";

function App() {
  return (
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/competitors" element={<Competitors />} />
        <Route path="/insights" element={<Insights />} /> 
      </Routes>
    </BrowserRouter>
  );
}

export default App;
