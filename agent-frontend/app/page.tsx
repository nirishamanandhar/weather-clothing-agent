"use client";
import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  async function ask() {
    const res = await fetch("/api/recommend", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({message}),
    });
    const data = await res.json();
    setResponse(data.recommendation);
  }


  return (
    <div style={{ padding: 40, fontFamily: "sans-serif" }}>
      <h1>Weather-based Clothing Suggestions</h1>

      <textarea
        rows={3}
        placeholder="Ask something..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{ width: "100%", padding: 10 }}
      />

      <button onClick={ask} style={{ marginTop: 10 }}>
        Ask
      </button>

      {response && (
        <div style={{ marginTop: 20, padding: 20, background: "#000", color: "#fff", borderRadius: 8, whiteSpace: "pre-wrap", }} > <strong style={{ color: "#0ff" }}>Agent</strong> <p>{response}</p> </div>
      )}
    </div>
  );
}
