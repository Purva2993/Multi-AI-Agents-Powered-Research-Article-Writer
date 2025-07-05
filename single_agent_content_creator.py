# Warning control
import warnings
warnings.filterwarnings('ignore')

# Import necessary libraries
from crewai import Agent, Task, Crew
import os
from langchain_community.chat_models import ChatOllama

# ✅ Use LLaMA 3 or any available Ollama model
llm = ChatOllama(model="llama3")

# -------------------------- 
# Single Agent Approach
# --------------------------

# Single agent that combines all three roles
unified_content_agent = Agent(
    role="Complete Content Creation Specialist",
    goal=(
        "You are a comprehensive content creation specialist who handles the entire article creation process. "
        "You must perform three distinct functions in sequence:\n"
        "1. RESEARCH & PLANNING: Plan engaging and factually accurate content on {topic}\n"
        "2. CONTENT WRITING: Write a comprehensive and engaging article based on your research\n"
        "3. EDITING & REVIEW: Review and edit the article to ensure it meets quality standards"
    ),
    backstory=(
        "You are an expert content creation specialist with expertise in research, writing, and editing. "
        "You work as a one-person editorial team, capable of:\n\n"
        
        "AS A CONTENT PLANNER:\n"
        "- You work on planning a blog article about the topic: {topic}\n"
        "- You collect information that helps the audience learn something and make informed decisions\n"
        "- You create comprehensive research and planning as the foundation for article writing\n\n"
        
        "AS A CONTENT WRITER:\n"
        "- You are a skilled content writer who transforms research into compelling articles\n"
        "- You write blog articles based on the research and planning you've completed\n"
        "- Your articles are engaging, informative, and well-structured\n"
        "- You ensure that articles are factually accurate and provide value to readers\n\n"
        
        "AS A CONTENT EDITOR:\n"
        "- You are a content editor who reviews and polishes written content\n"
        "- You ensure articles are well-written, engaging, and free of errors\n"
        "- You check for factual accuracy and ensure content meets quality standards\n"
        "- You provide the final polish for publication-ready content"
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# --------------------------
# Single Comprehensive Task
# --------------------------

complete_content_creation = Task(
    description=(
        "You must complete the entire content creation process for the topic: {topic}\n\n"
        
        "PHASE 1 - RESEARCH & PLANNING:\n"
        "1. Prioritize the latest trends, key players, and noteworthy news on {topic}\n"
        "2. Identify the target audience and their pain points\n"
        "3. Create a content outline with intro, key points, and a call to action\n"
        "4. Include SEO keywords and relevant data or sources\n\n"
        
        "PHASE 2 - CONTENT WRITING:\n"
        "1. Use your research and content plan to write a compelling blog post on {topic}\n"
        "2. Naturally incorporate SEO keywords\n"
        "3. Use engaging section titles\n"
        "4. Include intro, body, and conclusion\n"
        "5. Ensure alignment with brand voice\n\n"
        
        "PHASE 3 - EDITING & REVIEW:\n"
        "1. Proofread the blog post for grammar and readability\n"
        "2. Check tone alignment with brand voice\n"
        "3. Verify factual accuracy\n"
        "4. Ensure the article meets publication quality standards\n"
        "5. Make final polishing adjustments\n\n"
        
        "IMPORTANT: You must complete ALL three phases in sequence. "
        "Show your work for each phase clearly."
    ),
    expected_output=(
        "A complete, publication-ready article that includes:\n"
        "1. Research summary and content plan\n"
        "2. Full blog post in markdown format (2-3 paragraphs per section)\n"
        "3. Editorial review notes and final polished version\n"
        "The final output should be a polished blog post ready for publishing."
    ),
    agent=unified_content_agent,
)

# --------------------------
# Create and Run Single Agent Crew
# --------------------------

single_agent_crew = Crew(
    agents=[unified_content_agent],
    tasks=[complete_content_creation],
    verbose=2  # Show detailed logs
)

# --------------------------
# Dynamic Topic Input (Same as Multi-Agent)
# --------------------------

def get_topic_from_user():
    """Get topic input from user with validation"""
    while True:
        topic = input("\n🔍 Enter the topic you want to research and write about: ").strip()
        if topic:
            return topic
        print("❌ Please enter a valid topic (cannot be empty)")

def main():
    """Main function to run the single-agent content creation process"""
    print("🤖 Welcome to Single-Agent Content Creation System!")
    print("=" * 60)
    print("📝 This system uses ONE agent to handle research, writing, and editing")
    print("🆚 Compare this with the multi-agent system performance!")
    print("=" * 60)
    
    # Get dynamic topic from user
    topic = get_topic_from_user()
    
    print(f"\n📝 Starting single-agent content creation on: '{topic}'")
    print("⏳ This may take a few minutes...")
    print("🔄 Single agent will handle: Research → Writing → Editing")
    print()
    
    try:
        # Record start time for performance comparison
        import time
        start_time = time.time()
        
        # Run the single agent crew
        result = single_agent_crew.kickoff(inputs={"topic": topic})
        
        # Calculate processing time
        end_time = time.time()
        processing_time = round(end_time - start_time, 2)
        
        # Save result to file with clear naming
        filename = f"SINGLE_AGENT_article_{topic.replace(' ', '_').lower()}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Single-Agent Generated Article\n")
            f.write(f"**Topic:** {topic}\n")
            f.write(f"**Processing Time:** {processing_time} seconds\n")
            f.write(f"**Generated by:** Single Unified Agent\n\n")
            f.write("---\n\n")
            f.write(str(result))
        
        print(f"\n✅ Single-agent article successfully generated!")
        print(f"⏱️  Processing time: {processing_time} seconds")
        print(f"📄 Saved as: {filename}")
        print("\n" + "=" * 60)
        print("📖 SINGLE-AGENT GENERATED ARTICLE:")
        print("=" * 60)
        print(result)
        
        # Performance comparison note
        print("\n" + "=" * 60)
        print("🔬 PERFORMANCE ANALYSIS:")
        print("=" * 60)
        print("🤖 Single Agent Approach:")
        print(f"   ⏱️  Time: {processing_time} seconds")
        print("   📝 Method: One agent handling all tasks sequentially")
        print("   🧠 Cognitive Load: High (research + writing + editing)")
        print("\n💡 Now run the multi-agent version with the same topic to compare!")
        print("   Command: python research_article_ai.py")
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        print("Please try again with a different topic or check your internet connection.")

# Run the program
if __name__ == "__main__":
    main()
