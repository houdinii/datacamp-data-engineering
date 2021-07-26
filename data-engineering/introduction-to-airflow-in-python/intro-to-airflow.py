"""

HOW TO START AIRFLOW IN MY VM:
    airflow webserver
    airflow scheduler
    airflow celery worker

to stop (if a daemon):
    cat $AIRFLOW_HOME/airflow-webserver.pid
    sudo kill -9 {process_id of airflow}

Intro To Airflow
----------------

In this chapter, you’ll gain a complete introduction to the components of Apache Airflow and learn how and why you
should use them.


Introduction to Airflow
Welcome to Introduction to Airflow! I'm Mike Metzger, a Data Engineer, and I'll be your instructor while we learn the
components of Apache Airflow and why you'd want to use it. Let's get started!


What is data engineering?
Before getting into workflows and Airflow, let's discuss a bit about data engineering. While there are many specific
definitions based on context, the general meaning behind data engineering is:

    Taking any action involving data and making it a reliable, repeatable, and maintainable process.


What is a workflow?
Before we can really discuss Airflow, we need to talk about workflows. A workflow is:
+ A set of steps to accomplish a given data engineering task.
    + These can include any given task, such as:
        + downloading a file
        + copying data
        + filtering information
        + writing to a database
        + so forth.
    + Of varying levels of complexity.

Some workflows may only have 2 or 3 steps, while others consist of hundreds of components. The complexity of a workflow
is completely dependent on the needs of the user. We show an example of a possible workflow to the right. It's
important to note that we're defining a workflow here in a general data engineering sense. This is an informal
definition to introduce the concept. As you'll see later, workflow can have specific meaning within specific tools.


What is Airflow? (https://airflow.apache.org/docs/stable)
Airflow is a platform to program workflows (general), including the creation, scheduling, and monitoring of said
workflows. Airflow can use various tools and languages, but the actual workflow code is written with Python. Airflow
implements workflows as DAGs, or Directed Acyclic Graphs. We'll discuss exactly what this means throughout this course,
but for now think of it as a set of tasks and the dependencies between them. Airflow can be accessed and controlled via
code, via the command-line, or via a built-in web interface. We'll look at all these options later on.

+ Airflow is a platform to program workflows, including:
    + Creation
    + Scheduling
    + Monitoring
+ Can implement programs from any language, but workflows are written in Python.
+ Implements workflows as DAGs: Directed Acyclic Graphs
+ Accessed via code, CLI, or via web interface.


Other workflow tools
Airflow is not the only tool available for running data engineering workflows. Some other options are Spotify's Luigi,
Microsoft's SSIS, or even just Bash scripting. We'll use some Bash scripting within our Airflow usage, but otherwise
we'll focus on Airflow.


Quick introduction to DAGs
A DAG stands for a Directed Acyclic Graph. In Airflow, this represents the set of tasks that make up your workflow. It
consists of the tasks and the dependencies between tasks. DAGs are created with various details about the DAG,
including the name, start date, owner, email alerting options, etc.

A DAG stands for Directed Acyclic Graph
+ In Airflow, this represents the set of tasks that make up your workflow.
+ Consists of the tasks and the dependencies between tasks.
+ Created with various details about the DAG, including the name, start date, owner, etc.


DAG code example
We will go into further detail in the next lesson but a very simple DAG is defined using the following code. A new DAG
is created with the dag_id of etl_pipeline and a default_args dictionary containing a start_date for the DAG.
Note that within any Python code, this is referred to via the variable identifier, etl_dag, but within the Airflow
shell command, you must use the dag_id.


Running a workflow in Airflow
To get started, let's look at how to run a component of an Airflow workflow. These components are called tasks and
simply represent a portion of the workflow. We'll go into further detail in later chapters. There are several ways to
run a task, but one of the simplest is using the airflow run shell command. Airflow run takes three arguments, a
dag_id, a task_id, and a start_date.

Running a simple Airflow task:

    airflow run <dag_id> <task_id> <start_date>

All of these arguments have specific meaning and will make more sense later in the course. For our example, we'll use a
dag_id of example-etl, a task named download-file, and a start date of 2020-01-10. This task would simply download a
specific file, perhaps a daily update from a remote source. Our command as such is

        airflow run example-etl download-file 2020-01-10

This will then run the specified task within Airflow.

What is a DAG?
DAG or Directed Acyclic Graph:
+ Directed, there is an inherent flow representing dependencies between components.
+ Acyclic, does not loop/cycle/repeat.
+ Graph, the actual set of components.
+ Seen in Airflow, Apache Spark, Luigi


DAGs in Airflow:
Within Airflow, DAGs:
+ Are written in Python (but can use components written in other languages)
+ Are made up of components (typically tasks) to be executed, such as operators, sensors, etc.
+ Contain dependencies defined explicitly or implicitly.
    + ie, Copy the file to the server before trying to import it to the database service.


DAGs on the Command Line:
Using 'airflow ' command:
+ The airflow command line program contains many subcommands.
+ airflow -h for descriptions.
+ Many are related to DAGs.
+ airflow list_dags to show all recognized DAGs
"""

from airflow.models import DAG
from datetime import datetime

# A simple DAG definition
# etl_dag = DAG(
#     dag_id='etl_pipeline',
#     default_args={"start_date": "2020-01-08"}
# )


def define_a_dag():
    default_arguments = {
        'owner': 'jdoe',
        'email': 'jdoe@datacamp.com',
        'start_date': datetime(2020, 1, 20)
    }
    etl_dag = DAG('etl_workflow', default_args=default_arguments)


def main():
    pass


if __name__ == '__main__':
    main()
