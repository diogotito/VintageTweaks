import sublime
import sublime_plugin


class CloseFileWithoutPrompting(sublime_plugin.WindowCommand):
    def run(self):
        # Mark the active view (tab) as scratch, so that Sublime doesn't
        # prompt about unsaved changes on close
        the_tab = self.window.active_view()
        the_tab.set_scratch(True)
        the_tab.close()

        # Removing the scratch status brings back the dot indicator in the tab
        # if there are unsaved changes, and Sublime prompts again for unsaved
        # changes on close.
        self.window.active_view().set_scratch(False)
