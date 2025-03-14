from devops.reflective_agent import DevOpsReflectiveAgent
import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def run_agent():
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Initialize the agent
    agent = DevOpsReflectiveAgent()
    
    print("\n🤖 DevOps AI Agent Ready!")
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            # Get user input
            question = input("\n🔍 Please enter your DevOps question:\n> ")
            
            if question.lower() == 'exit':
                print("\n👋 Goodbye!")
                break
                
            # Generate and display solution
            logger.info("Analyzing question...")
            analysis = agent.analyze_question(question)
            
            logger.info("Generating solution...")
            solution = agent.generate_solution(question)
            
            print("\n📋 Solution:")
            print(agent.explain_solution(solution))
            
            # Ask for feedback
            feedback = input("\n✨ Was this solution helpful? (y/n): ")
            if feedback.lower() == 'n':
                print("\n🔄 Please provide more context or rephrase your question for a better solution.")
                
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            print("\n❌ Something went wrong. Please try again.")

if __name__ == "__main__":
    run_agent() 