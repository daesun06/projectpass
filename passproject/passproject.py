import reflex as rx
import hashlib as hashf
# dont know how to set up reflex on my desktop

bg = "gray"

class State(rx.State):
    name: str
    masterpass: str 
    site: str 
    show: bool = True
    passwords = {}
    
    def create_pass(self) -> dict[str, ]:
        self.passwords[self.site] = hashf.sha512(self.site.encode()).hexdigest()[:4] + hashf.sha512(self.name.encode()).hexdigest()[:4] + hashf.sha512(self.masterpass.encode()).hexdigest()[:4]

def index():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.text("ㅤㅤ"),
                rx.badge(
                    "Password Generator",   
                    variant="solid", 
                    color_scheme="green",
                    bg="green",
                    color="white",
                    ),
                rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
                rx.color_mode.button("Switch theme", color_scheme="green", size="1", variant="solid", bg="green"),
                rx.link(
                    rx.text.strong("GitHub", color_scheme="green"),
                    href="https://github.com/daesun06/projectpass",
                    color="green",
                    _hover={"cursor": "pointer"},
                ),
                rx.text("ㅤㅤ"),
                bg="black",
                color="white",
                height="5vh", trim="both"
            ),
            rx.box("", height="30vh", bg=""),
            rx.center(
                rx.hstack(
                    rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
                    rx.vstack(
                        rx.text("Enter your name:", align="center", color_scheme="green"),
                        rx.hstack(
                            rx.input(on_change=State.set_name, value=State.name, color_scheme="green"),
                        ),
                        rx.text("Enter or create your master password:", align="center", color_scheme="green"),
                        rx.hstack(
                            rx.input(on_change=State.set_masterpass, value=State.masterpass, type="password", color_scheme="green"),
                        ),
                        rx.text("Enter the name of the site:", align="center", color_scheme="green"),
                        rx.hstack(
                            rx.input(on_change=State.set_site, value=State.site, color_scheme="green"),
                            rx.button(
                                "Create",
                                color_scheme="green",
                                on_click=State.create_pass,
                            ),
                        ),
                    ),
                ),
                rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
                rx.heading(
                    State.passwords[State.site],
                    size='8', weight="bold", align="center",
                    color='green',
                ),
                
            ),
        ),
        rx.box("", height="50vh", bg="bg"),
        center_content=True,
        bg="bg",
        color="gray",
    )
    

app = rx.App()
app.add_page(index)
