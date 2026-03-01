import asyncio
import sys
from agent.agent import agent


async def main():
    print("Weather Clothing Agent (type 'exit' to quit)\n")
    history = [] #for in-conversation memory
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}: 
            print("Stay safe and have a great day!")
            sys.exit(0)
        history.append({"role": "user", "content": user_input})
        try:
            result = await agent.run(user_input)
            history.append({"role": "user", "content": result.output})
            print("\nRecommendation:")
            print(result.output)  
            print() 
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    asyncio.run(main())