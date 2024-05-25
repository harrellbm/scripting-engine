# SPDX-FileCopyrightText: 2024-present harrellbm <brendenharrell1@gmail.com>
#
# SPDX-License-Identifier: MIT
# Main entry point for pepper-x v.2 engine
import subprocess
from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.suggester import SuggestFromList
from textual.widgets import Button, Footer, Header, Static, Input, RichLog
from rich.text import Text
from rich.rule import Rule
from __about__ import __version__ 

savedComms = ["dkron start", "dkron status"]
warning_color = "bright_red"
success_color = "bright_green"

class CommandInput(Static):
    """Reusable single line command input widget"""
    def compose(self) -> ComposeResult:
        """Create child widgets of command input."""
        yield Input(id="commandIn", placeholder="Enter Command", suggester=SuggestFromList(savedComms, case_sensitive=False))
        yield Button("Run", id="run")

class CommandWindow(Static):
    """A widget window that accepts a command and then prints its output after running."""
    def run_command(self, command: str)-> subprocess.CompletedProcess:
        """Run the given command in the shell and return output"""
        '''result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result'''
        command_log = self.query_one(RichLog)
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        while True:
            output = proc.stdout.readline()
            error = proc.stderr.readline()
            if output == '' and error == '' and proc.poll() is not None:
                break
            if output:
                command_log.write(output.strip())
            if error:#TODO:possibly add so styling to error message
                command_log.write(error.strip())
        rc = proc.poll()
        command_log.write(f"Return Code: {rc}")
        command_log.write(Rule(characters="^"))

    
    def clean_command(self, command: str)-> str:
        """Strip the given command of any stray whitespace"""
        cleanComm = command.lstrip().rstrip()
        return cleanComm
    
    def render_result(self, result: subprocess.CompletedProcess) -> None:
        """Render returned result using Rich styles function"""
        command_log = self.query_one(RichLog)
        args = Text("Command: ")
        args.append(result.args)
        command_log.write(args)
        
        exit = Text("Exit Code: ")
        exit.append(str(result.returncode))
        command_log.write(exit)
        
        stdout = Text(result.stdout)
        stdout.stylize(success_color)
        command_log.write(stdout)
        
        stderr = Text(result.stderr)
        stderr.stylize(warning_color)
        command_log.write(stderr)
        command_log.write(Rule(characters="^"))
    
    def on_input_submitted(self, message: Input.Submitted) -> None:
        """Event handler called when enter key is pushed and input is in focus."""
        command = self.clean_command(message.value)
        result = self.run_command(command)
        #self.render_result(result)
            
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when the run button is pressed."""
        if event.button.id == "run":
            commandIn = self.query_one('#commandIn')
            command = self.clean_command(commandIn.value)
            result = self.run_command(command)
            #self.render_result(result)
             
    def compose(self) -> ComposeResult:
        "TODO: Implement varibles for output styling"
        """Create child widgets of command input."""
        yield CommandInput()
        yield RichLog(highlight=True, markup=True)
            
class PepperXApp(App):
    """A Scripting Engine to serve up Spicy workflows."""
    CSS_PATH = "cssMain.tcss"
    BINDINGS = [Binding(key="ctrl + c", action="quit", description="Quit the app"),
                Binding(key="d", action="toggle_dark", description="Toggle dark mode")]
    
    def on_mount(self) -> None:
        self.title = "Pepper-X Engine"
        self.sub_title = __version__

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield CommandWindow()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

def main():
    app = PepperXApp()
    app.run()
    
if __name__ == "__main__":
    main()