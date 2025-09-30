# GitSensei 🤖

*Your AI GitHub Assistant – Ask questions about GitHub repositories and get intelligent answers powered by advanced AI.*

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Gemini AI](https://img.shields.io/badge/Gemini-2.0--flash-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Overview

GitSensei is an intelligent AI-powered assistant that helps developers understand and interact with GitHub repositories. Using advanced natural language processing and hybrid search capabilities, GitSensei can answer questions about repository content, provide code explanations, and assist with development workflows.

### Key Features

* **🤖 AI-Powered Q&A**: Get intelligent answers about repository content using Google Gemini AI.
* **🔍 Hybrid Search**: Combines text-based and semantic search for accurate results.
* **💬 Interactive Chat**: User-friendly Streamlit web interface.
* **📊 Repository Analysis**: Indexes and analyzes GitHub repository data.
* **🔧 CLI & Web Interfaces**: Choose between command-line or graphical interface.
* **📝 Comprehensive Logging**: Track interactions and performance metrics.
* **🛡️ Error Handling**: Robust error handling with user-friendly messages.

### Target Audience

* **Developers** looking to understand large codebases quickly.
* **Open Source Contributors** exploring new projects.
* **Students** learning from real-world code examples.
* **Teams** needing quick answers about their repositories.

---

## 🚀 Installation

### Prerequisites

* Python 3.13 or higher
* Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Step-by-Step Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/RajdeepKushwaha5/GitSensei.git
   cd GitSensei
   ```

2. **Install dependencies**

   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:

   ```bash
   GOOGLE_API_KEY=your_gemini_api_key_here
   # Optional
   GEMINI_API_KEY=your_backup_key_here
   ```

4. **Run the application**

   **Web Interface (Recommended):**

   ```bash
   streamlit run app.py
   ```

   Open [http://localhost:8501](http://localhost:8501) in your browser.

   **Command Line Interface:**

   ```bash
   python main.py
   ```

---

## 🎮 Usage

### Web Interface

The Streamlit app provides an intuitive chat interface where you can:

* Ask questions about GitHub repositories.
* Get AI-powered explanations and code insights.
* View conversation history.
* Access comprehensive error handling.

**Example Questions:**

* "How do I set up a Kafka producer in Python?"
* "What are the best practices for error handling?"
* "Explain the repository structure and main components."

### Command Line Interface

For programmatic or headless usage:

```bash
python main.py
```

Type your questions interactively. Type `stop` to exit.

### Programmatic Usage

```python
import asyncio
from ingest import index_data
from search_agent import init_agent

# Initialize the system
index = index_data("DataTalksClub", "faq")  # Replace with your repo
agent = init_agent(index, "DataTalksClub", "faq")

async def ask_question(question):
    response = await agent.run(user_prompt=question)
    return response.output

answer = asyncio.run(ask_question("How do I run Kafka with Python?"))
print(answer)
```

---

## 📁 Project Structure

```
gitsensei/
├── app.py               # Streamlit web application
├── main.py              # Command-line interface
├── ingest.py            # Data ingestion and indexing
├── search_agent.py      # Pydantic AI agent configuration
├── search_tools.py      # Search functionality and tools
├── logs.py              # Logging utilities
├── pyproject.toml       # Project configuration and dependencies
├── requirements.txt     # Alternative dependency management
├── .env                 # Environment variables (create this)
├── src/                 # Core modules
│   ├── __init__.py
│   ├── agent_logic.py
│   ├── data_processing.py
│   ├── evaluation.py
│   ├── logging_utils.py
│   └── search_engine.py
├── tests/               # Test suite
│   ├── __init__.py
│   ├── run_tests.py
│   ├── test_*.py
├── logs/                # Generated log files
└── __pycache__/         # Python cache (generated)
```

---

## 🛠️ Technologies Used

### Core Dependencies

* **[Pydantic AI](https://ai.pydantic.dev/)** – AI agent framework with tool calling.
* **[Google Gemini AI](https://ai.google.dev/)** – Large language model for responses.
* **[Streamlit](https://streamlit.io/)** – Web application framework.
* **[minsearch](https://github.com/alexeygrigorev/minsearch)** – Lightweight text search engine.
* **[python-frontmatter](https://github.com/jonbeebe/frontmatter)** – YAML frontmatter parsing.

### Development Tools

* **Python 3.13+** – Core programming language.
* **uv** – Fast Python package manager.
* **pytest** – Testing framework.
* **Jupyter** – Interactive development notebooks.

### Infrastructure

* **GitHub API** – Repository data access.
* **Environment Variables** – Configuration management.
* **JSON Logging** – Structured interaction logging.

---

## 🤝 Contributing

We welcome contributions!

### Development Setup

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Install development dependencies:

   ```bash
   uv sync --group dev
   ```
4. Run tests:

   ```bash
   python tests/run_tests.py
   ```

### Guidelines

* **Code Style**: Follow PEP 8 standards.
* **Testing**: Add tests for new features.
* **Documentation**: Update README for significant changes.
* **Commits**: Use clear, descriptive commit messages.

### Pull Request Process

1. Ensure all tests pass.
2. Update documentation if needed.
3. Create a pull request with a clear description.
4. Wait for review and address feedback.

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

The MIT License allows for:

* ✅ Commercial use
* ✅ Modification
* ✅ Distribution
* ✅ Private use
* ⚠️ No liability or warranty

---

## 🙏 Acknowledgments

### Core Technologies

* **Google Gemini AI** – Powerful language model.
* **Pydantic AI** – Agent framework.
* **Streamlit** – Web interface framework.
* **minsearch** – Efficient text search functionality.

### Inspiration & Resources

* **DataTalksClub** – FAQ repository used in demos.
* **Open Source Community** – Amazing tools and libraries.
* **AI Research Community** – Advancing AI assistants.

### Special Thanks

* Built with ❤️ for developers who want to understand codebases faster.
* Special acknowledgment to the AI agent development community.

---

## 📞 Contact & Support

* **GitHub Issues**: [Report bugs or request features](https://github.com/RajdeepKushwaha5/GitSensei/issues)
* **GitHub Discussions**: [Ask questions and join discussions](https://github.com/RajdeepKushwaha5/GitSensei/discussions)
* **Documentation**: Check this README and inline code documentation.

### Author

**Rajdeep Kushwaha**

* GitHub: [@RajdeepKushwaha5](https://github.com/RajdeepKushwaha5)
* Repository: [GitSensei](https://github.com/RajdeepKushwaha5/GitSensei)

---

**Built with ❤️ for developers, by developers**
*Transform how you understand and interact with GitHub repositories* 🚀
