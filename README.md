<p align="center">
  <img
    src="https://raw.githubusercontent.com/yashsj/yashsj/main/assets/system-header.svg"
    alt="Suyash Jawadekar — animated backend and AI system diagram"
    width="100%"
  />
</p>

<div align="center">

### Production AI. Reliable backends. Built beyond the happy path.

Senior Software Engineer building cloud services and production LLM systems.<br>
Currently building at Shipped.ai · Previously at Amdocs · Co-founder of RadnessTech

[Explore my projects](https://github.com/yashsj?tab=repositories) · [Backend notes](https://github.com/yashsj/Backend_from_1st_principles) · [Say hello](mailto:suyashjawadekar@gmail.com)

</div>

---

## 👋 A little about me

I enjoy turning complex systems into useful products—and making sure they
still work when the happy path ends.

My work spans backend engineering, cloud infrastructure, and applied AI:
from APIs and distributed workers to grounded agents, evaluation pipelines,
and voice-first applications.

```text
suyash@dev:~$ cat engineering-principles.txt

Ground answers in evidence.
Verify actions in the backend.
Measure before optimizing.
Design for failure, not just success.
Keep learning from first principles.
```

## ⚡ What I build

- Production AI agents with grounded answers and verified tool execution.
- Backend services with retries, timeouts, idempotency, and clear failure handling.
- Evaluation pipelines that catch regressions before release.
- Cloud deployments with observability across inference, retrieval, and tool calls.

## 🛠️ Where I've built

### Shipped.ai · AI Engineer
*May 2025 — Present*

Building production LLM systems across conversational agents, grounded RAG,
model evaluation, and agent infrastructure.

- Reduced inference latency from approximately 4 seconds to 1 second.
- Used an 81-case held-out regression suite to evaluate changes.
- Implemented backend safeguards, observability, and authorized tool execution.

### Amdocs · Senior Software Engineer
*August 2021 — November 2024*

Built Python backend systems and cloud-based validation tooling, integrated
with CI/CD pipelines.

- Reduced system validation runtime from 2 hours to 20 minutes.
- Automated data provisioning and improved delivery turnaround.
- Built semantic search across more than 1,400 records.

### RadnessTech · Co-founder
*2018 — 2021*

Co-founded a tech media startup and helped lead product direction,
engineering coordination, and publishing workflows.

- Android app reached approximately 10,000 installs.
- YouTube channel grew to approximately 8,000 subscribers.

## 🚀 Selected work

### 🛒 Composable AI Shopping Agent · Team Fourcast

A team-built AI shopping agent that connects product discovery,
personalized recommendations, live Shopify checkout, and post-purchase
engagement across Gemini, Bloomreach, Shopify, and Databricks.

Built for the Bloomreach Composable AI Hackathon 2026.

My contributions:
- Reduced returning-user turn-2 response time from 7.4 seconds to 3.4 seconds
  through session caching and concurrent API requests.
- Prevented fabricated checkout links by accepting transactional URLs
  only when they exactly matched verified tool output.
- Debugged and stabilized two Cloud Run services by resolving webhook
  registration, signing-secret mismatches, and a stale container revision.

`Gemini` · `Bloomreach` · `Shopify` · `Databricks` · `GCP Cloud Run`

[Explore the team repository →](https://github.com/Seilarmoon7/Team_fourcast)

`Agentic AI` · `Caching` · `Tool validation` · `GCP Cloud Run`

### 🎙️ Voice-First Portfolio Assistant

A conversational way to explore my experience, skills, and projects—with
voice interaction and calendar integration.

- Integrates Gemini, Deepgram, and Google Calendar.
- Uses grounded tool calling with server-side authorization.
- Revalidates calendar availability before executing scheduling actions.

`Voice AI` · `Gemini` · `Deepgram` · `Google Calendar`

[Find the portfolio agent →](https://github.com/yashsj?tab=repositories&q=portfolio-agent)

### 🧠 Backend From First Principles

My notes and explanations on backend engineering:
how things work, why they work that way, and where the trade-offs are.

`Backend engineering` · `First principles` · `Learning in public`

[Explore the notes →](https://github.com/yashsj/Backend_from_1st_principles)

### 🔎 ReviewRecommender

A semantic review recommendation system that surfaces relevant Yelp reviews
using embeddings and vector search, with emotion-based filtering.

`Sentence Transformers` · `ChromaDB` · `Hugging Face`

[Browse my repositories →](https://github.com/yashsj?tab=repositories)

## 💻 Tools I use

### Languages

<p>
  <img
    src="https://skillicons.dev/icons?i=python,ts,java&theme=dark"
    alt="Python, TypeScript, and Java"
  />
</p>

### Backend & data

<p>
  <img
    src="https://skillicons.dev/icons?i=fastapi,mysql,kafka&theme=dark"
    alt="FastAPI, MySQL, and Kafka"
  />
</p>

### Cloud & infrastructure

<p>
  <img
    src="https://skillicons.dev/icons?i=aws,gcp,docker,kubernetes,jenkins,git&theme=dark"
    alt="AWS, Google Cloud, Docker, Kubernetes, Jenkins, and Git"
  />
</p>

### AI & LLM systems

`Amazon Bedrock` · `AgentCore` · `LangChain` · `RAG` · `Tool calling`

`Embeddings` · `Vector search` · `LoRA / QLoRA` · `LLM evaluation`

## 🧩 How I think about systems

```text
                         ┌── evaluation
                         │
request → API → agent → verified tools → result
           │      │             │
           │      └── retrieval │
           │                    │
           └── authorization ───┘

Across every step: observability · timeouts · retries · recovery
```

A model can propose an action. The backend decides whether it is authorized
and valid.

I'm interested in what happens when a request arrives twice, a dependency
times out, a worker crashes, or an agent produces a convincing answer
without supporting evidence.

## 🟩 Building, one commit at a time

<p align="center">
  <picture>
    <source
      media="(prefers-color-scheme: dark)"
      srcset="https://raw.githubusercontent.com/yashsj/yashsj/output/contribution-grid-dark.svg"
    />
    <source
      media="(prefers-color-scheme: light)"
      srcset="https://raw.githubusercontent.com/yashsj/yashsj/output/contribution-grid-light.svg"
    />
    <img
      src="https://raw.githubusercontent.com/yashsj/yashsj/output/contribution-grid-light.svg"
      alt="My contribution graph assembling itself from falling squares"
      width="100%"
    />
  </picture>
</p>

---

<div align="center">

### Less noise. More useful things.

[Browse my work](https://github.com/yashsj?tab=repositories) · [Get in touch](mailto:suyashjawadekar@gmail.com)

</div>
