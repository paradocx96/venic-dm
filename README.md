<div align="center">

# VENIC - Dialogue Management

**Voice Enabled Intelligent Programming Assistant**

[![Website](https://img.shields.io/badge/Website-venic.io-blue)](https://venic.io)
[![GitHub](https://img.shields.io/badge/GitHub-paradocx96%2Fvenic--dm-181717?logo=github)](https://github.com/paradocx96/venic-dm)
[![Rasa](https://img.shields.io/badge/Rasa-3.0.8-5A17EE?logo=rasa)](https://rasa.com/)
[![Python](https://img.shields.io/badge/Python-3.7.7-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Training the Model](#training-the-model)
- [Testing](#testing)
- [Deployment](#deployment)
- [API Endpoints](#api-endpoints)
- [Dataset Generation](#dataset-generation)
- [Model Evaluation](#model-evaluation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

VENIC Dialogue Management is a conversational AI system built on Rasa that enables voice-controlled programming assistance. The system understands natural language commands and translates them into programming actions, supporting Java development, IDE operations, and version control workflows.

This dialogue management module serves as the natural language understanding (NLU) and dialogue policy component of the VENIC ecosystem, processing user intents and managing conversational flows for programming assistance.

### Key Capabilities

- **Programming Language Support**: Comprehensive Java command recognition (classes, methods, variables, arrays, collections, OOP concepts)
- **IDE Automation**: Voice commands for IDE operations (file management, editing, navigation, views)
- **Version Control**: Git command interpretation and execution
- **Context-Aware Dialogues**: Maintains conversation context for multi-turn interactions
- **Extensible Intent System**: Easily add new intents and responses

---

## Features

### Programming Commands

- **Java Language Constructs**
  - Classes, Interfaces, and Enums
  - Methods, Functions, and Procedures
  - Variables, Attributes, Properties, and Constants
  - Arrays and Collections (ArrayList, HashMap, HashSet, LinkedList)
  - Control Flow (if-else, loops, switch)
  - OOP Concepts (constructors, encapsulation, inheritance)

### IDE Commands

- **File Operations**: Create, open, save, delete files
- **Project Management**: Build, compile, run, debug, clean projects
- **Editor Actions**: Cut, copy, paste, undo, redo, find, replace
- **View Management**: Split editor, toggle panels, zoom controls
- **Navigation**: Go to file, switch editors, cursor movements
- **Configuration**: Settings, extensions, themes, keyboard shortcuts

### Version Control

- Git initialization and configuration
- Branch creation and switching
- Add, commit, push, pull operations
- Merge, diff, log, status, stash commands

### Dialogue Management

- Intent classification with high accuracy
- Entity extraction (names, types, numbers, messages)
- Slot filling for context retention
- Multi-turn conversation support
- Fallback handling for out-of-scope queries

---

## Architecture

```
┌────────────────────────────────────────────────────────────┐
│                        User Interface                      │
│                   (Voice/Text Input Layer)                 │
└───────────────────────────┬────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────┐
│                   VENIC Dialogue Management                │
│                         (Rasa Core)                        │
├────────────────────────────────────────────────────────────┤
│  ┌──────────────────┐       ┌──────────────────────────┐   │
│  │   NLU Pipeline   │       │   Dialogue Policies      │   │
│  │  - Tokenization  │       │  - Memoization Policy    │   │
│  │  - Featurization │◄─────►│  - Rule Policy           │   │
│  │  - Intent Class. │       │  - TED Policy            │   │
│  │  - Entity Extract│       │  - Fallback Classifier   │   │
│  └──────────────────┘       └──────────────────────────┘   │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Domain & Training Data                  │  │
│  │  - Intents (200+)  - Entities  - Responses           │  │
│  │  - Stories         - Rules     - Slots               │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────────┬────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Action Server / Backend                  │
│               (IDE Integration / Command Execution)         │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

- **Framework**: Rasa 3.0.8
- **Language**: Python 3.7.7
- **NLU Pipeline**: WhitespaceTokenizer, DIETClassifier, EntitySynonymMapper
- **Policies**: MemoizationPolicy, RulePolicy, TEDPolicy, UnexpecTEDIntentPolicy
- **Containerization**: Docker
- **Deployment**: Okteto, Azure Kubernetes Service (AKS)
- **CI/CD**: GitHub Actions
- **Development Tools**: Jupyter Notebooks for training and analysis

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python**: 3.7.7 or compatible version
- **pip**: Latest version
- **Docker**: (Optional) For containerized deployment
- **Git**: For version control
- **Rasa**: 3.0.8 (will be installed via pip)

---

## Installation

### Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/paradocx96/venic-dm.git
cd venic-dm
```

2. **Install Rasa**

```bash
pip install rasa==3.0.8
```

3. **Verify installation**

```bash
rasa --version
```

### Docker Setup

1. **Build the Docker image**

```bash
docker build -t venic-dm:latest .
```

2. **Run using Docker Compose**

```bash
docker-compose up
```

The Rasa server will be available at `http://localhost:5006`

---

## Usage

### Training the Model

Train the Rasa model with your training data:

```bash
rasa train
```

This will create a new model in the `models/` directory.

### Running the Server

Start the Rasa server with API enabled:

```bash
rasa run --enable-api --cors "*" --debug
```

Default port: `5005`

### Interactive Testing

Test the model interactively in the command line:

```bash
rasa shell
```

### Using the REST API

Send a message to the bot:

```bash
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "sender": "user",
    "message": "create a class named Student"
  }'
```

---

## Project Structure

```
venic-dm/
├── actions/                            # Custom Rasa actions
│   ├── __init__.py
│   └── actions.py                      # Custom action implementations
├── data/                               # Training data
│   ├── nlu.yml                         # NLU training examples
│   ├── stories.yml                     # Conversation stories
│   └── rules.yml                       # Conversation rules
├── dataset_generate/                   # Dataset generation tools
│   ├── data_nlu/                       # Organized NLU data by category
│   │   ├── GIT-Command/                # Git-related intents
│   │   ├── IDE-Command/                # IDE operation intents
│   │   ├── Java-Command/               # Java programming intents
│   │   ├── Other-Error/                # Error handling intents
│   │   └── data_story/                 # Story templates
│   ├── text_generate.py                # Script for generating training data
│   └── result_inform*.yml              # Generated data samples
├── models/                             # Trained Rasa models (generated)
├── notebooks/                          # Jupyter notebooks
│   ├── Rasa_Model_Train_Final.ipynb
│   ├── Google_Colab_Testing_v*.ipynb
│   └── Google_Colab_Train.ipynb
├── results/                            # Model evaluation results
│   └── [timestamp]/                    # Timestamped test results
│       ├── intent_confusion_matrix.png
│       ├── intent_report.json
│       ├── DIETClassifier_*.png
│       └── TEDPolicy_*.png
├── tests/                              # Test stories
│   └── test_stories.yml
├── .github/                            # GitHub Actions workflows
│   └── workflows/
│       ├── docker-image.yml
│       └── deploy-aks.yml
├── config.yml                          # Rasa NLU and Core configuration
├── domain.yml                          # Domain file (intents, entities, responses)
├── credentials.yml                     # Channel credentials
├── endpoints.yml                       # Endpoint configuration
├── Dockerfile                          # Docker image definition
├── docker-compose.yml                  # Docker Compose configuration
├── okteto.yml                          # Okteto deployment configuration
└── README.md                           # Project documentation
```

---

## Configuration

### config.yml

Defines the NLU pipeline and dialogue policies. The default configuration uses:

- **NLU Pipeline**: Optimized for English language processing
- **Dialogue Policies**: Combination of rule-based and machine learning policies

### domain.yml

Contains:
- **Intents**: 200+ intents for programming, IDE, and Git commands
- **Entities**: name, type, process, number, message
- **Slots**: Context storage for conversation management
- **Responses**: Templated responses for each intent

### endpoints.yml

Configures:
- Action server endpoint
- Tracker store
- Event broker

---

## Training the Model

### Using Command Line

```bash
# Train a new model
rasa train

# Train NLU only
rasa train nlu

# Train Core only
rasa train core
```

### Using Jupyter Notebooks

Training notebooks are provided in the `notebooks/` directory:

1. **Rasa_Model_Train_Final.ipynb**: Complete training pipeline
2. **Google_Colab_Train.ipynb**: Training on Google Colab with GPU support

### Training Data Organization

Training data is organized by command type:

- **GIT-Command**: Git operations
- **IDE-Command**: IDE interactions (cursor, file, font, project, statement)
- **Java-Command**: Java language constructs (30+ categories)
- **Other-Error**: Error handling and common queries

---

## Testing

### Interactive Testing

```bash
rasa shell
```

### Test Stories

Run automated tests using test stories:

```bash
rasa test
```

Results are saved to the `results/` directory with:
- Confusion matrices
- Classification reports
- Failed test stories
- Precision, recall, and F1 scores

### Using Jupyter Notebooks

Testing notebooks are available:

- **Google_Colab_Testing_v1.ipynb**: Basic model testing
- **Google_Colab_Testing_v2.ipynb**: Enhanced testing with metrics
- **Google_Colab_Testing_v3.ipynb**: Comprehensive evaluation

---

## Deployment

### Local Deployment

```bash
rasa run --enable-api --cors "*" -p 5005
```

### Docker Deployment

```bash
docker-compose up -d
```

### Okteto Cloud Deployment

The project includes `okteto.yml` for deployment to Okteto Cloud:

```bash
okteto deploy
```

### Azure Kubernetes Service (AKS)

GitHub Actions workflow is configured for automated deployment to AKS:

- **Workflow**: `.github/workflows/deploy-aks.yml`
- **Trigger**: Push to main branch
- **Steps**: Build Docker image → Push to registry → Deploy to AKS

---

## API Endpoints

### Local Development

| Endpoint | URL |
|----------|-----|
| Localhost | `http://localhost:5005` |

### Production

| Endpoint | URL |
|----------|-----|
| Okteto Cloud | `https://rasa-paradocx96.cloud.okteto.net` |

### REST API

**Send Message**
```
POST /webhooks/rest/webhook
Content-Type: application/json

{
  "sender": "user_id",
  "message": "create a class named Student"
}
```

**Response**
```json
[
  {
    "recipient_id": "user_id",
    "text": "Student class created"
  }
]
```

---

## Dataset Generation

The `dataset_generate/` directory contains tools for generating training data:

### text_generate.py

Script for automated generation of NLU training examples:

```bash
cd dataset_generate
python text_generate.py
```

### Data Organization

Training data is modularized by command type for easier maintenance and extension:

- Each category has dedicated YAML files
- Examples follow consistent formatting
- Entity annotations are clearly marked

---

## Model Evaluation

### Evaluation Metrics

Model performance is tracked using:

- **Intent Classification**: Precision, recall, F1-score
- **Entity Extraction**: Exact match accuracy
- **Dialogue Prediction**: Story success rate
- **Confusion Matrices**: Visual representation of misclassifications

### Latest Results

Results are stored in timestamped directories under `results/`:

```
results/
└── 220817 2254/
    ├── intent_confusion_matrix.png     # Intent classification visualization
    ├── intent_report.json              # Detailed metrics
    ├── DIETClassifier_report.json      # Entity extraction performance
    ├── TEDPolicy_report.json           # Dialogue policy performance
    └── failed_test_stories.yml         # Stories that failed testing
```

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add: Description of your feature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow Rasa best practices for dialogue design
- Add test stories for new intents
- Update domain.yml with new intents and responses
- Document new features in the README
- Ensure all tests pass before submitting PR

---

## License

This project is part of the VENIC system. Please refer to the repository for license information.

---

## Contact

**Website**: [https://venic.io](https://venic.io)

**GitHub Repository**: [https://github.com/paradocx96/venic-dm](https://github.com/paradocx96/venic-dm)

**Author**: [paradocx96](https://github.com/paradocx96)

---

## Acknowledgments

- Built with [Rasa Open Source](https://rasa.com/)
- Powered by Python and modern NLU technologies
- Deployed on Okteto Cloud and Azure Kubernetes Service

---

<div align="center">

**Made with ❤️ by [paradocx96](https://github.com/paradocx96)**

[Report Bug](https://github.com/paradocx96/venic-dm/issues) · [Request Feature](https://github.com/paradocx96/venic-dm/issues)

[Back to Top](#venic---dialogue-management)

</div>
