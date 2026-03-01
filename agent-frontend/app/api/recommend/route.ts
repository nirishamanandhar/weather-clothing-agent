export async function POST(req: Request) {
    const body = await req.json();
  
    const backendUrl = process.env.BACKEND_URL;
    const backendToken = process.env.BACKEND_AUTH_TOKEN;
  
    if (!backendUrl || !backendToken) {
      return new Response(
        JSON.stringify({ error: "Server not configured correctly" }),
        { status: 500 }
      );
    }
  
    const res = await fetch(`${backendUrl}/recommend`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": backendToken
      },
      body: JSON.stringify(body),
    });
  
    const data = await res.text(); // or .json() if always JSON
  
    return new Response(data, {
      status: res.status,
      headers: { "Content-Type": res.headers.get("Content-Type") || "application/json" },
    });
  }
  