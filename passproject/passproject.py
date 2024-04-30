import reflex as rx
import hashlib as hashf
import json
import jsonpickle

bg = "gray"
n=0

class State(rx.State):
    name: str
    masterpass: str 
    website: str 
    show: bool = True
    passwords = {}
    content = []
    dialog_opened: bool
    
    data_raw: str = rx.LocalStorage("{}", sync=True)
    data: dict[str, list[str]] = {}
    
    def _save_settings(self):
        print(self.data)
        self.data_raw = jsonpickle.encode(self.data)

    def load_settings(self):
        print("I am about to print")
        print(self.data_raw)
        self.data = json.loads(self.data_raw)
        del self.data['py/object']
    
        print(self.data)

    def add_record(self, name: str, website: str):
        if name in self.data:
            print("data already existed, i am appending")
            self.data[name].append(website)
        else:
            print("data did not exist before, creating new list")
            self.data[name] = [website] 
        
        print("I am about to save some data")
        self._save_settings()
            
    def delete_record(self, name: str, website: str):
        if not self.data[name]:
            return 

        self.data[name] = [site for site in self.data[name] if site != website]
        self._save_settings()
        
    
    def create_pass(self) -> None:
        # part 1 
        nonce = hashf.sha512(self.website.encode()).hexdigest()[:4] + hashf.sha512(self.name.encode()).hexdigest()[:4] + hashf.sha512(self.masterpass.encode()).hexdigest()[:4]
        self.passwords[self.website] = hashf.sha512(nonce.encode()).hexdigest()[:16].replace("0", "@").replace("e", "$").replace("1", "!")
        
        # part 2 - save it -_____-
        self.add_record(self.name, self.website)
        
    def dialog_switch(self):
        self.dialog_opened = not self.dialog_opened
        
    def generate_row(item: str):
        
        

@rx.page(route="/", title="Home")
def index():
    return rx.center(
        rx.tablet_and_desktop(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.text("ㅤㅤㅤㅤㅤㅤㅤ", align="left"),
                        rx.heading(
                            "Password Generator",  
                            size="5",
                            trim="normal", 
                            weight="bold", 
                            color_scheme="green",
                            align="left",
                            ),
                        rx.text("ㅤ" * 95 , align="center"),
                        rx.box(
                            rx.link(
                                rx.text.strong("GitHub", color_scheme="green"),
                                href="https://github.com/daesun06/projectpass",
                                color_scheme="green",
                                _hover={"cursor": "pointer"},
                                align="right", trim="normal",
                            ), margin="14x", padding="14px", border_radius="6px",
                        ),
                        rx.box(
                            rx.color_mode.button("Switch theme", color_scheme="green", size="2", variant="solid", align="right"), margin="10px", padding="10px", border_radius="5px", 
                        ),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.box(
                                    rx.button("Menu", color_scheme="green", size="2", variant="solid", align="center", trim="start", direction="column"),margin="10px", padding="10px", border_radius="5px", 
                                ),
                            ),
                            rx.menu.content(
                                rx.menu.item(rx.button("Main"), href="http://loaclhost:3000/index/", color_scheme="green"),
                                rx.menu.separator(),
                                rx.menu.item(rx.button("Table"), href="http://localhost:3000/passwords/", color_scheme="green"),
                            ),
                        ),
                        bg="black",
                        color="white",
                        height="7vh", trim="both", width="100%"
                    ),
                    rx.box("", height="30vh", bg=""),
                    rx.hstack(
                        rx.text("ㅤ" * 50),
                        rx.flex(
                            rx.text("Enter your name:", align="center", color_scheme="green"),
                            rx.hstack(
                                rx.input(on_change=State.set_name, value=State.name, color_scheme="green"),
                            ),
                            rx.text("Enter or create your master password:", align="center", color_scheme="green"),
                            rx.hstack(
                                rx.input(on_change=State.set_masterpass, value=State.masterpass, type="password", color_scheme="green"),
                            ),
                            rx.text("Enter the name of the site:", align="center", color_scheme="green"),
                            rx.input(on_change=State.set_website, value=State.website, color_scheme="green"),
                            rx.button(
                                "Create",
                                color_scheme="green",
                                on_click=State.create_pass, 
                                size="4"
                            ), 
                            rx.heading(
                                State.passwords[State.website],
                                size='8', weight="bold", align="center",
                                color='green',
                            ), align="center", direction="column",
                        ), 
                        rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
                    ),     
                ), 
            ),
            rx.box("", height="50vh", bg="bg"),
            center_content=True,
            bg="bg",
            color="gray",
            direction="column",
            align="center",
        ),
        
        
        
        rx.mobile_only(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.text("ㅤㅤㅤㅤ", align="left"),
                        rx.heading(
                            "Password Generator",  
                            size="5",
                            trim="normal", 
                            weight="bold", 
                            color_scheme="green",
                            align="left",
                            ),
                        rx.text("ㅤ" * 34 , align="center"),
                        rx.box(
                            rx.link(
                                rx.text.strong("GitHub", color_scheme="green"),
                                href="https://github.com/daesun06/projectpass",
                                color_scheme="green",
                                _hover={"cursor": "pointer"},
                                align="right", trim="normal",
                            ), margin="10x", padding="10px", border_radius="5px",
                        ),
                        rx.box(
                            rx.color_mode.button("Switch theme", color_scheme="green", size="2", variant="solid", align="right", trim="start"), margin="10px", padding="10px", border_radius="5px", 
                        ),
                        rx.text("ㅤㅤㅤㅤㅤㅤㅤ"),
                        bg="black",
                        color="white",
                        height="7vh", trim="both"
                    ),
                    rx.box("", height="15vh", bg=""),
                    rx.hstack(
                        rx.text("ㅤㅤㅤ"),
                        rx.vstack(
                            rx.flex(
                                rx.flex(
                                    rx.text("Enter your name:", align="center", color_scheme="green"),
                                    rx.hstack(
                                        rx.input(on_change=State.set_name, value=State.name, color_scheme="green"),
                                    ),
                                    rx.text("Enter or create your master password:", align="center", color_scheme="green"),
                                    rx.hstack(
                                        rx.input(on_change=State.set_masterpass, value=State.masterpass, type="password", color_scheme="green"),
                                    ),
                                    rx.text("Enter the name of the site:", align="center", color_scheme="green"),
                                    rx.input(on_change=State.set_website, value=State.website, color_scheme="green"),
                                    rx.button(
                                        "Create",
                                        color_scheme="green",
                                        on_click=State.create_pass,
                                        size="4"
                                    ), 
                                    rx.heading(
                                        State.passwords[State.website],
                                        size='8', weight="bold", align="center",
                                        color='green',
                                    ), align="center", direction="column",
                                ), 
                                rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
                            ),
                        ),
                    ),     
                ), 
            ),
            rx.box("", height="20vh", bg="bg"),
            center_content=True,
            bg="bg",
            color="gray",
            direction="column",
            align="center",
        ),
    ),

@rx.page(route="/passwords", title="Passwords", on_load=State.load_settings)
def passwords():
    return rx.tablet_and_desktop(
        rx.flex(
            rx.vstack(
                rx.hstack(
                    rx.text("ㅤㅤㅤㅤㅤㅤㅤ", align="left"),
                    rx.heading(
                        "Password Generator",  
                        size="5",
                        trim="normal", 
                        weight="bold", 
                        color_scheme="green",
                        align="left",
                        ),
                    rx.text("ㅤ" * 95 , align="center"),
                    rx.box(
                        rx.link(
                            rx.text.strong("GitHub", color_scheme="green"),
                            href="https://github.com/daesun06/projectpass",
                            color_scheme="green",
                            _hover={"cursor": "pointer"},
                            align="right", trim="normal",
                        ), margin="14x", padding="14px", border_radius="6px",
                    ),
                    rx.box(
                        rx.color_mode.button("Switch theme", color_scheme="green", size="2", variant="solid", align="right"), margin="10px", padding="10px", border_radius="5px", 
                    ),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.box(
                                rx.button("Menu", color_scheme="green", size="2", variant="solid", align="center", trim="start", direction="column"),margin="10px", padding="10px", border_radius="5px", 
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item(rx.link("Main"), href="http://loaclhost:3000/index/", color_scheme="green"),
                            rx.menu.separator(),
                            rx.menu.item(rx.link("Table"), href="http://localhost:3000/passwords/", color_scheme="green"),
                        ),
                    ),
                    bg="black",
                    color="white",
                    height="7vh", trim="both", width="100%",
                ),
                rx.box("", height="20vh", bg="bg"),
                
                rx.hstack(
                    
                    rx.text("ㅤ" * 50 , align="center"),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Name"),
                                rx.table.column_header_cell("Website"),
                                rx.table.column_header_cell("Show")
                            ),
                        ),
                        
                        rx.table.body(
                            # rx.foreach(State.data, colored_box),
                            rx.table.row(
                                rx.table.cell(State.name),
                                rx.table.cell(State.website),
                                rx.table.cell(rx.button("Show", on_click=State.dialog_switch ,color_scheme="green")),
                            ),
                        ),
                    ),
                    rx.alert_dialog.root(
                        rx.alert_dialog.content(
                            rx.alert_dialog.title("My password"),
                            rx.alert_dialog.description(
                                "Regenerate your password securely",
                            ),
                            rx.flex(
                                
                                rx.alert_dialog.cancel(
                                    rx.button("Close", on_click=State.dialog_switch),
                                ),  
                                rx.alert_dialog.cancel(
                                    rx.button("Generate"),
                                ),
                                spacing="3",
                            ),
                        ),
                        open=State.dialog_opened,
                    ),
                ),
            ),
        ),
    ),
    
app = rx.App()
# app.add_page(index)
# app.add_page(passwords, route="/passwords")
