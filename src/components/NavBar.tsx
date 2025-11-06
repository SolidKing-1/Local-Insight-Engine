import { Link } from "react-router-dom";

export default function NavBar() {
  return (
    <nav className="bg-gray-800 text-white p-4 flex justify-between">
      <h1 className="font-bold text-lg">Local Insight Engine</h1>
      <div className="space-x-4">
        <Link to="/">Dashboard</Link>
        <Link to="/competitors">Competitors</Link>
        <Link to="/insights">Insights</Link> 
      </div>
    </nav>
  );
}
