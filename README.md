# MultiAI-Agents-Powered-Research-Article-Writer

A sophisticated multi-agent AI system that autonomously researches, writes, and edits professional articles on any topic using CrewAI and LLaMA 3. Features three specialized AI agents working collaboratively as a content team.
It is an AI-powered content creation system where multiple specialized agents work together to research, write, and edit professional articles on any topic. Just enter a subject and get a complete, ready-to-publish article.

## **What This Does**

Transform any topic into a professional, SEO-optimized article in minutes! This system uses three specialized AI agents that work like a real editorial team:

- **Content Planner**: Researches trends, identifies audience, creates outlines
- **Content Writer**: Writes engaging, well-structured articles  
- **Content Editor**: Polishes grammar, tone, and overall quality

##  **Key Features**

- **Multi-Agent Collaboration**: Three AI agents working as a coordinated team
- **Fully Autonomous**: Just input a topic and let the AI do the rest
- **Dynamic Content**: Real-time research and trend analysis
- **Auto-Save**: Articles saved as markdown files with topic-based naming
- **SEO Optimized**: Includes keywords and proper content structure
- **Fast Generation**: Complete articles in minutes, not hours
- **Any Topic**: Works for technology, business, health, science, and more

##  **Prerequisites**

Before running this project, make sure you have:

- **Python 3.8+** installed
- **Ollama** installed and running ([Installation Guide](https://ollama.ai))
- **LLaMA 3** model downloaded in Ollama

### Install Ollama & LLaMA 3:
```bash
# Install Ollama (macOS)
brew install ollama

# Pull LLaMA 3 model
ollama pull llama3

# Start Ollama service
ollama serve
```

## **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MultiAI-Agents-Powered-Research-Article-Writer.git
   cd MultiAI-Agents-Powered-Research-Article-Writer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv ra_env
   source ra_env/bin/activate  # On Windows: ra_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

### Quick Start
```bash
python research_article_ai.py
```

### What Happens:
1. **Enter Topic**: Program prompts for your desired article topic
2. **AI Processing**: Three agents collaborate automatically
3. **Article Generation**: Complete article created and saved
4. **File Output**: Markdown file saved (e.g., `article_ai_in_healthcare.md`)

### Example Session:
```
Welcome to Autonomous Research & Article Writing with AI Agents!
============================================================

Enter the topic you want to research and write about: Future of Electric Vehicles

Starting research and article writing on: 'Future of Electric Vehicles'
This may take a few minutes...

Article successfully generated!
Saved as: article_future_of_electric_vehicles.md
```

## **Project Structure**

```
MultiAI-Agents-Powered-Research-Article-Writer/
├── research_article_ai.py    # Main application file
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── ra_env/                  # Virtual environment
└── generated_articles/      # Output folder (created automatically)
```

## **How It Works**

### Agent Workflow:
```
User Input → Content Planner → Content Writer → Content Editor → Final Article
```

### Agent Responsibilities:

#### **Content Planner**
- Researches latest trends and key players
- Identifies target audience and pain points
- Creates detailed content outline
- Suggests SEO keywords and sources

####  **Content Writer** 
- Uses planner's research to write compelling content
- Incorporates SEO keywords naturally
- Creates engaging section titles
- Structures intro, body, and conclusion

####  **Content Editor**
- Reviews for grammar and readability
- Ensures brand voice consistency
- Performs final quality checks
- Polishes for publication

##  **Dependencies**

- `crewai` - Multi-agent AI framework
- `langchain-community` - LLM integration
- `ollama` - Local LLM hosting
- Additional dependencies in `requirements.txt`

##  **Use Cases**

- ** Blog Content**: Generate engaging blog posts for websites
- ** News Articles**: Create informative articles on current topics  
- ** Business Content**: Develop thought leadership articles
- ** Educational Materials**: Create learning resources and guides
- ** Research Reports**: Generate comprehensive topic overviews
- ** Marketing Content**: Develop SEO-optimized content for campaigns

##  **Configuration**

### Changing AI Models:
```python
# In research_article_ai.py, modify:
llm = ChatOllama(model="llama3")  # Change to your preferred model
```

### Customizing Agents:
- Edit agent roles, goals, and backstories in the code
- Modify task descriptions for different content styles
- Adjust verbosity levels and output formats

##  **Contributing**

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  **Troubleshooting**

### Common Issues:

**Ollama Connection Error:**
```bash
# Make sure Ollama is running
ollama serve

# Check if LLaMA 3 is available
ollama list
```
