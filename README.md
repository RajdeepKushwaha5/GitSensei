# GitSensei 🤖# GitSensei 🤖# GitSensei 🤖



*Your AI GitHub Assistant - Ask questions about GitHub repositories and get intelligent answers powered by advanced AI*



[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)*Your AI GitHub Assistant - Ask questions about GitHub repositories and get intelligent answers powered by advanced AI**Your AI GitHub Assistant - Ask questions about GitHub repositories and get intelligent answers powered by advanced AI*

[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)

[![Gemini AI](https://img.shields.io/badge/Gemini-2.0--flash-orange.svg)](https://ai.google.dev/)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)

## 📋 Overview

[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)

GitSensei is an intelligent AI-powered assistant that helps developers understand and interact with GitHub repositories. Using advanced natural language processing and hybrid search capabilities, GitSensei can answer questions about repository content, provide code explanations, and assist with development workflows.

[![Gemini AI](https://img.shields.io/badge/Gemini-2.0--flash-orange.svg)](https://ai.google.dev/)[![Gemini AI](https://img.shields.io/badge/Gemini-2.0--flash-orange.svg)](https://ai.google.dev/)

### Key Features

- **🤖 AI-Powered Q&A**: Get intelligent answers about repository content using Google Gemini AI[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

- **🔍 Hybrid Search**: Combines text-based and semantic search for accurate results

- **💬 Interactive Chat**: User-friendly Streamlit web interface

- **📊 Repository Analysis**: Indexes and analyzes GitHub repository data

- **🔧 CLI & Web Interfaces**: Choose between command-line or graphical interface## 📋 Overview## 📋 Overview

- **📝 Comprehensive Logging**: Track interactions and performance metrics

- **🛡️ Error Handling**: Robust error handling with user-friendly messages



### Target AudienceGitSensei is an intelligent AI-powered assistant that helps developers understand and interact with GitHub repositories. Using advanced natural language processing and hybrid search capabilities, GitSensei can answer questions about repository content, provide code explanations, and assist with development workflows.GitSensei is an intelligent AI-powered assistant that helps developers understand and interact with GitHub repositories. Using advanced natural language processing and hybrid search capabilities, GitSensei can answer questions about repository content, provide code explanations, and assist with development workflows.

- **Developers** looking to understand large codebases quickly

- **Open Source Contributors** exploring new projects

- **Students** learning from real-world code examples

- **Teams** needing quick answers about their repositories### Key Features### Key Features



## 🚀 Installation- **🤖 AI-Powered Q&A**: Get intelligent answers about repository content using Google Gemini AI- **🤖 AI-Powered Q&A**: Get intelligent answers about repository content using Google Gemini AI



### Prerequisites- **🔍 Hybrid Search**: Combines text-based and semantic search for accurate results- **🔍 Hybrid Search**: Combines text-based and semantic search for accurate results

- Python 3.13 or higher

- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))- **💬 Interactive Chat**: User-friendly Streamlit web interface- **💬 Interactive Chat**: User-friendly Streamlit web interface



### Step-by-Step Setup- **📊 Repository Analysis**: Indexes and analyzes GitHub repository data- **📊 Repository Analysis**: Indexes and analyzes GitHub repository data



1. **Clone the repository**- **🔧 CLI & Web Interfaces**: Choose between command-line or graphical interface- **🔧 CLI & Web Interfaces**: Choose between command-line or graphical interface

   ```bash

   git clone https://github.com/RajdeepKushwaha5/GitSensei.git- **📝 Comprehensive Logging**: Track interactions and performance metrics- **📝 Comprehensive Logging**: Track interactions and performance metrics

   cd GitSensei

   ```- **🛡️ Error Handling**: Robust error handling with user-friendly messages- **🛡️ Error Handling**: Robust error handling with user-friendly messages



2. **Install dependencies**

   ```bash

   # Using uv (recommended)### Target Audience### Target Audience

   uv sync

- **Developers** looking to understand large codebases quickly- **Developers** looking to understand large codebases quickly

   # Or using pip

   pip install -r requirements.txt- **Open Source Contributors** exploring new projects- **Open Source Contributors** exploring new projects

   ```

- **Students** learning from real-world code examples- **Students** learning from real-world code examples

3. **Set up environment variables**

- **Teams** needing quick answers about their repositories- **Teams** needing quick answers about their repositories

   Create a `.env` file in the project root:

   ```bash

   GOOGLE_API_KEY=your_gemini_api_key_here

   # Optional: GEMINI_API_KEY=your_backup_key_here## 🚀 Installation## 🚀 Installation

   ```



4. **Run the application**

### Prerequisites### Prerequisites

   **Web Interface (Recommended):**

   ```bash- Python 3.13 or higher- Python 3.13 or higher

   streamlit run app.py

   ```- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

   Open http://localhost:8501 in your browser



   **Command Line Interface:**

   ```bash### Step-by-Step Setup### Step-by-Step Setup

   python main.py

   ```



## 🎮 Usage1. **Clone the repository**1. **Clone the repository**



### Web Interface   ```bash   ```bash

The Streamlit app provides an intuitive chat interface where you can:

- Ask questions about GitHub repositories   git clone https://github.com/RajdeepKushwaha5/GitSensei.git   git clone https://github.com/RajdeepKushwaha5/GitSensei.git

- Get AI-powered explanations and code insights

- View conversation history   cd GitSensei   cd GitSensei

- Access comprehensive error handling

   ```   ```

**Example Questions:**

- "How do I set up a Kafka producer in Python?"

- "What are the best practices for error handling?"

- "Explain the repository structure and main components"2. **Install dependencies**2. **Install dependencies**



### Command Line Interface   ```bash   ```bash

For programmatic or headless usage:

   # Using uv (recommended)   # Using uv (recommended)

```bash

python main.py   uv sync   uv sync

```



Then type your questions interactively. Type "stop" to exit.

   # Or using pip   # Or using pip

### Programmatic Usage

   pip install -r requirements.txt   pip install -r requirements.txt

```python

import asyncio   ```   ```

from ingest import index_data

from search_agent import init_agent



# Initialize the system3. **Set up environment variables**3. **Set up environment variables**

index = index_data("DataTalksClub", "faq")  # Replace with your repo

agent = init_agent(index, "DataTalksClub", "faq")



# Ask questions   Create a `.env` file in the project root:   Create a `.env` file in the project root:

async def ask_question(question):

    response = await agent.run(user_prompt=question)   ```bash   ```bash

    return response.output

   GOOGLE_API_KEY=your_gemini_api_key_here   GOOGLE_API_KEY=your_gemini_api_key_here

# Example

answer = asyncio.run(ask_question("How do I run Kafka with Python?"))   # Optional: GEMINI_API_KEY=your_backup_key_here   # Optional: GEMINI_API_KEY=your_backup_key_here

print(answer)

```   ```   ```



### Configuration



**Environment Variables:**4. **Run the application**4. **Run the application**

- `GOOGLE_API_KEY`: Primary Gemini API key (required)

- `GEMINI_API_KEY`: Backup API key (optional)

- `LOGS_DIRECTORY`: Custom logs directory (default: "logs")

   **Web Interface (Recommended):**   **Web Interface (Recommended):**

**Repository Configuration:**

Edit the repository settings in `app.py` or `main.py`:   ```bash   ```bash

```python

REPO_OWNER = "your-org"   streamlit run app.py   streamlit run app.py

REPO_NAME = "your-repo"

```   ```   ```



## 📁 Project Structure   Open http://localhost:8501 in your browser   Open http://localhost:8501 in your browser



```

gitsensei/

├── app.py                 # Streamlit web application   **Command Line Interface:**   **Command Line Interface:**

├── main.py               # Command-line interface

├── ingest.py             # Data ingestion and indexing   ```bash   ```bash

├── search_agent.py       # Pydantic AI agent configuration

├── search_tools.py       # Search functionality and tools   python main.py   python main.py

├── logs.py               # Logging utilities

├── pyproject.toml        # Project configuration and dependencies   ```   ```

├── requirements.txt      # Alternative dependency management

├── .env                  # Environment variables (create this)

├── src/                  # Core modules

│   ├── __init__.py## 🎮 Usage## 🎮 Usage

│   ├── agent_logic.py    # Agent implementation

│   ├── data_processing.py # Data processing utilities

│   ├── evaluation.py     # Evaluation and testing

│   ├── logging_utils.py  # Logging utilities### Web Interface### Web Interface

│   └── search_engine.py  # Search engine implementation

├── tests/                # Test suiteThe Streamlit app provides an intuitive chat interface where you can:The Streamlit app provides an intuitive chat interface where you can:

│   ├── __init__.py

│   ├── run_tests.py      # Test runner- Ask questions about GitHub repositories- Ask questions about GitHub repositories

│   ├── test_*.py         # Individual test files

├── logs/                 # Generated log files- Get AI-powered explanations and code insights- Get AI-powered explanations and code insights

└── __pycache__/          # Python cache (generated)

```- View conversation history- View conversation history



### Key Components- Access comprehensive error handling- Access comprehensive error handling



- **`app.py`**: Main Streamlit application with chat interface

- **`search_agent.py`**: AI agent configuration using Pydantic AI

- **`ingest.py`**: Repository data loading and text indexing**Example Questions:****Example Questions:**

- **`search_tools.py`**: Search tools for the AI agent

- **`src/`**: Core business logic modules- "How do I set up a Kafka producer in Python?"- "How do I set up a Kafka producer in Python?"

- **`tests/`**: Comprehensive test suite

- "What are the best practices for error handling?"- "What are the best practices for error handling?"

## 🛠️ Technologies Used

- "Explain the repository structure and main components"- "Explain the repository structure and main components"

### Core Dependencies

- **[Pydantic AI](https://ai.pydantic.dev/)**: AI agent framework with tool calling

- **[Google Gemini AI](https://ai.google.dev/)**: Large language model for responses

- **[Streamlit](https://streamlit.io/)**: Web application framework### Command Line Interface### Command Line Interface

- **[minsearch](https://github.com/alexeygrigorev/minsearch)**: Lightweight text search engine

- **[python-frontmatter](https://github.com/jonbeebe/frontmatter)**: YAML frontmatter parsingFor programmatic or headless usage:For programmatic or headless usage:



### Development Tools

- **Python 3.13+**: Core programming language

- **uv**: Fast Python package manager```bash```bash

- **pytest**: Testing framework

- **Jupyter**: Interactive development notebookspython main.pypython main.py



### Infrastructure``````

- **GitHub API**: Repository data access

- **Environment Variables**: Configuration management

- **JSON Logging**: Structured interaction logging

Then type your questions interactively. Type "stop" to exit.Then type your questions interactively. Type "stop" to exit.

## 🤝 Contributing



We welcome contributions! Please follow these guidelines:

### Programmatic Usage### Programmatic Usage

### Development Setup

1. Fork the repository

2. Create a feature branch: `git checkout -b feature/your-feature`

3. Install development dependencies: `uv sync --group dev````python```python

4. Run tests: `python tests/run_tests.py`

import asyncioimport asyncio

### Guidelines

- **Code Style**: Follow PEP 8 standardsfrom ingest import index_datafrom ingest import index_data

- **Testing**: Add tests for new features

- **Documentation**: Update README for significant changesfrom search_agent import init_agentfrom search_agent import init_agent

- **Commits**: Use clear, descriptive commit messages



### Pull Request Process

1. Ensure all tests pass# Initialize the system# Initialize the system

2. Update documentation if needed

3. Create a pull request with a clear descriptionindex = index_data("DataTalksClub", "faq")  # Replace with your repoindex = index_data("DataTalksClub", "faq")  # Replace with your repo

4. Wait for review and address feedback

agent = init_agent(index, "DataTalksClub", "faq")agent = init_agent(index, "DataTalksClub", "faq")

## 📄 License



This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

# Ask questions# Ask questions

The MIT License allows for:

- ✅ Commercial useasync def ask_question(question):async def ask_question(question):

- ✅ Modification

- ✅ Distribution    response = await agent.run(user_prompt=question)    response = await agent.run(user_prompt=question)

- ✅ Private use

- ⚠️ No liability or warranty    return response.output    return response.output



## 🙏 Acknowledgments



### Core Technologies# Example# Example

- **Google Gemini AI**: For providing powerful language model capabilities

- **Pydantic AI**: For the excellent agent frameworkanswer = asyncio.run(ask_question("How do I run Kafka with Python?"))answer = asyncio.run(ask_question("How do I run Kafka with Python?"))

- **Streamlit**: For the intuitive web application framework

- **minsearch**: For efficient text search functionalityprint(answer)print(answer)



### Inspiration & Resources``````

- **DataTalksClub**: For the comprehensive FAQ repository used in demos

- **Open Source Community**: For the amazing tools and libraries

- **AI Research Community**: For advancing the field of AI assistants

### Configuration### Configuration

### Special Thanks

- Built with ❤️ for developers who want to understand codebases faster

- Special acknowledgment to the AI agent development community

**Environment Variables:****Environment Variables:**

## 📞 Contact & Support

- `GOOGLE_API_KEY`: Primary Gemini API key (required)- `GOOGLE_API_KEY`: Primary Gemini API key (required)

### Issues & Bug Reports

- **GitHub Issues**: [Report bugs or request features](https://github.com/RajdeepKushwaha5/GitSensei/issues)- `GEMINI_API_KEY`: Backup API key (optional)- `GEMINI_API_KEY`: Backup API key (optional)

- **Security Issues**: Please email security concerns directly

- `LOGS_DIRECTORY`: Custom logs directory (default: "logs")- `LOGS_DIRECTORY`: Custom logs directory (default: "logs")

### Questions & Discussions

- **GitHub Discussions**: [Ask questions and join discussions](https://github.com/RajdeepKushwaha5/GitSensei/discussions)

- **Documentation**: Check this README and inline code documentation

**Repository Configuration:****Repository Configuration:**

### Author

**Rajdeep Kushwaha**Edit the repository settings in `app.py` or `main.py`:Edit the repository settings in `app.py` or `main.py`:

- GitHub: [@RajdeepKushwaha5](https://github.com/RajdeepKushwaha5)

- Project Repository: [GitSensei](https://github.com/RajdeepKushwaha5/GitSensei)```python```python



---REPO_OWNER = "your-org"REPO_OWNER = "your-org"



**Built with ❤️ for developers, by developers**REPO_NAME = "your-repo"REPO_NAME = "your-repo"



*Transform how you understand and interact with GitHub repositories* 🚀``````



## 📁 Project Structure## 📁 Project Structure



``````

gitsensei/gitsensei/

├── app.py                 # Streamlit web application├── app.py                 # Streamlit web application

├── main.py               # Command-line interface├── main.py               # Command-line interface

├── ingest.py             # Data ingestion and indexing├── ingest.py             # Data ingestion and indexing

├── search_agent.py       # Pydantic AI agent configuration├── search_agent.py       # Pydantic AI agent configuration

├── search_tools.py       # Search functionality and tools├── search_tools.py       # Search functionality and tools

├── logs.py               # Logging utilities├── logs.py               # Logging utilities

├── pyproject.toml        # Project configuration and dependencies├── pyproject.toml        # Project configuration and dependencies

├── requirements.txt      # Alternative dependency management├── requirements.txt      # Alternative dependency management

├── .env                  # Environment variables (create this)├── .env                  # Environment variables (create this)

├── src/                  # Core modules├── src/                  # Core modules

│   ├── __init__.py│   ├── __init__.py

│   ├── agent_logic.py    # Agent implementation│   ├── agent_logic.py    # Agent implementation

│   ├── data_processing.py # Data processing utilities│   ├── data_processing.py # Data processing utilities

│   ├── evaluation.py     # Evaluation and testing│   ├── evaluation.py     # Evaluation and testing

│   ├── logging_utils.py  # Logging utilities│   ├── logging_utils.py  # Logging utilities

│   └── search_engine.py  # Search engine implementation│   └── search_engine.py  # Search engine implementation

├── tests/                # Test suite├── tests/                # Test suite

│   ├── __init__.py│   ├── __init__.py

│   ├── run_tests.py      # Test runner│   ├── run_tests.py      # Test runner

│   ├── test_*.py         # Individual test files│   ├── test_*.py         # Individual test files

├── logs/                 # Generated log files├── logs/                 # Generated log files

└── __pycache__/          # Python cache (generated)└── __pycache__/          # Python cache (generated)

``````



### Key Components### Key Components



- **`app.py`**: Main Streamlit application with chat interface- **`app.py`**: Main Streamlit application with chat interface

- **`search_agent.py`**: AI agent configuration using Pydantic AI- **`search_agent.py`**: AI agent configuration using Pydantic AI

- **`ingest.py`**: Repository data loading and text indexing- **`ingest.py`**: Repository data loading and text indexing

- **`search_tools.py`**: Search tools for the AI agent- **`search_tools.py`**: Search tools for the AI agent

- **`src/`**: Core business logic modules- **`src/`**: Core business logic modules

- **`tests/`**: Comprehensive test suite- **`tests/`**: Comprehensive test suite



## 🛠️ Technologies Used## 🛠️ Technologies Used



### Core Dependencies### Core Dependencies

- **[Pydantic AI](https://ai.pydantic.dev/)**: AI agent framework with tool calling- **[Pydantic AI](https://ai.pydantic.dev/)**: AI agent framework with tool calling

- **[Google Gemini AI](https://ai.google.dev/)**: Large language model for responses- **[Google Gemini AI](https://ai.google.dev/)**: Large language model for responses

- **[Streamlit](https://streamlit.io/)**: Web application framework- **[Streamlit](https://streamlit.io/)**: Web application framework

- **[minsearch](https://github.com/alexeygrigorev/minsearch)**: Lightweight text search engine- **[minsearch](https://github.com/alexeygrigorev/minsearch)**: Lightweight text search engine

- **[python-frontmatter](https://github.com/jonbeebe/frontmatter)**: YAML frontmatter parsing- **[python-frontmatter](https://github.com/jonbeebe/frontmatter)**: YAML frontmatter parsing



### Development Tools### Development Tools

- **Python 3.13+**: Core programming language- **Python 3.13+**: Core programming language

- **uv**: Fast Python package manager- **uv**: Fast Python package manager

- **pytest**: Testing framework- **pytest**: Testing framework

- **Jupyter**: Interactive development notebooks- **Jupyter**: Interactive development notebooks



### Infrastructure### Infrastructure

- **GitHub API**: Repository data access- **GitHub API**: Repository data access

- **Environment Variables**: Configuration management- **Environment Variables**: Configuration management

- **JSON Logging**: Structured interaction logging- **JSON Logging**: Structured interaction logging



## 🤝 Contributing## 🤝 Contributing



We welcome contributions! Please follow these guidelines:We welcome contributions! Please follow these guidelines:



### Development Setup### Development Setup

1. Fork the repository1. Fork the repository

2. Create a feature branch: `git checkout -b feature/your-feature`2. Create a feature branch: `git checkout -b feature/your-feature`

3. Install development dependencies: `uv sync --group dev`3. Install development dependencies: `uv sync --group dev`

4. Run tests: `python tests/run_tests.py`4. Run tests: `python tests/run_tests.py`



### Guidelines### Guidelines

- **Code Style**: Follow PEP 8 standards- **Code Style**: Follow PEP 8 standards

- **Testing**: Add tests for new features- **Testing**: Add tests for new features

- **Documentation**: Update README for significant changes- **Documentation**: Update README for significant changes

- **Commits**: Use clear, descriptive commit messages- **Commits**: Use clear, descriptive commit messages



### Pull Request Process### Pull Request Process

1. Ensure all tests pass1. Ensure all tests pass

2. Update documentation if needed2. Update documentation if needed

3. Create a pull request with a clear description3. Create a pull request with a clear description

4. Wait for review and address feedback4. Wait for review and address feedback



## 📄 License## 📄 License



This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.



The MIT License allows for:The MIT License allows for:

- ✅ Commercial use- ✅ Commercial use

- ✅ Modification- ✅ Modification

- ✅ Distribution- ✅ Distribution

- ✅ Private use- ✅ Private use

- ⚠️ No liability or warranty- ⚠️ No liability or warranty



## 🙏 Acknowledgments## 🙏 Acknowledgments



### Core Technologies### Core Technologies

- **Google Gemini AI**: For providing powerful language model capabilities- **Google Gemini AI**: For providing powerful language model capabilities

- **Pydantic AI**: For the excellent agent framework- **Pydantic AI**: For the excellent agent framework

- **Streamlit**: For the intuitive web application framework- **Streamlit**: For the intuitive web application framework

- **minsearch**: For efficient text search functionality- **minsearch**: For efficient text search functionality



### Inspiration & Resources### Inspiration & Resources

- **DataTalksClub**: For the comprehensive FAQ repository used in demos- **DataTalksClub**: For the comprehensive FAQ repository used in demos

- **Open Source Community**: For the amazing tools and libraries- **Open Source Community**: For the amazing tools and libraries

- **AI Research Community**: For advancing the field of AI assistants- **AI Research Community**: For advancing the field of AI assistants



### Special Thanks### Special Thanks

- Built with ❤️ for developers who want to understand codebases faster- Built with ❤️ for developers who want to understand codebases faster

- Special acknowledgment to the AI agent development community- Special acknowledgment to the AI agent development community



## 📞 Contact & Support## 📞 Contact & Support



### Issues & Bug Reports### Issues & Bug Reports

- **GitHub Issues**: [Report bugs or request features](https://github.com/RajdeepKushwaha5/GitSensei/issues)- **GitHub Issues**: [Report bugs or request features](https://github.com/RajdeepKushwaha5/GitSensei/issues)

- **Security Issues**: Please email security concerns directly- **Security Issues**: Please email security concerns directly



### Questions & Discussions### Questions & Discussions

- **GitHub Discussions**: [Ask questions and join discussions](https://github.com/RajdeepKushwaha5/GitSensei/discussions)- **GitHub Discussions**: [Ask questions and join discussions](https://github.com/RajdeepKushwaha5/GitSensei/discussions)

- **Documentation**: Check this README and inline code documentation- **Documentation**: Check this README and inline code documentation



### Author### Author

**Rajdeep Kushwaha****Rajdeep Kushwaha**

- GitHub: [@RajdeepKushwaha5](https://github.com/RajdeepKushwaha5)- GitHub: [@RajdeepKushwaha5](https://github.com/RajdeepKushwaha5)

- Project Repository: [GitSensei](https://github.com/RajdeepKushwaha5/GitSensei)- Project Repository: [GitSensei](https://github.com/RajdeepKushwaha5/GitSensei)



------



**Built with ❤️ for developers, by developers****Built with ❤️ for developers, by developers**



*Transform how you understand and interact with GitHub repositories* 🚀*Transform how you understand and interact with GitHub repositories* 🚀