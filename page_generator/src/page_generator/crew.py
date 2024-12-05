from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import (
    SerperDevTool,
    FileReadTool,
    FileWriterTool,
    BrowserbaseLoadTool,
)


class RedditSearchTool:
    def __init__(self):
        self.name = "Reddit Search"
        self.description = "Search Reddit for discussions about specific services"


class VectorStoreTool:
    def __init__(self):
        self.name = "Vector Store"
        self.description = "Store and search vector embeddings for content similarity"


# Uncomment the following line to use an example of a custom tool
# from page_generator.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool


@CrewBase
class PageGeneratorCrew:
    """PageGenerator crew"""

    @agent
    def service_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["service_researcher"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["content_creator"],
            tools=[
                SerperDevTool(),
                RedditSearchTool(),
                FileReadTool(),
                FileWriterTool(),
            ],
            verbose=True,
        )

    @agent
    def translator(self) -> Agent:
        return Agent(
            config=self.agents_config["translator"],
            tools=[FileReadTool(), FileWriterTool()],
            verbose=True,
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_specialist"],
            tools=[
                FileReadTool(),
                FileWriterTool(),
                VectorStoreTool(),
            ],
            verbose=True,
        )

    @agent
    def service_provider_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["service_provider_researcher"],
            tools=[SerperDevTool(), BrowserbaseLoadTool()],
            verbose=True,
        )

    @task
    def identify_services(self) -> Task:
        return Task(
            config=self.tasks_config["identify_services"], agent=self.service_researcher
        )

    @task
    def create_service_content(self) -> Task:
        return Task(
            config=self.tasks_config["create_service_content"],
            agent=self.content_creator,
        )

    @task
    def translate_content(self) -> Task:
        return Task(
            config=self.tasks_config["translate_content"], agent=self.translator
        )

    @task
    def optimize_metadata(self) -> Task:
        return Task(
            config=self.tasks_config["optimize_metadata"], agent=self.seo_specialist
        )

    @task
    def create_internal_links(self) -> Task:
        return Task(
            config=self.tasks_config["create_internal_links"], agent=self.seo_specialist
        )

    @task
    def research_service_providers(self) -> Task:
        return Task(
            config=self.tasks_config["research_service_providers"],
            agent=self.service_provider_researcher,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Administrative Services content generation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            max_rpm=50,  # Limit requests per minute to avoid rate limits
            cache=True,  # Cache tool results
            full_output=True,  # Get outputs from all tasks
        )
