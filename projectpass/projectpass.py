import reflex as rx
import hashlib as hashf
import json
import jsonpickle

bg = "gray"

class State(rx.State):
    name: str
    masterpass: str 
    website: str 
    show: bool = True
    passwords = {}
    content = []
    dialog_opened: bool
    currentuser: str
    current_passwords: list[str]
    
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
        if self.website in self.passwords:
            self.passwords.popitem()
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
        self.masterpass=""
        
    def dialog_switch(self):
        self.dialog_opened = not self.dialog_opened
        
    def generate_row(item: str):
        return 
    
    def count_names(self):
        return self.data.keys()
    
    def setcurrentuser(self, given_user: tuple[str, list[str]]):
        self.currentuser = given_user[0]
        self.current_passwords = list(given_user[1])
    
    
    
cnames=State.count_names

def table_box(current_password: str):
    return rx.table.row(
        rx.table.cell(current_password),
        rx.table.cell(rx.button("Show", on_click=State.dialog_switch, color_scheme="green")),
    )
        
def names(cname: str):
    return rx.menu.item(rx.button(cname, on_click=State.setcurrentuser(cname)))

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
                                rx.menu.item(rx.link("Main"), on_click=rx.redirect("/"), color_scheme="green"),
                                rx.menu.separator(),
                                rx.menu.item(rx.link("Table"), on_click=rx.redirect("/passwords/"), color_scheme="green"),
                            ),
                        ),
                        bg="black",
                        color="white",
                        height="7vh", trim="both", width="100%"
                    ),
                    rx.box("", height="20vh", bg=""),
                    rx.hstack(
                        rx.text("ㅤ" * 47),
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
                            ), align="center", direction="column", spacing="2",
                        ), 
                        rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
                    ),     
                ), 
            ),
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
                        height="7vh", trim="both",
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
                                        size="4",
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
                            rx.menu.item(rx.link("Main"), on_click=rx.redirect("/"), color_scheme="green"),
                            rx.menu.separator(),
                            rx.menu.item(rx.link("Table"), on_click=rx.redirect("/passwords/"), color_scheme="green"),
                        ),
                    ),
                    bg="black",
                    color="white",
                    height="7vh", trim="both", width="100%",
                ),
                rx.box("", height="20vh", bg="bg"),
                rx.hstack(
                    rx.text("ㅤ" * 50 , align="center"),
                    rx.flex(
                        rx.menu.root(
                            rx.menu.trigger(rx.button("Pick a user", color_scheme="green")),
                            rx.menu.content(
                                rx.foreach(State.data, names), # foreach is commented, bcs it's very grumpy and always crashes, so idk how to do it else
                            )
                            # rx.menu.content(
                            #     rx.menu.item(State.name), # did it temporarily just so it works, don't know how to puy only the key
                            # ), 
                        ),
                        rx.hstack( 
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Website"),
                                        rx.table.column_header_cell("Show")
                                    ),
                                ),
                                
                                rx.table.body(
                                    rx.foreach(State.current_passwords, table_box), # foreach is commented, bcs it's very grumpy and always crashes, so idk how to do it else
                                    # rx.table.row(
                                    #     rx.table.cell(State.website), # also only temporary, have an idea how to do it, but can't make happen
                                    #     rx.table.cell(rx.button("Show", on_click=State.dialog_switch ,color_scheme="green")),
                                    # ),
                                ),
                            ),
                            rx.alert_dialog.root(
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("To show your password, regenerate it"),
                                    rx.alert_dialog.description(
                                        rx.vstack(
                                            rx.text("Enter your master password: "),
                                            rx.input(on_change=State.set_masterpass, value=State.masterpass, type="password", color_scheme="green"),
                                            rx.heading(
                                                State.passwords[State.website],
                                                size='8', weight="bold", align="center",
                                                color='green',
                                            ),
                                        ),
                                    ),  
                                    rx.flex(
                                        
                                        rx.alert_dialog.cancel(
                                            rx.button("Close", on_click=State.dialog_switch, color_scheme="red"),
                                        ),  
                                        rx.alert_dialog.action(
                                            rx.button("Generate", on_click=State.create_pass, color_scheme="green"),
                                        ),
                                        rx.alert_dialog.action(
                                            rx.button("Copy", on_click=rx.set_clipboard(State.passwords[State.website])), 
                                        ),
                                        spacing="3",
                                    ),
                                ),
                                open=State.dialog_opened,
                            ),
                        ), direction="column", align="center",
                    ),
                ),
            ),
        ),
    ),
    
app = rx.App()
# app.add_page(index)
# app.add_page(passwords, route="/passwords")
