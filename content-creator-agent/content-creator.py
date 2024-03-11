import os
from crewai import Agent
from crewai import Process
from crewai import Task
from crewai import Crew

os.environ['OPENAI_API_KEY'] = ""

# Define your agents with roles and goals
boss = Agent(
    role  = 'Boss',
    goal = "Ensure the successful creation and promotion of the SEO blog post about split testing",
    backstory = "An experienced digital marketing manager who oversees content creation and strategy.",
    verbose=True,
    allow_delegation=True
)

outliner = Agent(
    role = 'Outliner',
    goal = "Create a comprehensive and engaging outline for the blog post about split testing",
    backstory = "A skilled content strategist who understands how to structure blog posts for maximum impact",
    verbose=True,
)

keyword_researcher = Agent(
    role = 'Keyword Researcher',
    goal = "Identify the best keywords to target for optimal SEO performance",
    backstory = "An SEO specilaist with expertise in Keyword reasearch and search trends.",
    verbose=True,
)

technical_seo = Agent(
    role = 'Technical SEO',
    goal = "Ensure all technical SEO aspects are optimised for the blog post",
    backstory = "An expert in SEO with focus on the technical elements that improve the search rankings.",
    verbose=True,
)

content_writer = Agent(
    role = 'Content Writer',
    goal = "Write an informative, engaging and SEO optimised blog post",
    backstory = "A Creative Writer who excels at crafting compelling content that also meets SEO guidelines.",
    verbose=True,
)

proofreader = Agent(
    role = "Proofreader",
    goal = "Ensure the blog post is free from grammatical and spelling errors",
    backstory = "A meticulous proofreader with an eye for detail and a passion for perfect grammer.",
    verbose=True,
)

editor = Agent(
    role = "Editor",
    goal = "Refine the blog post for clarity, style, and overall coherence", 
    backstory = "An experienced editor who enhances content quality and ensures it aligns with overall strategy.",
    verbose=True,
    allow_delegation=True

)

outreach_expert = Agent(
    role = "Outreach Expert",
    goal = "Indentify and suggest stratergies for promoting the blog post about split testing", 
    backstory = "A marketing specialist skilled in indetifying promotional opportunities and outreach Strategies.",
    verbose=True,
)

# Create tasks for your agent
task_oversee_project = Task(description="Oversee an entire project on split testing", agent=boss, expected_output="Generate a report")
task_manage_content_creation = Task(description="Manage the content creation process for the blog post", agent=editor, expected_output="Generate a report")

task_outline = Task(description = "Create a blog outline, the blog is about split testing", agent=outliner, expected_output="Generate a report")
task_keyword_search = Task(description = "Conduct keyword research about split testing", agent=keyword_researcher, expected_output="Generate a report")
task_technical_seo = Task(description="Advice on Technical SEO aspects about the blog post that is about split testing", agent=technical_seo, expected_output="Generate a report")
task_content_writing = Task(description="Write a blog postb about Split testing, based on the outline, it should be 1000 words long", agent=content_writer, expected_output="Generate a report")
task_proofreading = Task(description="Proofread the blog post", agent=proofreader, expected_output="Generate a report")
task_editing = Task(description="Edit the blog post", agent=editor, expected_output="Generate a report")
task_outreach = Task(description="Identify Outreach opportunities, must be relevant to the blog post topic", agent=outreach_expert, expected_output="Generate a report")
task_approve = Task(description="make sure the task is about split testing and you like the content", agent=boss, expected_output="Generate a report")

# instantiate your crew with a sequential Process
crew = Crew(
    agents = [boss, editor, outliner, keyword_researcher, technical_seo, content_writer, proofreader, outreach_expert],
    tasks = [task_oversee_project, task_manage_content_creation , task_outline, task_keyword_search, task_technical_seo, task_content_writing, task_proofreading, task_editing, task_outreach, task_approve],
    verbose=True,
    process = Process.sequential
)

result = crew.kickoff()


