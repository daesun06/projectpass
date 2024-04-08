import reflex as rx
import hashlib as hashf
# dont know how to set up reflex on my desktop

bg = "#1D2330"

class State(rx.State):
    name: str
    masterpass: str 
    site: str 
    show: bool = True
    passwords = {}
    
    def create_pass(self) -> dict[str, ]:
        self.passwords[self.site] = hashf.sha512(self.site.encode()).hexdigest()[:4] + hashf.sha512(self.name.encode()).hexdigest()[:4] + hashf.sha512(self.masterpass.encode()).hexdigest()[:4]

def index():
    return rx.hstack(
        rx.hstack(
            rx.text("ㅤㅤ"),
            rx.badge(
                "Password Generator", 
                variant="soft", 
                color_scheme="blue",
                bg="royalblue",
                color="white",
                ),
            rx.text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"),
            rx.link(
                "GitHub",
                href="https://github.com/daesun06/projectpass",
                color="green",
            ),
            rx.text("ㅤㅤ"),
            bg="black",
            color="white",
            height="5vh",
        ),
        rx.box("", height="40vh", bg=""),
        rx.vstack(
            rx.text("Enter your name:"),
            rx.hstack(
                rx.input(on_change=State.set_name, value=State.name),
            ),
            rx.text("Enter or create your master password:"),
            rx.hstack(
                rx.input(on_change=State.set_masterpass, value=State.masterpass),
            ),
            rx.text("Enter the name of the site:"),
            rx.hstack(
                rx.input(on_change=State.set_site, value=State.site),
                rx.button(
                    "Create",
                    color_scheme="green",
                    on_click=State.create_pass,
                ),
            ),
            rx.heading(
                State.passwords[State.site],
                size='5',
                color='goldenrod',
            ),
        ),
        rx.box("", height="40vh", bg="bg"),
        center_content=True,
        bg="bg",
        color="white",
    )

app = rx.App()
app.add_page(index)
