ClauseGuard 🛡️

ClauseGuard is an AI-powered contract assistant built for the IBM TechXchange 2025 Pre-conference watsonx Hackathon.
It integrates with Watson Orchestrate via an OpenAPI spec and custom workflow to:

📌 Classify a contract clause

⚖️ Assess its risk with explanation

✍️ Suggest a safer/clearer rewrite

🚀 Features

Simple OpenAPI backend (openapi.yaml) with 3 endpoints: /classify, /risk, /rewrite

Deployed to Watson Orchestrate as tools using the OpenAPI import feature

Behavior workflow that chains tools automatically for end-to-end analysis

Fully interactive Orchestrate agent: just paste a clause and get instant results

🛠️ Tech Stack

Watson Orchestrate

Custom API (OpenAPI 3.0 spec)

ngrok (for tunneling local server to cloud)

Python / FastAPI (backend implementation)

📂 Project Structure
ClauseGuard/
│── openapi.yaml               # API specification for Watson Orchestrate
│── behavior_instructions.txt  # Workflow instructions for Orchestrate
│── screenshots/               # Demo screenshots
│── demo_video.mp4             # (Optional) Recorded demo video
│── README.md                  # Project documentation

⚡ How It Works

Import openapi.yaml into Watson Orchestrate → tools /classify, /risk, /rewrite become available

Add these tools to your Toolset

Create a new Behavior using behavior_instructions.txt

Deploy the agent → test by pasting any contract clause

Get instant classification, risk analysis, and rewrite suggestion

🎥 Demo

(Insert link to Loom/YouTube video here)

🏆 Hackathon Info

Submitted to: IBM TechXchange 2025 Pre-conference watsonx Hackathon
