import reflex as rx

# DATOS
SITE_URLS = {
    "Ecuabet": "https://ecuabet.com/",
    "Bilitv": "https://www.bilibili.tv/",
    "computrabajo": "https://secure.computrabajo.com/",
    "Loteria": "https://www.loteria.com.ec/",
    "DataBet": "https://consultasecuador.com/",
    "Reflex": "https://reflex.dev/docs/getting-started/introduction/",
}

# STATE
class State(rx.State):
    current_site: str = list(SITE_URLS.keys())[0]

    @rx.var
    def current_url(self) -> str:
        return SITE_URLS[self.current_site]

    def change_site(self, site: str):
        self.current_site = site

# COMPONENTES
def tab_button(site_name: str):
    return rx.button(
        site_name,
        on_click=lambda: State.change_site(site_name),
        size="2",
        variant="solid",
        color_scheme="blue",
        flex="1",
    )


def tab_bar():
    return rx.hstack(
        rx.foreach(list(SITE_URLS.keys()), tab_button),
        width="100%",
        padding="0.5rem",
        bg="gray.100",
    )


def webview():
    return rx.box(
        rx.el.iframe(
            src=State.current_url,
            width="100%",
            height="100%",
            style={"border": "none"},
        ),
        flex="1",
        width="100%",
    )

# PAGE
def index():
    return rx.vstack(
        tab_bar(),
        webview(),
        height="100vh",
        width="100%",
        spacing="0",
        bg="white",
    )

app = rx.App()
app.add_page(index)