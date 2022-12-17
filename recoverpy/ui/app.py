from textual.app import App
from textual.reactive import Reactive

from ui.screens.screen_search_params import SearchParamsScreen

from ui.css import get_css

from ui.screens.screen_search import SearchScreen


class RecoverpyApp(App):
    SCREENS = {"params": SearchParamsScreen(),
               "search": SearchScreen()}
    CSS_PATH = get_css()

    def on_mount(self) -> None:
        self.dark = Reactive(True)
        self.push_screen("params")

    async def on_search_params_screen_continue(self, message: SearchParamsScreen.Continue) -> None:
        self.pop_screen()
        await self.push_screen("search")
        await self.get_screen("search").post_message(
            SearchScreen.Start(self, message.searched_string, message.selected_partition)
        )
        print("start search message sent")
