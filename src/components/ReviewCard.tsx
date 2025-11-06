type ReviewProps = {
  username: string;
  rating: number;
  comment: string;
  sentiment: "Positive" | "Neutral" | "Negative";
};

export default function ReviewCard({
  username,
  rating,
  comment,
  sentiment,
}: ReviewProps) {
  const sentimentColor =
    sentiment === "Positive"
      ? "text-green-600"
      : sentiment === "Neutral"
      ? "text-gray-600"
      : "text-red-600";

  return (
    <div className="border rounded-md p-4 mb-3 shadow-sm hover:shadow-md transition">
      <h3 className="font-semibold">
        {username} - {rating}⭐
      </h3>
      <p className={`mt-2 ${sentimentColor}`}>{sentiment}</p>
      <p className="mt-1 text-gray-800">{comment}</p>
    </div>
  );
}
