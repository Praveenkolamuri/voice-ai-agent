# Real-Time Multilingual Voice AI Agent

### Clinical Appointment Booking System

## Overview

This project implements a **Real-Time Multilingual Voice AI Agent** capable of managing clinical appointments through natural voice conversations. The system supports appointment booking, cancellation, and rescheduling while maintaining conversational context and patient history.

The AI agent processes voice input, interprets user intent using an AI reasoning module, and performs scheduling actions using backend tools. The response is then converted back into speech, creating a seamless conversational experience.

The system supports **three languages**:

* English
* Hindi
* Tamil

The design focuses on **low latency (<450ms response time)**, modular architecture, and scalable agent-based orchestration.

---

# System Architecture

The system follows a **real-time conversational pipeline**:

Voice Input
→ Speech-to-Text
→ Language Detection
→ AI Agent (LLM Reasoning)
→ Tool Orchestration
→ Appointment Scheduler
→ Database
→ Text-to-Speech
→ Audio Response

The architecture diagram is available in:

```
docs/architecture.png
```

---

# Key Features

### Voice-Based Appointment Management

The AI agent can:

* Book appointments
* Cancel appointments
* Reschedule appointments
* Suggest alternative slots when conflicts occur

---

### Multilingual Support

The system detects and maintains conversations in:

* English
* Hindi
* Tamil

Language preference can be stored in persistent memory for returning patients.

---

### Contextual Memory

The agent maintains **two levels of memory**:

#### Session Memory

Stores current conversation state.

Example:

```
User: Book appointment
Agent: Which doctor?
User: Cardiologist
```

Session memory stores the intent until confirmation.

#### Persistent Memory

Stores long-term patient information:

* Preferred language
* Previous appointments
* Preferred doctors

---

### Scheduling and Conflict Detection

The appointment engine validates:

* Doctor availability
* Double booking conflicts
* Invalid time selections
* Past-time bookings

When a slot is unavailable, the agent suggests alternative time slots.

---

# Project Structure

```
voice-ai-agent
│
├── agent
│   ├── agent.py
│   ├── prompts.py
│   └── tools.py
│
├── backend
│   ├── main.py
│   └── websocket.py
│
├── services
│   ├── speech_to_text.py
│   ├── language_detection.py
│   └── text_to_speech.py
│
├── memory
│   ├── session_memory.py
│   └── persistent_memory.py
│
├── scheduler
│   └── appointment_engine.py
│
├── database
│   └── db.py
│
├── docs
│   └── architecture.png
│
├── requirements.txt
└── README.md
```

---

# Technology Stack

| Component               | Technology          |
| ----------------------- | ------------------- |
| Backend API             | FastAPI             |
| Real-time communication | WebSockets          |
| Speech-to-text          | Whisper             |
| Language detection      | langdetect          |
| Agent reasoning         | LLM-based logic     |
| Text-to-speech          | gTTS                |
| Session memory          | Redis / in-memory   |
| Persistent storage      | SQLite / PostgreSQL |

---

# Latency Considerations

The system is designed to maintain a **target response latency under 450 milliseconds**.

Example breakdown:

| Stage              | Estimated Time |
| ------------------ | -------------- |
| Speech recognition | ~120ms         |
| Agent reasoning    | ~200ms         |
| Speech synthesis   | ~90ms          |

Total estimated latency:

```
≈ 410ms
```

Latency is logged within the backend service for monitoring and optimization.

---

# Running the Project

## Install Dependencies

```
pip install -r requirements.txt
```

## Start the Server

```
uvicorn backend.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

# API Testing

Open the interactive API documentation:

```
http://127.0.0.1:8000/docs
```

Example request:

```
Book cardiologist appointment tomorrow
```

Example response:

```
Available slots are 10:00 AM, 2:00 PM, and 4:30 PM.
Which time would you like?
```

---

# Error Handling

The system gracefully handles scenarios such as:

* Invalid requests
* Booking conflicts
* Scheduling errors
* AI interpretation failures

Fallback message example:

```
"I'm having trouble understanding the request. Could you repeat?"
```

---

# Known Limitations

* Real-time streaming audio is simulated through API calls
* Whisper processing is not optimized for production latency
* Outbound campaign scheduler is simplified

---

# Future Improvements

* Real-time WebRTC audio streaming
* Redis-backed distributed session memory
* Horizontal scaling with container orchestration
* Background campaign scheduler for reminders

---

# Demo

A demonstration of the system architecture and functionality is provided via a Loom video submission as part of the assignment.
