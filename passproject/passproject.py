import reflex as rx
import hashlib as hashf

bg = "gray"
n=0

class State(rx.State):
    name: str
    masterpass: str 
    site: str 
    show: bool = True
    passwords = {}
    content = []
    
    def create_pass(self) -> dict[str, ]:
        self.passwords[self.site] = hashf.sha512(self.site.encode()).hexdigest()[:4] + hashf.sha512(self.name.encode()).hexdigest()[:4] + hashf.sha512(self.masterpass.encode()).hexdigest()[:4]
        

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
                            rx.color_mode.button("Switch theme", color_scheme="green", size="2", variant="solid", align="right", trim="start"), margin="10px", padding="10px", border_radius="5px", 
                        ),
                        rx.text("ㅤㅤㅤㅤㅤㅤㅤ"),
                        bg="black",
                        color="white",
                        height="7vh", trim="both"
                    ),
                    rx.box("", height="30vh", bg=""),
                    rx.hstack(
                        rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
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
                            rx.input(on_change=State.set_site, value=State.site, color_scheme="green"),
                            rx.button(
                                "Create",
                                color_scheme="green",
                                on_click=State.create_pass,
                                size="4"
                            ), 
                            rx.heading(
                                State.passwords[State.site],
                                size='8', weight="bold", align="center",
                                color='green',
                            ), align="center", direction="column",
                        ), 
                        rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("site1", color_scheme="green"),
                                    rx.table.column_header_cell("site2", color_scheme="green"),
                                    rx.table.column_header_cell("site3", color_scheme="green"),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.cell("password1-1", color_scheme="green"),
                                    rx.table.cell("password1-2", color_scheme="green"),
                                    rx.table.cell("password1-3", color_scheme="green"),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.cell("password2-1", color_scheme="green"),
                                    rx.table.cell("password2-2", color_scheme="green"),
                                    rx.table.cell("password2-3", color_scheme="green"),
                                ),
                            ), color_scheme="green"
                        ),
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
                                    rx.input(on_change=State.set_site, value=State.site, color_scheme="green"),
                                    rx.button(
                                        "Create",
                                        color_scheme="green",
                                        on_click=State.create_pass,
                                        size="4"
                                    ), 
                                    rx.heading(
                                        State.passwords[State.site],
                                        size='8', weight="bold", align="center",
                                        color='green',
                                    ), align="center", direction="column",
                                ), 
                                rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
                                rx.table.root(
                                    rx.table.header(
                                        rx.table.row(
                                            rx.table.column_header_cell("site1", color_scheme="green"),
                                            rx.table.column_header_cell("site2", color_scheme="green"),
                                            rx.table.column_header_cell("site3", color_scheme="green"),
                                        ),
                                    ),
                                    rx.table.body(
                                        rx.table.row(
                                            rx.table.cell("password1-1", color_scheme="green"),
                                            rx.table.cell("password1-2", color_scheme="green"),
                                            rx.table.cell("password1-3", color_scheme="green"),
                                        ),
                                    ),
                                    rx.table.body(
                                        rx.table.row(
                                            rx.table.cell("password2-1", color_scheme="green"),
                                            rx.table.cell("password2-2", color_scheme="green"),
                                            rx.table.cell("password2-3", color_scheme="green"),
                                        ),
                                    ),
                                ), align="center", direction="column", color_scheme="green"
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
      
    
app = rx.App()
app.add_page(index)