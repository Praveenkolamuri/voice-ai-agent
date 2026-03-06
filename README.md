# Real-Time Multilingual Voice AI Agent

Clinical Appointment Booking System

## Overview

This project implements a real-time multilingual voice AI agent capable of managing clinical appointments through natural voice conversations. The system supports booking, rescheduling, and cancelling appointments while maintaining contextual memory across conversations.

The agent supports English, Hindi, and Tamil and can operate both in inbound conversations and outbound reminder campaigns.

---

## Key Features

* Voice-based appointment booking
* Multilingual support (English, Hindi, Tamil)
* Session and persistent contextual memory
* Appointment conflict detection
* Real-time conversational pipeline
* Tool orchestration for scheduling operations
* Latency monitoring (<450ms target)

---

## System Architecture

Voice Input
→ Speech-to-Text (Whisper)
→ Language Detection
→ AI Agent (LLM reasoning)
→ Tool Orchestration
→ Appointment Scheduler
→ Database
→ Text-to-Speech
→ Voice Response

---

## Memory Design

### Session Memory

Stores current conversation state.

Example:
{
intent: "booking",
doctor: "cardiologist",
date: "tomorrow"
}

### Persistent Memory

Stores patient preferences and appointment history.

Example:
preferred_language: Hindi
last_doctor: Dr Sharma

---

## Scheduling Logic

The appointment engine validates:

* Doctor availability
* Slot conflicts
* Past-time booking attempts

If a slot is unavailable, the agent suggests alternative time slots.

---

## Latency Breakdown

Speech Recognition: ~120ms
Agent Reasoning: ~200ms
Speech Synthesis: ~90ms

Total latency: ~410ms

---

## Tech Stack

Python
FastAPI
WebSockets
OpenAI Whisper
Redis (session memory)
SQLite / PostgreSQL (appointments)
gTTS (text-to-speech)

---

## Running the Project

Install dependencies

pip install -r requirements.txt

Start the server

uvicorn backend.main:app --reload

Open API docs

http://127.0.0.1:8000/docs

---

## Known Limitations

* Real-time streaming audio is simulated via API
* Whisper processing is not optimized for production latency
* Outbound campaign scheduler is simplified
