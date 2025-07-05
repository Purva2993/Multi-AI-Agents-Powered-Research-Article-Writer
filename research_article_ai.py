# Warning control
import warnings
warnings.filterwarnings('ignore')

# Import necessary libraries
from crewai import Agent, Task, Crew
import os
from langchain_community.chat_models import ChatOllama  # ✅ Use Ollama LLM
# ✅ Use LLaMA 3 or any available Ollama model
llm = ChatOllama(model="llama3")

# --------------------------
# Step 1: Define Agents
# --------------------------

planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory=(
        "You're working on planning a blog article about the topic: {topic}. "
        "You collect information that helps the audience learn something and make informed decisions. "
        "Your work is the basis for the Content Writer to write an article on this topic."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

writer = Agent(
    role="Content Writer",
    goal="Write a comprehensive and engaging article based on the plan provided by the Content Planner",
    backstory=(
        "You are a skilled content writer. "
        "You will write a blog article based on the plan provided by the Content Planner. "
        "Your article should be engaging, informative, and well-structured. "
        "You will also ensure that the article is factually accurate and provides value to the readers."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

editor = Agent(
    role="Content Editor",
    goal="Review and edit the article to ensure it meets quality standards",
    backstory=(
        "You are a content editor. "
        "You will review the article written by the Content Writer. "
        "Your job is to ensure that the article is well-written, engaging, and free of errors. "
        "You will also check the article for factual accuracy and ensure it meets the quality standards of the publication."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# --------------------------
# Step 2: Define Tasks
# --------------------------

plan = Task(
    description=(
        "1. Prioritize the latest trends, key players, and noteworthy news on {topic}.\n"
        "2. Identify the target audience and their pain points.\n"
        "3. Create a content outline with intro, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
    expected_output="A detailed content plan with outline, audience analysis, SEO keywords, and references.",
    agent=planner,
)

write = Task(
    description=(
        "1. Use the content plan to write a compelling blog post on {topic}.\n"
        "2. Naturally incorporate SEO keywords.\n"
        "3. Use engaging section titles.\n"
        "4. Include intro, body, and conclusion.\n"
        "5. Proofread and ensure alignment with brand voice."
    ),
    expected_output="A ready-to-publish blog post in markdown format, 2–3 paragraphs per section.",
    agent=writer,
)

edit = Task(
    description="Proofread the blog post for grammar and tone alignment with brand voice.",
    expected_output="A polished blog post in markdown format, ready for publishing.",
    agent=editor
)

# --------------------------
# Step 3: Create and Run the Crew
# --------------------------

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2  # Show detailed logs
)

'''
# Run the crew with your topic
topic = "Future of Renewable Energy"
result = crew.kickoff(inputs={"topic": topic})

# Display result in Jupyter notebook (optional)
from IPython.display import Markdown
Markdown(result)

'''
#--------------------------
# Step 4: Get Dynamic Topic Input
# --------------------------

def get_topic_from_user():
    """Get topic input from user with validation"""
    while True:
        topic = input("\n🔍 Enter the topic you want to research and write about: ").strip()
        if topic:
            return topic
        print("❌ Please enter a valid topic (cannot be empty)")

def main():
    """Main function to run the research and article writing process"""
    print("🚀 Welcome to Autonomous Research & Article Writing with AI Agents!")
    print("=" * 60)
    
    # Get dynamic topic from user
    topic = get_topic_from_user()
    
    print(f"\n📝 Starting research and article writing on: '{topic}'")
    print("⏳ This may take a few minutes...\n")
    
    try:
        # Run the crew with the dynamic topic
        result = crew.kickoff(inputs={"topic": topic})
        
        # Save result to file
        filename = f"article_{topic.replace(' ', '_').lower()}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(result))
        
        print(f"\n✅ Article successfully generated!")
        print(f"📄 Saved as: {filename}")
        print("\n" + "=" * 60)
        print("📖 GENERATED ARTICLE:")
        print("=" * 60)
        print(result)
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        print("Please try again with a different topic or check your internet connection.")

# Run the program
if __name__ == "__main__":
    main()