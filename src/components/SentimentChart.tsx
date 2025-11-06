"use client";
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

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

type SentimentData = {
  week: string;
  score: number;
}[];

const mockData: SentimentData = [
  { week: "Week 1", score: 0.75 },
  { week: "Week 2", score: 0.82 },
  { week: "Week 3", score: 0.68 },
  { week: "Week 4", score: 0.9 },
];

const data = {
  labels: mockData.map((d) => d.week),
  datasets: [
    {
      label: "Average Sentiment",
      data: mockData.map((d) => d.score),
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

export default function SentimentChart() {
  return <Line data={data} options={options} />;
}
