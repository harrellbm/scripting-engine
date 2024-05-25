# Basic Usage
`pip install hatch`
`hatch env create`
`hatch shell`
`python src\pepper_x_2\main.py`


# Pepper-X Version 2
This second version of the Pepper-X data engine transforms the engine from a simple data engine into a versatile scripting engine. These scripting capabilities make it possible to run fetcher bots, trading bots, or any other scripts, arbitrary commands, or command chains in a robust and reliable system. 

This is accomplished by addressing a few of the common programming and scripting problems that make using command line tools and writing custom code difficult. By overcoming these issues the Pepper-X engine aims to open up low level scripting and coding as a powerful and useful tool that doesn’t take tons of education, reinventing the wheel, or hours of work to implement a workflow.

## Problems Pepper-X V.2 Solves:
1. Command Line tools are the most flexible, powerful and easy to implement, but suck to use. The average person doesn’t want to memorize a ton of commands just to use a tool. 
    - **Solution**: Let’s make that easier with command bookmarking and tools for working with the command line like a human. 
2. Bot loops (or execution loops in general) are hard to implement and observe. Not to mention adding tons of error prone code to loop even the simplest bot or script. 
    - **Solution**: Let’s leverage actual battle tested job scheduling and cron management tools. 
3. APIs are great over the web, but local tools tend to communicate a lot over them as well. This adds a lot of complexity in the form of api management and interfacing. In addition to the overhead of multiple servers just to communicate internally. 
    - **Solution**: Let’s go back to basics and pipe input and output using the good old fashion shell as much as possible. 
4. GUI heavy tools have a ton of overhead to integrate a new tool or technology into its workflow. 
    - **Solution**: Let’s make an interface that is as simple and powerful as possible and build it with the integration of new tools in mind. 
5. Tools change - having access to the best tools shouldn’t be a question or a painful challenge. Integration of new tools is key for the longevity of any workflow. 
    - **Solution**: If a tool exists that does a job well, let’s not reinvent the wheel. Integrate that bad boy via the command line!
6. Being locked into an ecosystem or programming language sucks. So many good tools exist across different ecosystems. 
    - **Solution**: Command line interfaces aren’t tied to a particular language. So let’s get the tools we actually want from a variety of ecosystems working together. 
7. Vendor or product lock-in serves the vendor not the user. 
    - **Solution**: Let’s future proof things as much as we can by keeping things modular and swappable.

Pepper-X V.2 is built on top of two main system components 
- **Terminal Command Piping** for connecting input and output of commands into chains.
    - https://www.geeksforgeeks.org/chaining-commands-in-linux/#
    - https://learn.microsoft.com/en-us/shows/it-ops-talk/how-to-chain-multiple-powershell-commands-on-one-line
- **Execution Loop and Scheduling via Cron Scheduler**
    - DKron will be used for now but could be any scheduler. This allows for executing a chain on any schedule while also benefiting from a scheduler's robustness.
    - https://dkron.io/docs/intro/

Because of this, the aim is for the UI to only hold bare minimum functionality so that everything else can be effectively build using command chains.

## Key Features: 
1. Accessing cli tools and command chains easily using in app command window (Use textual and rich terminal ui libraries)
2. Script and smaller chunks of code organization and execution within command chains (using Python-fire library)
3. Managing execution loops and scheduling of command chains (using DKron)
4. Writing bash and powershell scripts to handle long command chains 
5. Integrate AI via CLI (with fabric or aider for now)
6. Application packaging and dependency management (using Hatch) 

## Stuff that needs managed 
- Scripts and tools
- Commands and command chains
- Job description for scheduling 

## Command line tricks 
- Process substitution 
- Piping 

## Implementation Notes:
- Textual dev commands: 
    - `textual console` launches dev console opens the textual dev console.
    - `textual run --dev my_app.py` runs app in dev mode to connect with dev console and enable live css editing.

## Widgets:
- **CommandWindow Widget**: 
    - Basic compound widget extending the static class. Composed of an input, run button, and rich log together to send a typed command and print it’s output. 
    - Tested Commands: 
        - [x] Dir command 
        - [x] Simple echo print 
        - [ ] Read file and print to ui
        - [ ] Read from ui and store to file 
        - [ ] Start DKron server 
        - [ ] Send job to DKron server 
        - [ ] Check status of jobs on DKron server 
        - [ ] Stop DKron job
        - [ ] Kill DKron server 
