import sublime
import sublime_plugin


class CloseFileWithoutSaving(sublime_plugin.WindowCommand):
    def run(self):
        self.window.active_view().set_scratch(True)
        self.window.active_view().close()
        self.window.active_view().set_scratch(False)
