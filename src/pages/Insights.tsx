import { useEffect, useState } from "react";
import ReviewCard from "../components/ReviewCard";
import { getReviews } from "../services/api";

type Review = {
  username: string;
  rating: number;
  comment: string;
  sentiment: "Positive" | "Neutral" | "Negative";
};

export default function Insights() {
  const [reviews, setReviews] = useState<Review[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getReviews();
      setReviews(data);
    };
    fetchData();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Insights</h1>
      {reviews.map((r, idx) => (
        <ReviewCard key={idx} {...r} />
      ))}
    </div>
  );
}
