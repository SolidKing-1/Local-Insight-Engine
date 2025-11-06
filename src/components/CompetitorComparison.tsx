import { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { getCompetitors } from "../services/api";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

type Competitor = { name: string; rating: number };

export default function CompetitorComparison() {
  const [competitors, setCompetitors] = useState<Competitor[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getCompetitors();
      setCompetitors(data);
    };
    fetchData();
  }, []);

  const data = {
    labels: competitors.map((c) => c.name),
    datasets: [
      {
        label: "Average Rating",
        data: competitors.map((c) => c.rating),
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
    ],
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Competitor Ratings</h2>
      <Bar data={data} />
    </div>
  );
}
