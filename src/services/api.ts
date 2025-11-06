// GET / api / sentiment - summary;
// GET / api / competitors;
// GET / api / trends;
import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:5000/api", // Flask backend
});

export const getReviews = async () => {
  const res = await api.get("/reviews");
  return res.data;
};

export const getSentimentSummary = async () => {
  const res = await api.get("/sentiment-summary");
  return res.data;
};

export const getCompetitors = async () => {
  const res = await api.get("/competitors");
  return res.data;
};

export default api;


