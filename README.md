# 🧠 FeedbackVault AI

## Organizational Feedback Memory Agent Powered by Hindsight

FeedbackVault AI is an AI-powered organizational memory agent that learns from historical customer feedback, product decisions, and outcomes using Hindsight persistent memory.

---

## 🚀 Live Demo

🌐 Live Application:
https://feedbackvault.streamlit.app/

💻 GitHub Repository:
https://github.com/thakursejal/FeedbackVault

---

## 🎯 Overview

Product teams receive large amounts of customer feedback and feature requests every day.

The challenge is not only collecting feedback — it is remembering what the organization learned from previous decisions.

A feature may have been rejected because customer demand was low. Months later, the same request may appear again with increasing demand. Without persistent organizational memory, teams may repeatedly evaluate the same problem from scratch.

FeedbackVault AI solves this problem using Hindsight as its persistent memory layer.

The agent recalls relevant historical experiences, identifies previous decisions and outcomes, and uses them as context when analyzing new customer feedback.

After the product team makes a decision, the decision and outcome are stored back into Hindsight, allowing the system to continuously build organizational knowledge.

---

## 💡 Problem Statement

Organizations often lose valuable knowledge between:

- Customer feedback
- Feature requests
- Product decisions
- Decision reasoning
- Implementation outcomes

Traditional feedback systems primarily store feedback as individual records.

They do not necessarily provide an intelligent memory of:

"What happened when we faced something similar before?"

FeedbackVault AI introduces a persistent memory layer connecting:

Customer Feedback
        ↓
Historical Experience
        ↓
Product Decision
        ↓
Outcome
        ↓
Organizational Memory
        ↓
Future Decision Support

---

## 🧠 The Solution

For every new piece of customer feedback, FeedbackVault AI:

1. Searches Hindsight for relevant historical experiences.
2. Recalls similar feedback and previous organizational decisions.
3. Identifies previous actions and outcomes.
4. Generates a context-aware product recommendation.
5. Allows the product team to make the final decision.
6. Stores the decision and outcome in Hindsight.
7. Uses the newly stored experience for future feedback analysis.

This creates a continuous organizational learning loop.

---

## 🔄 Hindsight Memory Loop

NEW CUSTOMER FEEDBACK
        ↓
Hindsight Recall
        ↓
Historical Experience
        ↓
AI Recommendation
        ↓
Product Team Decision
        ↓
Outcome
        ↓
Hindsight Retain
        ↓
Future Organizational Experience
        ↓
Better-Informed Future Decisions

---

## 🌟 Example: WhatsApp Notifications

### 1. Historical Feedback

Customers requested:

"Customers want WhatsApp notifications."

The product team previously rejected the feature because customer demand was considered too low.

This experience was stored in Hindsight.

### 2. New Feedback

Later, customers started requesting the feature again:

"Customers are requesting WhatsApp notifications again."

FeedbackVault AI recalls the previous experience.

The agent identifies that the request had previously been rejected because of low demand.

It recommends reviewing the current demand before repeating the previous decision.

### 3. Product Decision

The product team can record:

"The product team decided to reconsider WhatsApp notifications because customer demand increased."

### 4. Outcome

The team records:

"The feature was moved to a limited product pilot for further evaluation."

The decision and outcome are then stored in Hindsight.

### 5. Future Feedback

A new request arrives:

"Customers are still asking for WhatsApp notifications, and the pilot appears to be gaining interest."

Hindsight can now recall the newer organizational experience, including the previous reconsideration and pilot outcome.

The agent uses this updated history when analyzing the new request.

---

## 🏆 Why Hindsight Matters

The core of FeedbackVault AI is not simply generating a recommendation.

The important capability is persistent organizational memory.

Without memory:

Feedback
   ↓
Recommendation

With Hindsight:

Feedback
   ↓
Recall Past Experience
   ↓
Previous Decision
   ↓
Previous Outcome
   ↓
New Recommendation
   ↓
New Decision
   ↓
New Outcome
   ↓
Persistent Memory
   ↓
Future Learning

This allows organizational experience to accumulate over time.

---

## 🏗️ System Architecture

Streamlit Frontend
        │
        ▼
Feedback Analyzer
(agent.py)
        │
        ▼
Memory Layer
(memory.py)
        │
        ▼
Hindsight Cloud API
        │
        ▼
Persistent Organizational Memory

The Streamlit interface allows users to:

- Enter customer feedback
- View recalled Hindsight memories
- Review the agent recommendation
- Record product decisions
- Record outcomes
- Store new organizational experience

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Hindsight
- Hindsight Python Client
- REST API
- Requests
- python-dotenv
- GitHub
- Streamlit Community Cloud

---

## 📁 Project Structure

FeedbackVault/
│
├── app.py
├── agent.py
├── memory.py
├── test_memory.py
├── requirements.txt
├── .gitignore
│
└── data/
    └── feedback.json

### app.py

Provides the Streamlit user interface.

Features include:

- Customer feedback input
- Hindsight memory display
- Agent recommendation
- Product decision input
- Outcome input
- Decision and outcome storage

### agent.py

Contains the feedback analysis logic.

It:

- Retrieves relevant memories
- Processes historical experience
- Removes duplicate memories
- Uses previous decisions and outcomes
- Generates contextual recommendations

### memory.py

Handles the Hindsight integration.

It provides functions for:

- Retaining organizational experience
- Recalling relevant historical experience

### test_memory.py

Used for testing the Hindsight memory integration and verifying that stored organizational experience can be recalled.

---

## 🔐 Security

Sensitive API credentials are not stored directly in the source code.

The Hindsight API key is stored using environment variables and Streamlit Secrets.

The .env file is excluded from Git using .gitignore.

Never commit your real API key to GitHub.

---

## ⚙️ Local Installation

### 1. Clone the Repository

git clone https://github.com/thakursejal/FeedbackVault.git

cd FeedbackVault

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Configure Hindsight API Key

Create a .env file:

HINDSIGHT_API_KEY=your_api_key_here

### 4. Run the Application

streamlit run app.py

The application will open in your browser.

---

## 🌐 Deployment

FeedbackVault AI is deployed using Streamlit Community Cloud.

### Live Application

https://feedbackvault.streamlit.app/

### Source Code

https://github.com/thakursejal/FeedbackVault

---

## 📊 Learning Workflow

### Stage 1 — Receive Feedback

Customer Feedback

↓

### Stage 2 — Recall

Search Hindsight

↓

### Stage 3 — Understand History

Previous Feedback  
Previous Decisions  
Previous Outcomes

↓

### Stage 4 — Recommend

Context-Aware Recommendation

↓

### Stage 5 — Human Decision

Product Team Decision

↓

### Stage 6 — Record Outcome

Decision + Outcome

↓

### Stage 7 — Learn

Store Experience in Hindsight

↓

### Stage 8 — Future Recall

Use Organizational Experience for Future Feedback

---

## 🎯 Hackathon Alignment

FeedbackVault AI is designed around the theme:

"AI Agents That Learn Using Hindsight"

The project focuses on persistent memory as a core capability rather than treating memory as an additional feature.

### Innovation

Applies persistent organizational memory to product feedback and decision support.

### Hindsight Memory

Historical feedback, decisions, and outcomes are retained and recalled using Hindsight.

### Technical Implementation

Uses Python, Streamlit, Hindsight, REST API integration, and persistent memory workflows.

### User Experience

The user can enter feedback, view recalled organizational experience, review the recommendation, and record the final product decision and outcome.

### Real-World Impact

Can help product teams avoid repeatedly evaluating similar requests without historical context.

---

## 🌍 Potential Real-World Applications

FeedbackVault AI can be adapted for:

- SaaS product teams
- Product management
- Customer success teams
- Customer support organizations
- Feature request management
- Product research
- Internal decision tracking
- Business intelligence workflows
- Organizational knowledge management

---

## 🔮 Future Enhancements

Future versions could include:

- Feedback trend dashboards
- Demand frequency analysis
- Automatic feedback categorization
- Repeated-request alerts
- LLM-powered recommendations
- Decision history timelines
- Team-level organizational memory
- Richer outcome tracking
- Advanced similarity search
- Long-term feature performance analysis

---

## 🚀 Key Differentiator

Most feedback systems answer:

"What are customers asking for?"

FeedbackVault AI additionally asks:

"What did our organization learn the last time customers asked for something similar?"

That historical context becomes reusable organizational intelligence.

---

## 🧠 Core Concept

ORGANIZATIONAL EXPERIENCE
            ↓
       HINDSIGHT
         MEMORY
            ↓
    Customer Feedback
            ↓
       AI Analysis
            ↓
     Recommendation
            ↓
    Human Decision
            ↓
         Outcome
            ↓
   Store Experience
      in Hindsight
            ↓
      Future Learning

---

## 👩‍💻 Author

Thakur Sejal

B.Tech — Artificial Intelligence & Machine Learning

---

## 🔗 Project Links

🌐 Live Demo:
https://feedbackvault.streamlit.app/

💻 GitHub Repository:
https://github.com/thakursejal/FeedbackVault

---

## ⭐ Final Thought

FeedbackVault AI turns organizational history into reusable intelligence.

Instead of repeatedly asking:

"What should we do with this feedback?"

the organization can ask:

"What have we learned from similar feedback before?"

And Hindsight provides the memory.
