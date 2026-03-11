# Personal AI Assistant Agent

An LLM-powered personal productivity assistant built using n8n, Streamlit, OpenAI, and Google Workspace integrations. The system accepts natural language requests through a Streamlit interface, routes them to an AI Agent in n8n, and performs actions across email, calendar, notes, tasks, web search, and expense tracking tools.


---

## Overview

This project is a multi-capability AI assistant designed to automate day-to-day productivity workflows from a single conversational interface. It combines a front-end chat application with an n8n orchestration layer and multiple integrated tools.

This assistant can:

- Search the web for live information.

- Create and fetch calendar events.

- Create, update and retrieve notes.

- Track expenses using Google Sheets.

- Create, fetch and delete tasks.

- Read and send emails through Gmail.

- Maintain conversational context using memory.


---

## System Architecture

| Layer | Component | Description |
|------|------|------|
| Interface Layer | Streamlit UI | User enters natural language requests |
| Trigger Layer | n8n Webhook | Receives request and triggers workflow |
| Reasoning Layer | AI Agent (OpenAI + Memory) | Interprets intent and decides which tool to use |
| Decision Layer | Tool Selection | Maps user intent to the correct tool |
| Execution Layer | External Tools | Gmail, Calendar, Docs, Tasks, Sheets, Search |
| Response Layer | Webhook Response | Sends processed response back |
| Output Layer | Streamlit UI | Displays final result to the user |


---

## End-to-End Workflow:

1. User Interaction Layer:

- The user enters a natural language request in the Streamlit interface.

- The request is sent to the n8n webhook endpoint.


2. Orchestration Layer:

- The Webhook triggers the workflow in n8n.

- The request is passed to the AI Agent node.


3. Reasoning Layer:

- The AI Agent uses:

    - OpenAI Chat Model for intent understanding and response generation

    - System prompt instructions for tool-selection rules

    - Simple Memory for conversation continuity

- Based on the request, the agent determines which tool to call.


4. Tool Execution Layer:

Depending on the user intent, the agent invokes one of the following capability groups:

A. Web Search

- Tool: Google Search / SerpAPI

- Use case: answering live queries, factual lookups, or current information requests

B. Calendar Management

- Tools:

    - Create Calendar Event

    - Get Single Calendar Event

    - Get Calendar Events

- Use case: scheduling meetings, checking events, fetching event details

C. Notes Management

- Tools:

    - Create Notes File

    - Update Notes

    - Get Notes

- Use case: storing ideas, updating notes, retrieving saved information

D. Expense Tracking

- Tools:

    - Calculator

    - Add Expense

    - Get Expenses

- Use case: recording expenses, computing values, retrieving expense history

E. Task Management

- Tools:

    - Create Task

    - Get Single Task

    - Get Multiple Tasks

    - Delete Task

- Use case: to-do creation, task retrieval, task deletion

F. Gmail Operations

- Tools:

    - Get Single Gmail Message

    - Get Multiple Gmail Messages

    - Send Gmail Message

- Use case: reading emails, fetching inbox content, sending email replies

5. Response Layer

- Tool outputs are sent back to the AI Agent.

- The agent formats a user-friendly response.

- The result is returned through Respond to Webhook.

- The final output is displayed in the Streamlit UI.


---

## Tools and Technologies Used

### Core Stack

- `n8n` – workflow orchestration and tool integration

- `Streamlit` – front-end chat interface

- `OpenAI Chat Model` – natural language understanding and response generation

- `Simple Memory` – short-term conversational memory within the workflow

### Integrations

- **Google Calendar API** – event creation and retrieval

- **Gmail API** – email read and send operations

- **Google Docs API** – note creation, update, and retrieval

- **Google Tasks API** – task management

- **Google Sheets API** – expense logging and retrieval

- **SerpAPI / Google Search** – web search capability

- **Calculator Tool** – arithmetic and expense calculations


---

## Key Features

- Natural language interface for multiple productivity actions

- Centralized AI Agent for intent classification and tool routing

- Multi-tool support within a single workflow

- Memory-enabled interactions for smoother conversations

- Google Workspace integration for real-world utility

- Expense tracking backed by spreadsheet storage

- Modular workflow design for future expansion


---

## Example User Requests

- "What meetings do I have today?"

- "Create a calendar event for tomorrow at 5 PM"

- "Add a note called project ideas"

- "Update my meeting notes with action items"

- "Add an expense of 250 for lunch"

- "Show all my expenses this week"

- "Create a task to submit the report"

- "Delete the task buy groceries"

- "Read my latest email"

- "Send an email to HR about interview availability"

- "Search the web for the latest AI news"


---

## Possible Future Enhancements

- Multi-step action chaining (for example, create event + send email)

- Authentication layer for multi-user support

- Better long-term memory and personalization

- Voice input and output

- Dashboard for expenses, tasks, and upcoming events

- Logging and analytics for agent decisions