# ClauseGuard - IBM TechXchange 2025 watsonx hackathon project

ClauseGuard is an AI-powered contract assistant built for the IBM TechXchange 2025 Pre-conference watsonx Hackathon.  
It integrates with Watson Orchestrate via an OpenAPI spec and a custom workflow to:

- Classify a contract clause  
- Assess its risk with explanation  
- Suggest a safer/clearer rewrite  

## Features
- OpenAPI backend (`openapi.yaml`) with 3 endpoints: `/classify`, `/risk`, `/rewrite`  
- Imported into Watson Orchestrate as tools  
- Behavior workflow that chains the tools automatically  
- End-to-end clause analysis with a single input  

## Tech Stack
- Watson Orchestrate  
- OpenAPI 3.0 (FastAPI backend)  
- ngrok (tunnel for local API)  
- Python  


## How It Works
1. Import `openapi.yaml` into Watson Orchestrate.  
2. Add the three tools (`/classify`, `/risk`, `/rewrite`) to your toolset.  
3. Create a new Behavior in Watson Orchestrate and paste `behavior_instructions.txt`.  
4. Deploy the agent.  
5. Provide a contract clause as input and receive classification, risk analysis, and a rewrite.  

## Demo


## Hackathon Info
- Submitted to: IBM TechXchange 2025 Pre-conference watsonx Hackathon  

## License
This project is licensed under the MIT License - see the LICENSE file for details.
