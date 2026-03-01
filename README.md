# 🧥 Weather Clothing Agent

> An end-to-end agentic AI practice project — from a simple weather tool to a fully deployed production-style system.

## Overview

This began as a simple practice project: build a small agent that uses a single weather tool and returns a clothing recommendation. The agent part came together quickly — connecting a Google Gemini model to a tool, enforcing structured output, and validating responses locally was straightforward. The real learning started when I tried to turn this into a fully deployed production-style system.

Over time, the project evolved into a complete end-to-end pipeline with a FastAPI backend, a Next.js frontend, secure API authentication, and deployments on Railway and Vercel. Each stage surfaced real-world issues that shaped the final architecture.

---

## What the System Does

- Accepts natural language queries like *"What should I wear in Dublin tomorrow?"*
- Uses an agentic workflow to fetch weather data and reason about clothing
- Returns structured recommendations to a clean Next.js UI
- Runs securely in production using a server-side proxy and API-key header authentication

---

## Architecture
```
Frontend → server-side API route → backend → weather tool → agent → response
```

| Directory | Description |
|---|---|
| `agent-frontend/` | Next.js App Router frontend |
| `app/` | FastAPI backend (API routes, auth, validation) |
| `agent/` | All agent logic, data models, tool calls and reasoning |

---

## Key Learnings From the Build

### 1. The agent was the easy part — deployment was the real challenge

Building the agent and wiring it to a weather tool was straightforward. The complexity emerged when turning it into a real API and deploying it.

### 2. Railway exposed several dependency and Python-version issues

Railway's build system surfaced multiple compatibility problems: PydanticAI required specific versions of Python and related packages, some dependencies failed during installation, and the backend wouldn't start until the correct Python version was explicitly set.

Fixing this required:
- Pinning Python's required version via `runtime.txt`
- Adjusting dependency versions for mutual compatibility

### 3. The backend was initially exposed — adding security was essential

Because the frontend called the backend directly in the initial deployment, anyone could see the backend URL, spam the endpoint or burn API credits.

This led to:
- Adding a secret key based authentication layer in FastAPI
- Moving all frontend → backend calls into a server-side proxy route
- Ensuring secrets never reach the browser

### 4. Vercel misidentified the project until the structure was fixed

Vercel initially assumed the repo was a Python project because of backend files at the root. Fixing this required:
- Temporarily specifying the project type in `vercel.json`
- Setting the correct root directory (`agent-frontend`)
- Removing the config once Vercel recognized the project correctly
- Ensuring environment variables were correctly scoped to server-side only

---

## Running the Project Locally
```bash
# 1. Clone the repo
git clone <your-repo-url>
cd <repo>

# 2. Start the backend
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
export BACKEND_AUTH_TOKEN=your_local_secret
export WEATHER_API_KEY=your_weather_api_key
export GOOGLE_API_KEY=your_gemini_key
uvicorn app.web:app --reload

# FastAPI Backend runs at http://localhost:8000

# 3. Start the frontend
cd agent-frontend
npm install
echo "BACKEND_URL=http://localhost:8000" >> .env.local
echo "BACKEND_AUTH_TOKEN=your_local_secret" >> .env.local
npm run dev

# Next JS Frontend runs at http://localhost:3000
```

---

## Future Improvements

- [ ] Add visual outfit suggestions 
- [ ] Add location auto-detection
- [ ] Add caching for weather calls