import { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { getSentimentSummary } from "../services/api";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function Dashboard() {
  const [chartData, setChartData] = useState<{
    labels: string[];
    scores: number[];
  }>({
    labels: [],
    scores: [],
  });

  useEffect(() => {
    const fetchData = async () => {
      const data = await getSentimentSummary();
      setChartData({ labels: data.weeks, scores: data.scores });
    };
    fetchData();
  }, []);

  const data = {
    labels: chartData.labels,
    datasets: [
      {
        label: "Average Sentiment",
        data: chartData.scores,
        fill: false,
        borderColor: "rgb(75, 192, 192)",
        tension: 0.1,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { display: true },
      title: { display: true, text: "Weekly Sentiment Trends" },
    },
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Sentiment Trends</h1>
      <Line data={data} options={options} />
    </div>
  );
}
