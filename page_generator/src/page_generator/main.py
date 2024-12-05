#!/usr/bin/env python
import sys
from page_generator.crew import PageGeneratorCrew


def run():
    """
    Run the crew to generate content for administrative services.
    """
    inputs = {
        "country": "Spain",  # Example country
        "service": "NIE Application",  # Example service
        "current_date": "2024-03-19",  # For content creation template
    }
    try:
        crew = PageGeneratorCrew().crew()
        result = crew.kickoff(inputs=inputs)
        print("Crew execution completed successfully!")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "country": "Spain",
        "service": "NIE Application",
        "current_date": "2024-03-19",
    }
    try:
        n_iterations = int(sys.argv[1])
        filename = sys.argv[2]
        crew = PageGeneratorCrew().crew()
        result = crew.train(n_iterations=n_iterations, filename=filename, inputs=inputs)
        print(f"Training completed for {n_iterations} iterations!")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        task_id = sys.argv[1]
        crew = PageGeneratorCrew().crew()
        result = crew.replay(task_id=task_id)
        print(f"Successfully replayed task: {task_id}")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution with different models and return results.
    """
    inputs = {
        "country": "Spain",
        "service": "NIE Application",
        "current_date": "2024-03-19",
    }
    try:
        n_iterations = int(sys.argv[1])
        model_name = sys.argv[2]
        crew = PageGeneratorCrew().crew()
        result = crew.test(
            n_iterations=n_iterations, openai_model_name=model_name, inputs=inputs
        )
        print(f"Testing completed with model: {model_name}")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
