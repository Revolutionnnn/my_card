import flet
from flet import (
    Column,
    Container,
    Page,
    Text,
    UserControl,
    border_radius,
    colors,
    alignment,
    padding,
    CircleAvatar,
    Theme,
    Divider,
    ListTile, Icon, icons, Image,
)

import webbrowser


class MICard(UserControl):
    # Link of profiles,you can change with your own
    urls = [
        "tel://+91966704XXX",
        "mailto://test@flet.com",
        "https://twitter.com/ganandocriptomonedas",
        "https://github.com/Revolutionnnn"

    ]

    def build(self):
        return Container(
            # using padding control as same Flutter EdgeInsets.symmetric()
            padding=padding.symmetric(horizontal=20, vertical=50),
            # alignment for aligning content in center
            alignment=alignment.center,
            # child control
            content=Column(
                alignment="center",
                horizontal_alignment="center",
                # fixed vertical spacing in b/w child controls
                spacing=20,
                controls=[
                    CircleAvatar(
                        background_image_url="https://avatars.githubusercontent.com/u/94705606?s=400&u=8a1255617900bf23ab504963daa33f453e2009fd&v=4",
                        bgcolor=colors.WHITE,
                        max_radius=100
                    ),

                    # Text control
                    Text("MAICOL", font_family='dancing_script', size=40),

                    Text("Python Developer", size=30, color=colors.WHITE),

                    Container(
                        width=1000,
                        padding=padding.symmetric(horizontal=20, vertical=10),
                        content=Divider(
                            color=colors.WHITE,
                            thickness=2,
                            height=50,
                        )
                    ),
                    self.tile_widget(icon=Icon(name=icons.CALL, color=colors.BLACK, size=50), title="+91 9667******",
                                     index=0),
                    self.tile_widget(icon=Icon(name=icons.EMAIL, color=colors.BLACK, size=50),
                                     title="test@flet.com",
                                     index=1),
                    self.tile_widget(
                        icon=Image(src="https://cdn-icons-png.flaticon.com/512/1384/1384033.png", fit="contain"),
                        title="@ganandocriptomonedas",
                        index=2),
                    self.tile_widget(
                        icon=Image(src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
                                   fit="contain"), title="Revolutionnnn",
                        index=3),

                ]
            )
        )

    # title widget
    def tile_widget(self, icon, title, index):
        return Container(
            width=1000,
            padding=padding.symmetric(horizontal=20, vertical=10),
            bgcolor=colors.WHITE,
            alignment=alignment.center,
            # it is same as flutter borderRadius.all()

            border_radius=border_radius.all(8),
            content=ListTile(
                leading=icon,
                title=Text(title, color=colors.BLACK),
                on_click=lambda e: self.onClick(index=index)
            )
        )

    def onClick(self, index):
        webbrowser.open_new_tab(self.urls[index])


def main(page: Page):
    page.title = "Mi Card"
    # making page content in center using horizontal and vertical alignment
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    # If page content required  scroll then it will enable scrolling in the page
    page.scroll = "adaptive"
    # Background color
    page.bgcolor = colors.RED_600
    # give all fonts that you are going to user
    page.fonts = {
        "dancing_script": "https://github.com/google/fonts/raw/main/ofl/dancingscript/DancingScript%5Bwght%5D.ttf"
    }
    # create application instance
    card = MICard()
    # add application's root control to the page

    page.add(card)


flet.app(target=main)