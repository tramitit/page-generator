from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import (
    SerperDevTool,
    FileReadTool,
    FileWriterTool,
)

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
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["content_creator"],
            verbose=True,
            tools=[SerperDevTool(), FileReadTool(), FileWriterTool()],
        )

    @agent
    def translator(self) -> Agent:
        return Agent(
            config=self.agents_config["translator"],
            verbose=True,
            tools=[FileReadTool(), FileWriterTool()],
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_specialist"],
            verbose=True,
            tools=[FileReadTool(), FileWriterTool()],
        )

    @agent
    def service_provider_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["service_provider_researcher"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @task
    def identify_services(self) -> Task:
        return Task(config=self.tasks_config["identify_services"])

    @task
    def create_service_content(self) -> Task:
        return Task(config=self.tasks_config["create_service_content"])

    @task
    def translate_content(self) -> Task:
        return Task(config=self.tasks_config["translate_content"])

    @task
    def optimize_metadata(self) -> Task:
        return Task(config=self.tasks_config["optimize_metadata"])

    @task
    def create_internal_links(self) -> Task:
        return Task(config=self.tasks_config["create_internal_links"])

    @task
    def research_service_providers(self) -> Task:
        return Task(config=self.tasks_config["research_service_providers"])

    @crew
    def crew(self) -> Crew:
        """Creates the Administrative Services content generation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
