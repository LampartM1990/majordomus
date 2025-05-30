# Majordomus

## Installation

1. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

2. Configure environment variables

```bash
cp .env.example .env
```

3. Run the application

```bash
python main.py
```

## TODO

### Database Integration (MongoDB)

- [ ] Setup MongoDB
- [ ] Choose ODM (Beanie or Tortoise)
- [ ] Create database models
- [ ] Get next task from the database

### FastAPI Implementation

- [x] Basic API setup
- [x] Health check endpoint
- [ ] Task management
  - [ ] Create, read, update, delete tasks
  - [ ] Task status management (e.g., pending, completed, failed)
- [ ] Task reminders and notifications
  - [ ] Webhook support
- [ ] Authorization (JWT authentication or API key)
- [ ] Rate limiting

### Task Scheduler

- [ ] Task scheduling system
  - [ ] Schedule tasks for specific dates and times
  - [ ] Support for recurring tasks (daily, weekly, monthly)
  - [ ] Custom day-of-week scheduling (e.g., every Monday and Wednesday)
  - [ ] Execution time management (e.g., run at 8 AM every day)

### Task Execution

- [ ] Task execution system
  - [ ] Execute tasks based on user-defined rules
  - [ ] Store task execution history
  - [ ] Log task execution details (success, failure, etc.)
- [ ] Task prioritization
  - [ ] Prioritize tasks based on user-defined criteria
  - [ ] Support for task dependencies (Task B depends on Task A)

### LLM Integration

- [ ] Integration with selected LLM
  - [ ] DeepSeek
  - [ ] OpenAI
  - [ ] Other LLMs ?
- [ ] Model configuration
- [ ] Generate tasks based on LLM responses

- API documentation: `http://localhost:${API_PORT}/docs`
- Alternative documentation: `http://localhost:${API_PORT}/redoc`
